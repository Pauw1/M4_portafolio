# 🦷 DentalManager

Sistema de gestión de pacientes para clínica dental desarrollado en Python. Este proyecto permite administrar la información de los pacientes, sus tratamientos y el estado financiero de su cuenta.

## 📋 Descripción del Proyecto

DentalManager es una aplicación de consola que simula un sistema CRUD (Crear, Leer, Actualizar, Borrar - lógicamente) para una clínica dental. Permite al usuario mantener un registro organizado de los pacientes y sus deudas.

El proyecto demuestra el uso de competencias técnicas fundamentales de programación:
- Estructuras de datos complejas (Listas de diccionarios).
- Control de flujo y validaciones.
- Modularización mediante funciones.

## 🚀 Funcionalidades Principales

1.  **Gestión de Pacientes:**
    - Registro de nuevos pacientes con validación de RUT único.
    - Almacenamiento de datos personales (Nombre, Edad, Teléfono, Previsión).
    - Visualización del estado (Activo/Inactivo).

2.  **Gestión de Tratamientos:**
    - Agregar tratamientos médicos a un paciente específico.
    - Cálculo automático de costos y actualización de saldo pendiente.

3.  **Sistema de Pagos:**
    - Registro de abonos o pagos totales.
    - Validación para no exceder el saldo adeudado.
    - Actualización automática del estado de los tratamientos a "Pagado" cuando la deuda es cero.

4.  **Búsqueda y Reportes:**
    - Búsqueda de pacientes por RUT.
    - Listado general de todos los pacientes con sus saldos.
    - Ficha técnica detallada por paciente.

## 🛠️ Tecnologías Aplicadas

El código implementa los siguientes conceptos de Python:

- **Variables y Tipos de Datos:** Manejo de `strings`, `ints`, `floats` para montos monetarios y `booleans` para el estado del paciente.
- **Ciclos (Loops):** Uso de `while True` para los menús interactivos y `for` para iterar sobre la base de datos de pacientes.
- **Condicionales:** Estructuras `if/elif/else` para la navegación del menú y validaciones de lógica de negocio (ej. no permitir pagos negativos).
- **Estructuras de Datos:** Uso de una lista principal (`pacientes_db`) que contiene diccionarios anidados (pacientes que contienen listas de tratamientos).
- **Funciones:** Código modularizado en funciones específicas (`agregar_paciente`, `registrar_pago`, etc.) para facilitar la lectura y mantenimiento.

## Instrucciones de Uso

1. Ejecutar el archivo principal:
   ```bash
   python dental_manager.py