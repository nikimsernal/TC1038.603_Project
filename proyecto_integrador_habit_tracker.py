"""
==========================================
PROYECTO INTEGRADOR: TC1038.603
Habit Tracker y Gestor de Productividad
==========================================
Kimberly Nikita Serna Lerma
GitHub Repo: https://github.com/nikimsernal/TC1038.603
==========================================
"""

import math

"""
==========================================
FUNCIONES DE HABITOS
==========================================
"""

# Agrega un nuevo habito a la lista.
def agregar_habito(habitos, nombre, meta):
    habito = {
        "nombre": nombre,
        "meta": meta,
        "completados": 0
    }
    habitos.append(habito)
    print("Habito agregado correctamente.")

# Registra una realizacion del habito.
def completar_habito(habitos, indice):
    if indice >= 0 and indice < len(habitos):
        habitos[indice]["completados"] += 1
        print("Habito actualizado.")
    else:
        print("Indice invalido.")

# Muestra todos los habitos registrados.
def mostrar_habitos(habitos):
    if len(habitos) == 0:
        print("No hay habitos registrados.")
    else:
        print("\n=== HABITOS ===")
        for i in range(len(habitos)):
            print(i, "-", habitos[i]["nombre"], "| Meta:", habitos[i]["meta"], "| Completados:", habitos[i]["completados"] )


"""
==========================================
FUNCIONES DE TO-DO LIST
==========================================
"""

# Agrega una nueva tarea a la lista de pendientes.
# "origen" indica de donde viene la tarea:
# "Manual", "Canvas" o "Google Calendar".
def agregar_tarea(tareas, nombre, origen="Manual"):
    tarea = {
        "nombre": nombre,
        "origen": origen,
        "completada": False
    }
    tareas.append(tarea)
    print("Tarea agregada correctamente.")

# Marca una tarea como completada.
def completar_tarea(tareas, indice):
    if indice >= 0 and indice < len(tareas):
        tareas[indice]["completada"] = True
        print("Tarea marcada como completada.")
    else:
        print("Indice invalido.")

# Muestra todas las tareas registradas.
def mostrar_tareas(tareas):
    if len(tareas) == 0:
        print("No hay tareas registradas.")
    else:
        print("\n=== TO-DO LIST ===")
        for i in range(len(tareas)):
            estado = "Completada" if tareas[i]["completada"] else "Pendiente"
            print(i, "-", tareas[i]["nombre"], "| Origen:", tareas[i]["origen"], "| Estado:", estado )

"""
==========================================
FUNCIONES DE ESTADISTICAS
==========================================
"""

# Calcula el porcentaje de cumplimiento
# considerando todos los habitos.
def calcular_porcentaje(habitos):
    total_meta = 0
    total_realizado = 0

    for habito in habitos:
        total_meta += habito["meta"]
        total_realizado += habito["completados"]
    if total_meta == 0:
        return 0

    porcentaje = (total_realizado / total_meta) * 100
    return porcentaje

# Muestra un resumen de productividad.
def mostrar_estadisticas(habitos):
    porcentaje = calcular_porcentaje(habitos)

    print("\n=== ESTADISTICAS ===")
    print("Cumplimiento:", round(porcentaje, 2), "%")

    if porcentaje >= 100:
        print("Excelente trabajo.")
    elif porcentaje >= 70:
        print("Buen progreso.")
    elif porcentaje >= 40:
        print("Puedes mejorar.")
    else:
        print("Necesitas mayor constancia.")

"""
==========================================
FUNCIONES PENDIENTES
==========================================
"""

# Pendiente:
# Obtener eventos desde Google Calendar y agregarlos como tareas en la to-do list.
# Cuando se conecte la API real de Google Calendar, aqui se debe:
#   1. Autenticarse con las credenciales del usuario.
#   2. Obtener la lista de eventos proximos.
#   3. Por cada evento, llamar a agregar_tarea()
#      usando el titulo del evento como nombre y "Google Calendar" como origen.
def sincronizar_google_calendar(tareas):
    print("Pendiente: sincronizacion con Google Calendar.")
    # Simulacion temporal mientras no hay conexion real:
    eventos_simulados = ["Reunion de equipo", "Entrega de proyecto"]
    for evento in eventos_simulados:
        agregar_tarea(tareas, evento, "Google Calendar")

# Pendiente:
# Obtener tareas desde Canvas LMS y agregarlas a la to-do list.
# Cuando se conecte la API real de Canvas, aqui se debe:
#   1. Autenticarse con el token de acceso del usuario.
#   2. Obtener la lista de tareas/asignaciones pendientes.
#   3. Por cada tarea, llamar a agregar_tarea()
#      usando el nombre de la asignacion como nombre y "Canvas" como origen.
def sincronizar_canvas(tareas):
    print("Pendiente: sincronizacion con Canvas LMS.")
    # Simulacion temporal mientras no hay conexion real:
    tareas_simuladas = ["Tarea de Matematicas", "Lectura Capitulo 3"]
    for tarea in tareas_simuladas:
        agregar_tarea(tareas, tarea, "Canvas")

# Pendiente:
# Obtener estadisticas de lectura Kindle.
def obtener_estadisticas_kindle():
    print("Pendiente: obtener estadisticas de Kindle.")

"""
==========================================
MENU PRINCIPAL
==========================================
"""

def menu():
    print("\n===== HABIT TRACKER =====")
    print("1. Agregar habito")
    print("2. Completar habito")
    print("3. Mostrar habitos")
    print("4. Ver estadisticas")
    print("5. Google Calendar")
    print("6. Canvas LMS")
    print("7. Kindle")
    print("8. Agregar tarea a To-Do List")
    print("9. Completar tarea")
    print("10. Mostrar To-Do List")
    print("0. Salir")

    opcion = int(input("Selecciona una opcion: "))
    return opcion

"""
==========================================
FUNCION PRINCIPAL
==========================================
"""

def main():
    habitos = []
    tareas = []
    salir = False

    while not salir:
        opcion = menu()
        match opcion:
            case 1:
                nombre = input("Nombre del habito: ")
                meta = int(input("Meta semanal: "))
                agregar_habito(habitos, nombre, meta)
            case 2:
                mostrar_habitos(habitos)
                indice = int(input("Indice del habito: "))
                completar_habito(habitos, indice)
            case 3:
                mostrar_habitos(habitos)
            case 4:
                mostrar_estadisticas(habitos)
            case 5:
                sincronizar_google_calendar(tareas)
            case 6:
                sincronizar_canvas(tareas)
            case 7:
                obtener_estadisticas_kindle()
            case 8:
                nombre = input("Nombre de la tarea: ")
                agregar_tarea(tareas, nombre, "Manual")
            case 9:
                mostrar_tareas(tareas)
                indice = int(input("Indice de la tarea: "))
                completar_tarea(tareas, indice)
            case 10:
                mostrar_tareas(tareas)
            case 0:
                salir = True
                print("Hasta luego.")
            case _:
                print("Opcion invalida.")

main()
