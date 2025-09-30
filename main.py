from decimal import Decimal

from Factory.FactoryTennis import FactoryTennis
from Factory.FactoryTacones import FactoryTacones

from Protoype.Granja import Granja
from Protoype.Jugador import Jugador
from Protoype.Vaca import Vaca
from Protoype.Oveja import Oveja
from Protoype.Gallina import Gallina

if __name__ == "__main__":
    #create tennis factory to create tennis shoes
    factory_tennis = FactoryTennis()
    tenis = factory_tennis.crearZapato(1, "Nike Air", "Deportivo", 50, 42, "Blanco con azul", "Tela y goma", 120.0, 100)

    #call methods to prepare, assemble and package the shoe
    tenis.preparar_materiales()
    tenis.ensamblar()
    tenis.empaquetar()

    print("")

    # create tacones factory to create high heels shoes
    factory_tacones = FactoryTacones()
    tacones = factory_tacones.crearZapato(2, "Prada Elegance", "Formal", 20, 37, "Rojo brillante", "Cuero y acero", 200.0, 30)

    tacones.preparar_materiales()
    tacones.ensamblar()
    tacones.empaquetar()
    
    #Prototype Pattern
    jugador = Jugador(5000)
    granja = Granja()

    vaca = Vaca(5, "manchada", 500, "produce leche", Decimal("1000"))
    oveja = Oveja(3, "blanca", 60, "lana suave", Decimal("300"))
    gallina = Gallina(2, "amarilla", 10, "pone huevos", Decimal("100"))

    # Comprar animales
    granja.comprarAnimal(jugador, vaca, 2, vaca.valor)
    granja.comprarAnimal(jugador, oveja, 3, oveja.valor)
    granja.comprarAnimal(jugador, gallina, 5, gallina.valor)

    # Criar un animal
    granja.criarAnimal(granja.animales[0])

    # Vender animales
    granja.venderAnimal(jugador, oveja, 2, oveja.valor)

    print(f"\nJocheCoins restantes: {jugador.jocheCoins}")
    print(f"Animales en la granja: {len(granja.animales)}")