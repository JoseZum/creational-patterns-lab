from abc import ABC, abstractmethod


#factory interface represent the creator in the factory method pattern
class Factory(ABC):
    @abstractmethod
    def crearZapato(self, id_zapato: int, nombre: str, estilo: str, disponibilidad: int,
                    talla: int, color: str, material: str, precio: float, stock: int):
        pass