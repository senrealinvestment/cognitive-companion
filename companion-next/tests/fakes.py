from types import SimpleNamespace

PROBABILITIES = {
    "anaphylaxis": 0.803,
    "malignant_hyperthermia": 0.1,
    "other_or_unclear": 0.1,
}


def answer(**changes):
    return SimpleNamespace(
        **(
            {
                "choice": "anaphylaxis",
                "probabilities": PROBABILITIES.copy(),
                "confidence": 0.73,
            }
            | changes
        )
    )


def response(value=None):
    return SimpleNamespace(
        choices={"algorithm": value if value is not None else answer()}
    )


class FakeSDK:
    def __init__(self, result=None, error=None):
        self.result = result if result is not None else response()
        self.error = error
        self.calls = []
        self.closed = False

    async def system_one(self, **kwargs):
        self.calls.append(kwargs)
        if self.error:
            raise self.error
        return self.result

    async def aclose(self):
        self.closed = True


def gate_choice(labels, selected, **changes):
    return SimpleNamespace(
        **(
            {
                "choice": selected,
                "confidence": 0.9,
                "probabilities": {label: float(label == selected) for label in labels},
            }
            | changes
        )
    )


def gate_response(*, mode="rounds", family="other", decision=0.9, evidence=0.9):
    return SimpleNamespace(
        nouls={
            "decision_shaped": SimpleNamespace(noul=decision),
            "enough_evidence": SimpleNamespace(noul=evidence),
        },
        choices={
            "mode_hint": gate_choice(("emergency", "rounds", "neither"), mode),
            "family": gate_choice(
                ("airway", "circulation", "metabolic", "other"), family
            ),
        },
    )
