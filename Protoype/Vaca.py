from .Prototype import AnimalPrototype
from decimal import Decimal
import copy

class Vaca(AnimalPrototype):
    def __init__(self, edad: int, color: str, tamano: int, habilidadEspecial: str, valor: Decimal):
        super().__init__(edad, color, tamano, habilidadEspecial, valor)

    def alimentarse(self):
        print("La vaca mastica pasto")

    def emitirSonido(self):
        print("Muuu!")

    def moverse(self):
        print("La vaca camina pesadamente en 4 patas")

    def clone(self):
        return copy.deepcopy(self)