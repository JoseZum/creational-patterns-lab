# Laboratorio de Patrones de Diseño Creacionales

En esta practica programada implementa tres patrones de diseño creacionales fundamentales: **Singleton**, **Prototype** y **Factory Method**.

## Patrones Implementados

### 1. Patrón Singleton - Sistema de Conexión a Base de Datos
**Ubicación:** `Singleton/`

**Propósito:** Garantizar que solo exista una única instancia de la conexión a la base de datos en toda la aplicación, compartida por todos los módulos.

**Implementación:**
- **`ConexionBaseDatos.py`**: Clase Singleton que gestiona la conexión única
- **`Ventas.py`**: Controlador de ventas que usa el Singleton
- **`Inventarios.py`**: Controlador de inventarios que usa el Singleton
- **`Reportes.py`**: Controlador de reportes que usa el Singleton

**Características:**
- Una única instancia compartida
- Estado sincronizado entre todas las referencias
- Control de conexión y desconexión centralizado

---

### 2. Patrón Prototype - Animales de Granja
**Ubicación:** `Protoype/`

**Propósito:** Permitir la creación de nuevos objetos mediante la clonación de instancias existentes, útil cuando crear un objeto desde cero es costoso.

**Implementación:**
- **`Prototype.py`**: Interfaz `AnimalPrototype` con método `clone()`
- **`Vaca.py`**: Implementación concreta con clonación profunda
- **`Oveja.py`**: Implementación concreta con clonación profunda
- **`Gallina.py`**: Implementación concreta con clonación profunda

**Características:**
- Clonación profunda usando `copy.deepcopy()`
- Independencia entre objeto original y clones
- Cada animal tiene atributos específicos: edad, color, tamaño, habilidad especial y valor

---

### 3. Patrón Factory Method - Fábrica de Zapatos
**Ubicación:** `Factory/`

**Propósito:** Definir una interfaz para crear objetos, pero permitir que las subclases decidan qué clase instanciar.

**Implementación:**
- **`Factory.py`**: Interfaz abstracta del creador (Factory)
- **`Zapato.py`**: Interfaz abstracta del producto con métodos de fabricación
- **`Tennis.py`**: Producto concreto - Zapatos deportivos
- **`Tacones.py`**: Producto concreto - Zapatos de tacón
- **`FactoryTennis.py`**: Factory concreto para crear tennis
- **`FactoryTacones.py`**: Factory concreto para crear tacones

**Características:**
- Proceso de fabricación en tres pasos: preparar materiales, ensamblar, empaquetar
- Cada tipo de zapato tiene su propia factory
- Polimorfismo a través de la interfaz `Zapato`

---

## Guía de Instalación

### Requisitos Previos
- **Python 3.7 o superior**

Para verificar tu versión de Python:
```bash
python --version
```
o en algunos sistemas:
```bash
python3 --version
```

### Paso 1: Clonar o Descargar el Proyecto

Si tienes el proyecto en un repositorio Git:
```bash
git clone <url-del-repositorio>
cd creational-patterns-lab
```

O simplemente navega al directorio donde descargaste el proyecto.

### Paso 2: Verificar la Estructura

Asegúrate de que todos los archivos estén en su lugar. El proyecto no requiere instalación de dependencias externas, solo usa bibliotecas estándar de Python.

---

## Cómo Ejecutar las Pruebas

### Opción 1: Desde la línea de comandos

Abre una terminal en el directorio raíz del proyecto y ejecuta:

```bash
python test_patrones.py
```

O en algunos sistemas:
```bash
python3 test_patrones.py
```

### Opción 2: Desde un IDE

Si usas un IDE como PyCharm, VS Code o similar:
1. Abre el proyecto en tu IDE
2. Localiza el archivo `test_patrones.py`
3. Haz clic derecho y selecciona "Run" o "Ejecutar"

---

## Qué Esperar de las Pruebas

El script `test_patrones.py` ejecutará pruebas exhaustivas de los tres patrones:

### Pruebas del Patrón Singleton
- Verificación de que todas las instancias son la misma
- Prueba de estado compartido
- Uso desde múltiples controladores

### Pruebas del Patrón Prototype
- Clonación de vacas, ovejas y gallinas
- Verificación de independencia entre originales y clones
- Modificación de clones sin afectar originales
- Clonación múltiple

### Pruebas del Patrón Factory
- Creación de tennis mediante `FactoryTennis`
- Creación de tacones mediante `FactoryTacones`
- Proceso completo de fabricación
- Creación de múltiples productos
- Verificación de polimorfismo

---

## Salida Esperada

Al ejecutar el script, verás una salida detallada que incluye:

```
╔════════════════════════════════════════════════════════════════════╗
║          LABORATORIO DE PATRONES DE DISEÑO CREACIONALES           ║
╚════════════════════════════════════════════════════════════════════╝

======================================================================
PRUEBAS PATRÓN SINGLETON - ConexionBaseDatos
======================================================================
...

======================================================================
PRUEBAS PATRÓN PROTOTYPE - Animales de Granja
======================================================================
...

======================================================================
PRUEBAS PATRÓN FACTORY - Fábrica de Zapatos
======================================================================
...

======================================================================
RESUMEN DE PRUEBAS
======================================================================
Patrón Singleton: Verificado correctamente
Patrón Prototype: Verificado correctamente
Patrón Factory: Verificado correctamente

======================================================================
TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE
======================================================================
```

---

## Solución de Problemas

### Error: "No module named 'Singleton'" (o similar)

**Solución:** Asegúrate de estar ejecutando el script desde el directorio raíz del proyecto donde están las carpetas `Singleton/`, `Protoype/` y `Factory/`.

### Error: "ModuleNotFoundError"

**Solución:** Verifica que todos los archivos `__init__.py` existan en las carpetas `Singleton/` y `Factory/`. Si no existen, créalos (pueden estar vacíos).

### Error: "Python no se reconoce como comando"

**Solución:** Python no está instalado o no está en el PATH del sistema. Instala Python desde [python.org](https://www.python.org/downloads/) y asegúrate de marcar la opción "Add Python to PATH" durante la instalación.

---

## Notas Adicionales

- El patrón Prototype usa clonación profunda (`copy.deepcopy()`) para garantizar que los clones sean completamente independientes
- El patrón Factory incluye atributos adicionales en la clase `Zapato` que no estaban en el diseño original, para hacer la implementación más completa
- Cada patrón está contenido en su propio módulo para facilitar la comprensión y el mantenimiento

---
