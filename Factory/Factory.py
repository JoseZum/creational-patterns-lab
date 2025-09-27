from abc import ABC, abstractmethod


#factory interface represent the creator in the factory method pattern
class Factory(ABC):
    @abstractmethod
    def crearZapato(self, tipo: str):
        pass