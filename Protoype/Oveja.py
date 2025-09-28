from .Prototype import AnimalPrototype
from decimal import Decimal
import copy

class Oveja(AnimalPrototype):
    def __init__(self, edad: int, color: str, tamano: int, habilidadEspecial: str, valor: Decimal):
        super().__init__(edad, color, tamano, habilidadEspecial, valor)

    def alimentarse(self):
        print("La oveja come hierba")

    def emitirSonido(self):
        print("Beee beee!")

    def moverse(self):
        print("La oveja se mueve en grupo a 4 patas")

    def clone(self):
        return copy.deepcopy(self)