from .Factory import Factory
from .Tacones import Tacones
from .Zapato import Zapato

#implementation of the factory method for creating Tacones to the interface Factory
class FactoryTacones(Factory):
    def crearZapato(self, id_zapato: int, nombre: str, estilo: str, disponibilidad: int,
                    talla: int, color: str, material: str, precio: float, stock: int) -> Zapato:
        return Tacones(id_zapato, nombre, estilo, disponibilidad,
                      talla, color, material, precio, stock)
