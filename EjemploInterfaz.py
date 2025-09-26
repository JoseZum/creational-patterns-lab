
""" 
En Python no hay interfaces

Entonces creamos una clase abstracta "Figura" que actúa como interfaz (define qué métodos deben tener las clases hijas). 
 
Luego implementamos dos clases concretas:
"Circulo" y "Cuadrado" que heredan de Figura.

Importante usar @abstractmethod en los métodos porque:

Si hereda de ABC pero no usan @abstractmethod, su clase no obliga a las hijas a implementar nada.
"""

from abc import ABC, abstractmethod

class InterfazFigura(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Circulo(InterfazFigura):
    def area(self):
        pass

    def perimetro(self):
        pass


class Cuadrado(InterfazFigura):
    def area(self):
        pass

    def perimetro(self):
        pass
