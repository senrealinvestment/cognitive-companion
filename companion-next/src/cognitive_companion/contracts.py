from collections.abc import Mapping
from decimal import Decimal
from types import MappingProxyType
from typing import Annotated, Literal, get_args

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_serializer,
    field_validator,
    model_validator,
)

from .catalog import IDS

Probability = Annotated[float, Field(strict=True, ge=0, le=1, allow_inf_nan=False)]
Revision = Annotated[int, Field(strict=True, gt=0)]


class FrozenModel(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid", strict=True)


class EncounterState(FrozenModel):
    session_id: str
    revision: Revision
    transcript: str

    @field_validator("session_id", "transcript")
    @classmethod
    def nonblank(cls, value):
        if not value.strip():
            raise ValueError("must be nonblank")
        return value


class JevAssessment(FrozenModel):
    revision: Revision
    selected_id: Literal["anaphylaxis", "malignant_hyperthermia", "other_or_unclear"]
    probabilities: Mapping[str, Probability]
    confidence: Probability
    latency_ms: Annotated[float, Field(strict=True, ge=0, allow_inf_nan=False)]

    @field_validator("probabilities")
    @classmethod
    def valid_probabilities(cls, value):
        if set(value) != set(IDS):
            raise ValueError("probability keys must exactly match catalog")
        mass = sum(Decimal(str(probability)) for probability in value.values())
        if abs(mass - Decimal(1)) > Decimal("0.01"):
            raise ValueError("probabilities must sum to one within 0.01")
        return MappingProxyType(dict(value))

    @field_serializer("probabilities")
    def serialize_probabilities(self, value):
        return dict(value)


# Gate-only synthetic engineering contracts; unrelated to the slice-1 catalog.
ModeHint = Literal["emergency", "rounds", "neither"]
GateFamily = Literal["airway", "circulation", "metabolic", "other"]
FiniteNonnegativeFloat = Annotated[float, Field(strict=True, ge=0, allow_inf_nan=False)]


class GateChoice(FrozenModel):
    choice: str
    probabilities: Mapping[str, Probability]
    confidence: Probability

    @field_validator("probabilities")
    @classmethod
    def freeze_distribution(cls, value):
        mass = sum(Decimal(str(p)) for p in value.values())
        if abs(mass - Decimal(1)) > Decimal("0.01"):
            raise ValueError("probabilities must sum to one within 0.01")
        return MappingProxyType(dict(value))

    @model_validator(mode="after")
    def validate_selection(self):
        labels = get_args(type(self).model_fields["choice"].annotation)
        if set(self.probabilities) != set(labels):
            raise ValueError("probability keys must exactly match declared labels")
        if self.probabilities[self.choice] != max(self.probabilities.values()):
            raise ValueError("selected label must have maximum probability")
        return self

    @field_serializer("probabilities")
    def serialize_distribution(self, value):
        return dict(value)

    @property
    def unique_maximum(self) -> bool:
        return (
            list(self.probabilities.values()).count(self.probabilities[self.choice])
            == 1
        )


class ModeJudgment(GateChoice):
    choice: ModeHint


class FamilyJudgment(GateChoice):
    choice: GateFamily


class GateJudgments(FrozenModel):
    decision_shaped: Probability
    enough_evidence: Probability
    mode_hint: ModeJudgment
    family: FamilyJudgment


class JevGateSilence(FrozenModel):
    revision: Revision
    outcome: Literal["silence"]
    pack: None
    mode_hint: ModeHint
    mode_hint_advisory: Literal[True] = Field(
        description="Advisory only; Python owns mode."
    )
    latency_ms: FiniteNonnegativeFloat


class JevGateRetrieve(FrozenModel):
    revision: Revision
    outcome: Literal["retrieve"]
    pack: GateFamily
    mode_hint: Literal["emergency", "rounds"]
    mode_hint_advisory: Literal[True] = Field(
        description="Advisory only; Python owns mode."
    )
    latency_ms: FiniteNonnegativeFloat


JevGate = Annotated[JevGateSilence | JevGateRetrieve, Field(discriminator="outcome")]
