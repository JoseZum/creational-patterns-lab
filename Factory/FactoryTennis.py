from .Factory import Factory
from .Tennis import Tennis
from .Zapato import Zapato

#implementation of the factory method for creating tennis to the interface Factory
class FactoryTennis(Factory):
    def crearZapato(self, id_zapato: int, nombre: str, estilo: str, disponibilidad: int,
                    talla: int, color: str, material: str, precio: float, stock: int) -> Zapato:
        return Tennis(id_zapato, nombre, estilo, disponibilidad,
                      talla, color, material, precio, stock)
