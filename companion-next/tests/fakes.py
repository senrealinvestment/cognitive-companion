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
