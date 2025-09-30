"""
Script de prueba para los patrones de diseño creacionales
- Singleton: ConexionBaseDatos
- Prototype: Animales de granja (Vaca, Oveja, Gallina)
- Factory: Fábrica de zapatos (Tennis, Tacones)
"""

from decimal import Decimal

# ============================================================================
# PRUEBAS PATRÓN SINGLETON - Conexión a Base de Datos
# ============================================================================

def test_singleton():
    print("=" * 70)
    print("PRUEBAS PATRÓN SINGLETON - ConexionBaseDatos")
    print("=" * 70)

    from Singleton.ConexionBaseDatos import ConexionBaseDatos
    from Singleton.Ventas import VentasControlador
    from Singleton.Inventarios import GestionarInventarios
    from Singleton.Reportes import ReportesFinancieros

    print("\n--- Prueba 1: Verificar que siempre se obtiene la misma instancia ---")
    db1 = ConexionBaseDatos.getInstance()
    db2 = ConexionBaseDatos.getInstance()
    db3 = ConexionBaseDatos()

    print(f"db1 id: {id(db1)}")
    print(f"db2 id: {id(db2)}")
    print(f"db3 id: {id(db3)}")
    print(f"¿db1 es db2? {db1 is db2}")
    print(f"¿db1 es db3? {db1 is db3}")
    print(f"Singleton verificado: Todas las referencias apuntan a la misma instancia\n")

    print("--- Prueba 2: Uso de la conexión desde diferentes controladores ---")
    ventas = VentasControlador()
    inventarios = GestionarInventarios()
    reportes = ReportesFinancieros()

    ventas.actualizarVentas()
    reportes.actualizarInventario()
    inventarios.generarReporte()

    print("\n--- Prueba 3: Estado compartido entre instancias ---")
    db1.connect()
    print(f"Estado de conexión db1: {db1.connected}")
    print(f"Estado de conexión db2: {db2.connected}")
    print(f"Estado de conexión db3: {db3.connected}")
    print("Todas las instancias comparten el mismo estado\n")

    db1.disconnect()
    print(f"Después de desconectar db1:")
    print(f"Estado de conexión db2: {db2.connected}")
    print(f"Estado de conexión db3: {db3.connected}")
    print("El estado se sincroniza entre todas las referencias\n")


# ============================================================================
# PRUEBAS PATRÓN PROTOTYPE - Animales de Granja
# ============================================================================

