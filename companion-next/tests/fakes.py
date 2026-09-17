from types import SimpleNamespace

PROBABILITIES = dict(anaphylaxis=.803, malignant_hyperthermia=.1, other_or_unclear=.1)


def answer(**changes):
    return SimpleNamespace(**(dict(choice="anaphylaxis", probabilities=PROBABILITIES.copy(),
                                  confidence=.73) | changes))


def response(value=None):
    return SimpleNamespace(choices={"algorithm": value if value is not None else answer()})


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
