from collections.abc import Mapping
from decimal import Decimal
from types import MappingProxyType
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, field_serializer, field_validator

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