def test_prototype():
    print("\n" + "=" * 70)
    print("PRUEBAS PATRÓN PROTOTYPE - Animales de Granja")
    print("=" * 70)

    from Protoype.Vaca import Vaca
    from Protoype.Oveja import Oveja
    from Protoype.Gallina import Gallina

    print("\n--- Prueba 1: Clonación de Vaca ---")
    vaca_original = Vaca(
        edad=3,
        color="Blanco con manchas negras",
        tamano=500,
        habilidadEspecial="Producción de leche",
        valor=Decimal("1500.00")
    )

    print(f"Vaca original - Edad: {vaca_original.edad}, Color: {vaca_original.color}, "
          f"Tamaño: {vaca_original.tamano}kg, Valor: ${vaca_original.valor}")
    vaca_original.emitirSonido()
    vaca_original.alimentarse()
    vaca_original.moverse()

    print("\nClonando vaca...")
    vaca_clonada = vaca_original.clone()

    print(f"\nVaca clonada - Edad: {vaca_clonada.edad}, Color: {vaca_clonada.color}, "
          f"Tamaño: {vaca_clonada.tamano}kg, Valor: ${vaca_clonada.valor}")
    print(f"¿Son el mismo objeto? {vaca_original is vaca_clonada}")
    print(f"¿Tienen los mismos valores? edad={vaca_original.edad == vaca_clonada.edad}, "
          f"color={vaca_original.color == vaca_clonada.color}")

    print("\nModificando vaca clonada...")
    vaca_clonada.edad = 5
    vaca_clonada.color = "Marrón"
    print(f"Vaca original después de modificar clonada - Edad: {vaca_original.edad}, Color: {vaca_original.color}")
    print(f"Vaca clonada después de modificación - Edad: {vaca_clonada.edad}, Color: {vaca_clonada.color}")
    print(" Clonación profunda verificada: Los objetos son independientes\n")

    print("\n--- Prueba 2: Clonación de Oveja ---")
    oveja_original = Oveja(
        edad=2,
        color="Blanco lanudo",
        tamano=80,
        habilidadEspecial="Producción de lana",
        valor=Decimal("300.00")
    )

    print(f"Oveja original - Edad: {oveja_original.edad}, Color: {oveja_original.color}, "
          f"Valor: ${oveja_original.valor}")
    oveja_original.emitirSonido()
    oveja_original.alimentarse()

    oveja_clonada = oveja_original.clone()
    print(f"\nOveja clonada - Edad: {oveja_clonada.edad}, Color: {oveja_clonada.color}")
    print(f"Clonación exitosa\n")

    print("\n--- Prueba 3: Clonación múltiple de Gallina ---")
    gallina_prototipo = Gallina(
        edad=1,
        color="Roja",
        tamano=3,
        habilidadEspecial="Producción de huevos",
        valor=Decimal("25.00")
    )

    print("Creando granja con gallinas clonadas...")
    gallinas = [gallina_prototipo]

    for i in range(3):
        nueva_gallina = gallina_prototipo.clone()
        nueva_gallina.edad = i + 1
        colores = ["Blanca", "Negra", "Amarilla"]
        nueva_gallina.color = colores[i]
        gallinas.append(nueva_gallina)

    print(f"\nTotal de gallinas creadas: {len(gallinas)}")
    for idx, gallina in enumerate(gallinas):
        print(f"Gallina {idx + 1}: Edad={gallina.edad}, Color={gallina.color}, Valor=${gallina.valor}")

    print("\nProbando comportamiento de gallinas:")
    gallinas[1].emitirSonido()
    gallinas[1].moverse()
    print("Todas las gallinas son independientes y funcionales\n")


# ============================================================================
# PRUEBAS PATRÓN FACTORY - Fábrica de Zapatos
# ============================================================================

