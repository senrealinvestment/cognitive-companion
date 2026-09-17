class NullLiteratureAdapter:
    async def assess(self, state):
        return {"research_status": "unavailable"}
