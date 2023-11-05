from ServiceResponse import ServiceResponse
from ShirtSeeder import ShirtSeeder

class ShirtService:
    async def GetShirts(self):
        try:
            response = ServiceResponse()
            response.Data = ShirtSeeder().GenerateShirts()
            response.Message = "Ok"
            response.Success = True
            return response
        except:
            response = ServiceResponse()
            response.Message = "Problem with accesing base of shirts"
            response.Success = False
            return response
        
    async def ChangeShirt(self, id: int):
        try:
            response = ServiceResponse()
            ##TODO zmiana
            response.Message = "Modified record"
            response.Success = True
            return response
        except:
            response = ServiceResponse()
            response.Message = "Problem with modifing record in database"
            response.Success = False
            return response
        
    async def DeleteShirt(self, id: int):
        try:
            response = ServiceResponse()
            ##TODO usunięcie
            response.Message = "Record deleted"
            response.Success = True
            return response
        except:
            response = ServiceResponse()
            response.Message = "Problem with deleting record from database"
            response.Success = False
            return response

    async def AddShirt(self, color: str, design: str):
        try:
            response = ServiceResponse()
            ##TODO dodanie
            response.Message = "Record added"
            response.Success = True
            return response
        except:
            response = ServiceResponse()
            response.Message = "Problem with adding record to database"
            response.Success = False
            return response