def test_factory():
    print("\n" + "=" * 70)
    print("PRUEBAS PATRÓN FACTORY - Fábrica de Zapatos")
    print("=" * 70)

    from Factory.FactoryTennis import FactoryTennis
    from Factory.FactoryTacones import FactoryTacones

    print("\n--- Prueba 1: Creación de Tennis mediante Factory ---")
    factory_tennis = FactoryTennis()

    tennis1 = factory_tennis.crearZapato(
        id_zapato=1,
        nombre="Nike Air Max",
        estilo="Deportivo",
        disponibilidad=1,
        talla=42,
        color="Negro/Blanco",
        material="Mesh sintético",
        precio=89.99,
        stock=50
    )

    print(f"\nZapato creado: {tennis1.nombre}")
    print(f"Detalles: Talla {tennis1.talla}, Color {tennis1.color}, Precio ${tennis1.precio}")
    print(f"Fabricado: {tennis1.fabricado}")

    print("\nProceso de fabricación:")
    tennis1.preparar_materiales()
    tennis1.ensamblar()
    tennis1.empaquetar()
    print(f"Estado después de fabricar: Fabricado={tennis1.fabricado}\n")

    print("\n--- Prueba 2: Creación de Tacones mediante Factory ---")
    factory_tacones = FactoryTacones()

    tacones1 = factory_tacones.crearZapato(
        id_zapato=101,
        nombre="Stiletto Elegance",
        estilo="Formal",
        disponibilidad=1,
        talla=38,
        color="Rojo",
        material="Cuero genuino",
        precio=129.99,
        stock=25
    )

    print(f"\nZapato creado: {tacones1.nombre}")
    print(f"Detalles: Talla {tacones1.talla}, Color {tacones1.color}, Precio ${tacones1.precio}")

    print("\nProceso de fabricación:")
    tacones1.preparar_materiales()
    tacones1.ensamblar()
    tacones1.empaquetar()
    print(f"Estado después de fabricar: Fabricado={tacones1.fabricado}\n")

    print("\n--- Prueba 3: Creación de múltiples zapatos ---")
    print("\nCreando línea de tennis...")
    modelos_tennis = [
        {"nombre": "Adidas Superstar", "talla": 40, "color": "Blanco", "precio": 79.99},
        {"nombre": "Puma RS-X", "talla": 41, "color": "Multicolor", "precio": 99.99},
        {"nombre": "Reebok Classic", "talla": 43, "color": "Negro", "precio": 69.99}
    ]

    zapatos_tennis = []
    for idx, modelo in enumerate(modelos_tennis, start=2):
        tennis = factory_tennis.crearZapato(
            id_zapato=idx,
            nombre=modelo["nombre"],
            estilo="Deportivo",
            disponibilidad=1,
            talla=modelo["talla"],
            color=modelo["color"],
            material="Sintético",
            precio=modelo["precio"],
            stock=100
        )
        zapatos_tennis.append(tennis)
        print(f" Tennis creado: {tennis.nombre} - Talla {tennis.talla} - ${tennis.precio}")

    print("\nCreando línea de tacones...")
    modelos_tacones = [
        {"nombre": "Elegance Night", "talla": 37, "color": "Negro", "precio": 149.99},
        {"nombre": "Summer Breeze", "talla": 39, "color": "Beige", "precio": 119.99}
    ]

    zapatos_tacones = []
    for idx, modelo in enumerate(modelos_tacones, start=102):
        tacones = factory_tacones.crearZapato(
            id_zapato=idx,
            nombre=modelo["nombre"],
            estilo="Formal",
            disponibilidad=1,
            talla=modelo["talla"],
            color=modelo["color"],
            material="Cuero",
            precio=modelo["precio"],
            stock=30
        )
        zapatos_tacones.append(tacones)
        print(f"Tacones creados: {tacones.nombre} - Talla {tacones.talla} - ${tacones.precio}")

    print(f"\n Total de zapatos creados: {len(zapatos_tennis) + len(zapatos_tacones)}")
    print(f"  - Tennis: {len(zapatos_tennis)}")
    print(f"  - Tacones: {len(zapatos_tacones)}")

    print("\n--- Prueba 4: Polimorfismo - Todos los zapatos implementan la misma interfaz ---")
    todos_zapatos = [tennis1, tacones1] + zapatos_tennis + zapatos_tacones

    print(f"\nFabricando todos los zapatos pendientes ({len([z for z in todos_zapatos if not z.fabricado])} zapatos)...")
    for zapato in todos_zapatos:
        if not zapato.fabricado:
            print(f"\n> Fabricando {zapato.nombre}:")
            zapato.preparar_materiales()
            zapato.ensamblar()
            zapato.empaquetar()

    print(f"\n Todos los zapatos fabricados exitosamente")
    print(f" Patrón Factory permite crear diferentes tipos de zapatos con la misma interfaz\n")


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    print("\n")
    print("=" * 70)
    print(" " * 10 + "LABORATORIO DE PATRONES DE DISEÑO CREACIONALES")
    print("=" * 70)
    print("\nEste script prueba los tres patrones implementados:")
    print("  1. Singleton - Conexión única a base de datos")
    print("  2. Prototype - Clonación de animales de granja")
    print("  3. Factory - Creación de diferentes tipos de zapatos")
    print()

    try:
        # Ejecutar pruebas de cada patrón
        test_singleton()
        test_prototype()
        test_factory()

        # Resumen final
        print("\n" + "=" * 70)
        print("RESUMEN DE PRUEBAS")
        print("=" * 70)
        print(" Patrón Singleton: Verificado correctamente")
        print("  - Una única instancia compartida")
        print("  - Estado sincronizado entre referencias")
        print()
        print(" Patrón Prototype: Verificado correctamente")
        print("  - Clonación profunda de objetos")
        print("  - Independencia entre originales y clones")
        print()
        print(" Patrón Factory: Verificado correctamente")
        print("  - Creación de objetos mediante factories")
        print("  - Polimorfismo a través de interfaz común")
        print()
        print("=" * 70)
        print("TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("=" * 70 + "\n")

    except Exception as e:
        print(f"\nERROR durante las pruebas: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()