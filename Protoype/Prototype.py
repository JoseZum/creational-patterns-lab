from abc import ABC, abstractmethod
from decimal import Decimal

# Interfaz AnimalPrototype
class AnimalPrototype(ABC):
    def __init__(self, edad: int, color: str, tamano: int, habilidadEspecial: str, valor: Decimal):
        self.edad = edad
        self.color = color
        self.tamano = tamano
        self.habilidadEspecial = habilidadEspecial
        self.valor = valor

    @abstractmethod
    def alimentarse(self):
        pass

    @abstractmethod
    def emitirSonido(self):
        pass

    @abstractmethod
    def moverse(self):
        pass
    
    @abstractmethod
    def clone(self) -> "AnimalPrototype":
        pass