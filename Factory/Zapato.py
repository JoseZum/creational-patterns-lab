from abc import ABC, abstractmethod

#zapato interface represent the product in the factory method pattern
from abc import ABC, abstractmethod

class Zapato(ABC):
    def __init__(self, id_zapato: int, nombre: str, estilo: str, disponibilidad: int,
                 talla: int, color: str, material: str, precio: float, stock: int):
        self.id_zapato = id_zapato
        self.nombre = nombre
        self.estilo = estilo
        self.disponibilidad = disponibilidad
        self.talla = talla
        self.color = color
        self.material = material
        self.precio = precio
        self.stock = stock
        self.fabricado = False

    @abstractmethod
    def preparar_materiales(self):
        pass

    @abstractmethod
    def ensamblar(self):
        pass

    @abstractmethod
    def empaquetar(self):
        pass

    def __str__(self): #return a string representation of the shoe object please ignore this method
        return (f"Zapato(id={self.id_zapato}, nombre={self.nombre}, estilo={self.estilo}, "
                f"talla={self.talla}, color={self.color}, material={self.material}, "
                f"precio=${self.precio}, stock={self.stock}, fabricado={self.fabricado})")
