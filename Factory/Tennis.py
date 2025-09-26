from .Zapato import Zapato

from .Zapato import Zapato

#this is the concrete product Tennis that implements the interface Zapato
class Tennis(Zapato):
    def __init__(self, id_zapato, nombre, estilo, disponibilidad,
                 talla, color, material, precio, stock):
        super().__init__(id_zapato, nombre, estilo, disponibilidad,
                         talla, color, material, precio, stock)

    def preparar_materiales(self):
        print(f"[{self.nombre}] seleccionando tela resistente y suela de goma.")
    
    def ensamblar(self):
        print(f"[{self.nombre}] ensamblando tenis talla {self.talla} con color {self.color}.")
    
    def empaquetar(self):
        self.fabricado = True
        print(f"[{self.nombre}] empaquetando tenis en caja deportiva.")
