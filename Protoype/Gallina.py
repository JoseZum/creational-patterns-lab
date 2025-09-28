from .Prototype import AnimalPrototype
from decimal import Decimal
import copy

class Gallina(AnimalPrototype):
    def __init__(self, edad: int, color: str, tamano: int, habilidadEspecial: str, valor: Decimal):
        super().__init__(edad, color, tamano, habilidadEspecial, valor)

    def alimentarse(self):
        print("La gallina come semillas")

    def emitirSonido(self):
        print("Clo clo clo!")

    def moverse(self):
        print("La gallina camina a dos patas")
        
    def clone(self):
        return copy.deepcopy(self)