class Jugador:
    def __init__(self, jocheCoins: int):
        self.jocheCoins = jocheCoins

    def agregarMonedas(self, cantidad: int):
        self.jocheCoins += cantidad

    def gastarMonedas(self, cantidad: int):
        if self.jocheCoins >= cantidad:
            self.jocheCoins -= cantidad
            return True
        return False