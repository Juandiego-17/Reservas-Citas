#Plan de mejoramiento Juan Mahecha ADSO 2717785 acerca de un sitio web de reservas de citas medicas
usuarios = {}

citas_medicas = {}

disponibilidadMedicos = {
    "Jose Rodriguez": {
        "Especialidad": "Odontologia",
        "Disponibilidad": {
            "09/05/2024": ["07:00", "08:00", "09:00"],
            "11/05/2024": ["09:00", "10:00", "11:00", "12:00"]
        }
    },
    "Julieth Lopez": {
        "Especialidad": "Odontologia",
        "Disponibilidad": {
            "10/05/2024": ["08:00", "09:00", "10:00"],
            "12/05/2024": ["09:00", "10:00", "11:00", "12:00"]
        }
    },
    "Tomas Chavarria": {
        "Especialidad": "Odontologia",
        "Disponibilidad": {
            "11/05/2024": ["09:00", "10:00", "11:00"],
            "13/05/2024": ["10:00", "11:00", "12:00", "13:00"]
        }
    },
    "Alejandro Garcia": {
        "Especialidad": "Medicina general",
        "Disponibilidad": {
            "10/05/2024": ["08:00", "09:00", "10:00"],
            "11/05/2024": ["08:00", "09:00", "10:00", "11:00"]
        }
    },
    "Lorena Cañon": {
        "Especialidad": "Medicina general",
        "Disponibilidad": {
            "11/05/2024": ["09:00", "10:00", "11:00"],
            "12/05/2024": ["09:00", "10:00", "11:00", "12:00"]
        }
    },
    "Valentina Gomez": {
        "Especialidad": "Medicina general",
        "Disponibilidad": {
            "12/05/2024": ["10:00", "11:00", "12:00"],
            "13/05/2024": ["10:00", "11:00", "12:00", "13:00"]
        }
    },
    "Sebastian Guzman": {
        "Especialidad": "Alergologia",
        "Disponibilidad": {
            "24/06/2024": ["09:00", "11:00", "13:00"],
            "28/06/2024": ["08:00", "10:00", "12:00", "14:00"]
        }
    },
    "Luis Hernandez": {
        "Especialidad": "Alergologia",
        "Disponibilidad": {
            "05/06/2024": ["10:00", "12:00", "14:00"],
            "10/06/2024": ["12:00", "14:00", "15:00"]
        }
    },
    "Eduardo Zapata": {
        "Especialidad": "Alergologia",
        "Disponibilidad": {
            "12/06/2024": ["07:00", "11:00", "16:00"],
            "15/06/2024": ["08:00", "10:00", "13:00", "15:00"]
        }
    }
}

historialPaciente = {}

def register():
    print("Por favor ingresa tus datos para registrarte:")
    nombre = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    usuarios[nombre] = contraseña
    print("Te has registrado exitosamente")

def login():
    print("Por favor ingresa tus datos para iniciar sesion:")
    nombre = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    if nombre in usuarios and usuarios[nombre] == contraseña:
        print("Has iniciado sesion con exito")
        return nombre
    else:
        print("Nombre de usuario o contraseña son incorrectos")
        return None

def verificarDisponibilidadMedico(medico, fecha, hora):
    if medico in disponibilidadMedicos and fecha in disponibilidadMedicos[medico]["Disponibilidad"]:
        if hora in disponibilidadMedicos[medico]["Disponibilidad"][fecha]:
            return True
    return False

def verificacionDeCitas(usuario, medico, fecha):
    for citas_usuario in citas_medicas.values():
        if citas_usuario["Medico"] == medico and citas_usuario["Fecha"] == fecha:
            return True
    return False

def reservaCitas(usuario):
    print("\nPor favor ingresa el tipo de consulta que necesitas:")
    print("1. Medicina general")
    print("2. Odontologia")
    print("3. Alergologia")
    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        especialidad = "Medicina general"
    elif opcion == "2":
        especialidad = "Odontologia"
    elif opcion == "3":
        especialidad = "Alergologia"
    else:
        print("Opcion no valida.")
        return

    print("Por favor ingresa los detalles para reservar una cita medica")
    fecha = input("Fecha (DD/MM/AAAA): ")
    hora = input("Hora (HH:MM): ")
    medico = input("Nombre del médico: ")

    if verificacionDeCitas(usuario, medico, fecha):
        print("Ya tienes una cita programada con el médico en esta fecha por favor selecciona otra fecha")
        return

    if not verificarDisponibilidadMedico(medico, fecha, hora):
        print("El medico no se encuentra disponible en la fecha y hora seleccionadas por favor elige otra fecha u hora")
        return

    motivo = input("Motivo de la cita: ")

    citas_medicas[usuario] = {"Especialidad": especialidad, "Fecha": fecha, "Hora": hora, "Medico": medico, "Motivo": motivo}
    print("La cita medica ha sido reservada con exito")

def agregarHistorialPaciente():
    print("Agregar Historial del Paciente:")
    nombre_paciente = input("Nombre del paciente: ")
    medico = input("Nombre del médico: ")
    fecha = input("Fecha de la cita médica (DD/MM/AAAA): ")
    hora = input("Hora de la cita médica (HH/MM): ")
    motivo = input("Motivo de la cita: ")
    descripcion = input("Descripción del historial: ")

    if nombre_paciente not in historialPaciente:
        historialPaciente[nombre_paciente] = []

    historialPaciente[nombre_paciente].append({
        "Fecha": fecha,
        "Hora": hora,
        "Médico": medico,
        "Motivo": motivo,
        "Descripción": descripcion
    })

    print("El historial del paciente ha sido agregado con éxito.")

def verificarHistorialdelPaciente(nombre_paciente):
    print("\nHistorial del Paciente:")
    if nombre_paciente in historialPaciente:
        for cita in historialPaciente[nombre_paciente]:
            print("Nombre del paciente:", nombre_paciente)
            print("Historial:")
            for key, value in cita.items():
                print(key + ":", value)
    else:
        print("No se ha encontrado historial para este paciente")

def menuDelUsuario(usuario):
    print(f"\nBienvenido {usuario}")   
    print("1. Reservar cita medica")
    print("2. Ver mis citas medicas")
    print("3. Verificación de historial del paciente")
    print("4. Agregari historial del paciente")
    print("5. Cerrar sesion")

# Función principal
def main():
    usuario_actual = None
    while True:
        if usuario_actual is None:
            print("\nBienvenido al sistema hospitalario de Ibague")
            print("1. Registrar")
            print("2. Iniciar sesión")
            print("3. Salir")
            opcion = input("Selecciona una opcion: ")

            if opcion == "1":
                register()
            elif opcion == "2":
                usuario_actual = login()
            elif opcion == "3":
                print("Hasta luego")
                break
            else:
                print("Por favor selecciona una opcion válida")
        else:
            menuDelUsuario(usuario_actual)
            opcion = input("Selecciona una opcion: ")

            if opcion == "1":
                reservaCitas(usuario_actual)
            elif opcion == "2":
                if usuario_actual in citas_medicas:
                    cita = citas_medicas[usuario_actual]
                    print("Tus citas medicas aqui:")
                    for key, value in cita.items():
                        print(key + ":", value)
                else:
                    print("Aun no tienes una cita medica programada")
            elif opcion == "3":
                verificarHistorialdelPaciente(usuario_actual)
            elif opcion == "4":
                agregarHistorialPaciente()
            elif opcion == "5":
                print(f"Hasta luego {usuario_actual}")
                usuario_actual = None
            else:
                print("Por favor selecciona una opcion válida")

if __name__ == "__main__":
    main()