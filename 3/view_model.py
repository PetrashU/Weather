import tkinter as tk

from model import Model

class ViewModel:
    _entry: tk.StringVar

    def __init__(self, model: Model):
        self.model = model

    @property
    def entry(self) -> str:
        return self._entry.get()
    
    @entry.setter
    def entry(self, value: str):
        self._entry = tk.StringVar()
        self._entry.set(value)

    def getCity(self):
        return self.model.getCity(self._entry)

    def getForecast(self):
        return self.model.getForecast()
    
    def getCurrentConditions(self):
        return self.model.getCurrentConditions()
    
    def getIndices(self):
        return self.model.getIndices()