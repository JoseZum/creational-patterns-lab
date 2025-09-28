from typing import List
from decimal import Decimal
from .Prototype import AnimalPrototype
from .Jugador import Jugador

class Granja:
    def __init__(self):
        self.animales: List[AnimalPrototype] = []

    def comprarAnimal(self, jugador: Jugador, animal: AnimalPrototype, cantidad: int, costo: Decimal):
        total = costo * cantidad
        if jugador.gastarMonedas(total):
            for _ in range(cantidad):
                self.animales.append(animal.clone())
            print(f"Se compraron {cantidad} {animal.__class__.__name__}(s)")
            return True
        else:
            print("No hay suficientes JocheCoins para comprar")
            return False

    def venderAnimal(self, jugador: Jugador, animal: AnimalPrototype, cantidad: int, precio: Decimal):
        contador = 0
        for a in list(self.animales):
            if isinstance(a, animal.__class__):
                self.animales.remove(a)
                jugador.agregarMonedas(precio)
                contador += 1
                if contador == cantidad:
                    break
        if contador == cantidad:
            print(f"Se vendieron {cantidad} {animal.__class__.__name__}(s).")
            return True
        else:
            print("No hay suficientes animales de ese tipo para vender.")
            return False

    def criarAnimal(self, animal: AnimalPrototype):
        if animal in self.animales:
            nuevo = animal.clone()
            self.animales.append(nuevo)
            print(f"El animal {animal.__class__.__name__} ha criado una nueva cría.")
            return True
        print("Ese animal no está en la granja.")
        return False
