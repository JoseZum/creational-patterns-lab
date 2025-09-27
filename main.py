from Factory.FactoryTennis import FactoryTennis 
from Factory.FactoryTacones import FactoryTacones


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