from typing import TypeVar

T = TypeVar("T")

class ServiceResponse:

    def __init__(self) -> None:
        self._Data = None
        self._Success = bool()
        self._Message = str()

    @property
    def Data(self):
        return self._Data
    
    @Data.setter
    def Data(self, value: T):
        self._Data = value

    @property
    def Success(self):
        return self._Success
    
    @Success.setter
    def Success(self, value: bool):
        self._Success = value

    @property
    def Message(self):
        return self._Message
    
    @Message.setter
    def Message(self, value: str):
        self._Message = value