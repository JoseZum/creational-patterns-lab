from .Zapato import Zapato   

from .Zapato import Zapato

#this is the concrete product Tacones that implements the interface Zapato
class Tacones(Zapato):
    def __init__(self, id_zapato, nombre, estilo, disponibilidad,
                 talla, color, material, precio, stock):
        super().__init__(id_zapato, nombre, estilo, disponibilidad,
                         talla, color, material, precio, stock)

    def preparar_materiales(self):
        print(f"[{self.nombre}] preparando cuero y tacón de acero reforzado.")
    
    def ensamblar(self):
        print(f"[{self.nombre}] ensamblando tacones elegantes de color {self.color}.")
    
    def empaquetar(self):
        self.fabricado = True
        print(f"[{self.nombre}] empaquetando tacones en caja de lujo y en una bolsa de seda.")
