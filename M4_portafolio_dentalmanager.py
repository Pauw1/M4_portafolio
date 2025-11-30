pacientes_db = []

def mostrar_menu():
    print("\n🦷 DentalManager")
    print("1. Agregar nuevo paciente")
    print("2. Mostrar todos los pacientes")
    print("3. Salir")

def buscar_paciente(rut):
    for paciente in pacientes_db:
        if paciente["rut"] == rut:
            return paciente
    return None

def agregar_paciente():
    print("\n1. Agregar Nuevo Paciente")
    rut = input("Ingrese RUT (ej. 12345678-9): ").strip()
    
    if buscar_paciente(rut) is not None:
        print(f"Error: El RUT {rut} ya está registrado.")
        return

    nombre = input("Ingrese nombre completo: ").strip()
    try:
        edad = int(input("Ingrese edad: "))
    except ValueError:
        print("Error: La edad debe ser un número.")
        return
        
    telefono = input("Ingrese teléfono (ej. +569...): ").strip()
    tiene_prevision_input = input("¿Tiene previsión de salud? (s/n): ").lower().strip()
    es_paciente_activo = (tiene_prevision_input == 's')

    nuevo_paciente = {
        "rut": rut,
        "nombre": nombre,
        "edad": edad,
        "telefono": telefono,
        "activo": es_paciente_activo,
        "saldo_pendiente": 0.0,
        "tratamientos": []
    }

    pacientes_db.append(nuevo_paciente)
    print(f"¡Paciente {nombre} agregado con éxito!")

def mostrar_todos_pacientes():
    print("\nLista de Todos los Pacientes")
    if not pacientes_db:
        print("No hay pacientes registrados.")
        return
    for paciente in pacientes_db:
        estado = "Activo" if paciente["activo"] else "Inactivo"
        print(f"RUT: {paciente['rut']} | Nombre: {paciente['nombre']} | Estado: {estado}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            agregar_paciente()
        elif opcion == '2':
            mostrar_todos_pacientes()
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()