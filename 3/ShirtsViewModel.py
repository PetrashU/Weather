from ShirtService import ShirtService

class ShirtsViewModel:
    def __init__(self, service: ShirtService) -> None:
        self._shirtsService = service
        self._Shirts = []

    @property
    def Shirts(self):
        return self._Shirts
    
    @Shirts.setter
    def Shirts(self, value: list):
        self._Shirts = value

    async def GetShirts(self):
        shirtsResult = await self._shirtsService.GetShirts()
        if (shirtsResult.Success):
            for shirt in shirtsResult.Data:
                self.Shirts.append(shirt)
    