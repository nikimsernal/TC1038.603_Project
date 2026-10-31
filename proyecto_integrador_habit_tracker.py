
"""
==========================================
PROYECTO INTEGRADOR: TC1038.603
Habit Tracker y Gestor de Productividad
==========================================
Kimberly Nikita Serna Lerma
GitHub Repo: https://github.com/nikimsernal/TC1038.603
==========================================
"""

import csv

TASKS_FILE = "tasks.csv"
HABITS_FILE = "habits.csv"
DAYS = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]

# ==========================================
# FUNCIONES DE TO-DO LIST
# ==========================================
# Carga las tareas almacenadas en el archivo CSV.
def load_tasks():
    try:
        with open(TASKS_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            task_list = [row[0] for row in reader if row]
    except FileNotFoundError:
        task_list = []
    return task_list

# Guarda las tareas actuales en el archivo CSV.
def save_tasks(task_list):
    with open(TASKS_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([[task] for task in task_list])

# Agrega una nueva tarea si el nombre no está vacío.
def add_task(task_list, task):
    if task.strip() != "":
        task_list.append(task.strip())
        save_tasks(task_list)
        return True
    return False

# Elimina todas las tareas registradas.
def clear_tasks(task_list):
    task_list.clear()
    save_tasks(task_list)

# Muestra todas las tareas registradas.
def display_tasks(task_list):
    if len(task_list) == 0:
        print("No hay nada pendiente aún.")
    else:
        print("\n======= PENDIENTES =======")
        for i, task in enumerate(task_list):
            print(f"{i + 1}. {task}")

# ==========================================
# FUNCIONES DE HABIT TRACKER
# ==========================================
#Carga los hábitos y su matriz semanal desde CSV.
#ada hábito tiene una fila con siete columnas adicionales,
#una por cada día de la semana.
def load_habits():
    habit_list = []
    weekly_history = []
    try:
        with open(HABITS_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 10:
                    habit = {"name": row[0], "goal": int(row[1]), "completed": int(row[2])}
                    history = []
                    for value in row[3:10]:
                        history.append(int(value))
                # Recupera hábitos del formato anterior.
                elif len(row) == 3:
                    habit = {"name": row[0], "goal": int(row[1]), "completed": int(row[2])}
                    history = [0, 0, 0, 0, 0, 0, 0]
                else:
                    continue
                habit_list.append(habit)
                weekly_history.append(history)
    except FileNotFoundError:
        pass
    return habit_list, weekly_history


# Guarda los hábitos y su matriz semanal en CSV.
def save_habits(habit_list, weekly_history):
    with open(HABITS_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for i in range(len(habit_list)):
            writer.writerow([
                habit_list[i]["name"],
                habit_list[i]["goal"],
                habit_list[i]["completed"]
            ] + weekly_history[i])


# Registra un nuevo hábito con una meta semanal.
# También agrega una fila de siete ceros a la matriz.
def add_habit(habit_list, weekly_history, name, goal):
    if name.strip() != "" and goal > 0:
        habit = {"name": name.strip(), "goal": goal, "completed": 0}
        habit_list.append(habit)
        # Cada columna es un día de la semana.
        weekly_history.append([0, 0, 0, 0, 0, 0, 0])
        save_habits(habit_list, weekly_history)
        return True
    return False


# Registra el cumplimiento de un hábito en un día específico.
# Evita registrar dos veces el mismo hábito durante el mismo día.
def complete_habit(habit_list, weekly_history, index, day):
    if index >= 0 and index < len(habit_list):
        if day >= 0 and day < 7:
            if weekly_history[index][day] == 0:
                weekly_history[index][day] = 1
                habit_list[index]["completed"] += 1
                save_habits(habit_list, weekly_history)
                print("¡Sigue así! Progreso actualizado.")
            else:
                print("Este hábito ya fue completado ese día.")
        else:
            print("Día inválido.")
    else:
        print("Número de hábito inválido.")


# Muestra los hábitos y su progreso semanal.
def display_habits(habit_list, weekly_history):
    if len(habit_list) == 0:
        print("Sin hábitos aún.")
    else:
        print("\n===== HABIT TRACKER =====")
        for i, habit in enumerate(habit_list):
            weekly_completed = sum(weekly_history[i])
            percentage = min((weekly_completed / habit["goal"]) * 100, 100)
            print(f"\n{i + 1}. {habit['name']}")
            print(f" Meta semanal: {habit['goal']}")
            print(f" Completado esta semana: {weekly_completed}")
            print(f" Total histórico: {habit['completed']}")
            print(f" Progreso semanal: {percentage:.2f}%")


# Elimina todos los hábitos y sus registros.
def clear_habits(habit_list, weekly_history):
    habit_list.clear()
    weekly_history.clear()
    save_habits(habit_list, weekly_history)


# ==========================================
# MATRIZ SEMANAL
# ==========================================
def display_weekly_matrix(habit_list, weekly_history):
    if len(habit_list) == 0:
        print("No hay hábitos registrados.")

    else:
        print("\n========== HISTORIAL SEMANAL ==========")
        print(f"{'Hábito':<18}", end="")
        for day in DAYS:
            print(f"{day:>6}", end="")
        print()
        
        for i in range(len(habit_list)):
            print(f"{habit_list[i]['name']:<18}", end="")
            for j in range(7):
                if weekly_history[i][j] == 1:
                    symbol = "X"
                else:
                    symbol = "-"
                print(f"{symbol:>6}", end="")
            print()
        print("\nX = Completado | - = Pendiente")


# Calcula el porcentaje global de cumplimiento semanal.
def calculate_progress(habit_list, weekly_history):
    total_goal = 0
    total_completed = 0
    for i in range(len(habit_list)):
        total_goal += habit_list[i]["goal"]
        total_completed += min(sum(weekly_history[i]), habit_list[i]["goal"])
    if total_goal == 0:
        return 0
    percentage = (total_completed / total_goal) * 100
    return percentage


# Cuenta cuántos hábitos se completaron en un día específico.
def calculate_daily_progress(weekly_history, day):
    total = 0
    if day >= 0 and day < 7:
        for i in range(len(weekly_history)):
            if weekly_history[i][day] == 1:
                total += 1
    return total


# Reinicia la matriz semanal sin eliminar el historial acumulado de cada hábito.
def reset_weekly_matrix(habit_list, weekly_history):
    for i in range(len(weekly_history)):
        for j in range(7):
            weekly_history[i][j] = 0
    save_habits(habit_list, weekly_history)
    print("¡Nueva semana! El seguimiento se ha reiniciado.")


# ==========================================
# FUNCIONES DE ESTADÍSTICAS
# ==========================================
def display_statistics(habit_list, weekly_history):
    percentage = calculate_progress(habit_list, weekly_history)
    print("\n===== ESTADÍSTICAS DE PRODUCTIVIDAD =====")
    print(f"Progreso general de hábitos: {percentage:.2f}%")

    if len(habit_list) > 0:
        total_completed = 0
        for habit in habit_list:
            total_completed += habit["completed"]
            
        print(f"Total histórico de hábitos completados: {total_completed}")
        print("\n===== CUMPLIMIENTO POR DÍA =====")
        
        for i in range(7):
            daily_total = calculate_daily_progress(weekly_history, i)
            print(f"{DAYS[i]}: {daily_total} hábitos completados")

    if percentage >= 100:
        print("\n¡Todas tus metas están completas! ¡Felicidades!")
    elif percentage >= 70:
        print("\n¡Vas muy bien!")
    elif percentage >= 40:
        print("\n¡Sigue así!")
    else:
        print("\nEl mejor momento para empezar es ahora.")


# ==========================================
# MENU PRINCIPAL
# ==========================================
def main_menu():
    print("\n================================")
    print("       SHELL CHECK TRACKER")
    print("================================")

    print("\n===== TO-DO LIST =====")
    print("1. Mostrar Pendientes")
    print("2. Agregar Pendiente")
    print("3. Borrar Todo")

    print("\n===== HABIT TRACKER =====")
    print("4. Mostrar Hábitos")
    print("5. Agregar Hábito")
    print("6. Completar Hábito")
    print("7. Borrar Hábitos")
    print("8. Estadísticas de Productividad")

    print("\n===== SEGUIMIENTO SEMANAL =====")
    print("9. Mostrar Matriz Semanal")
    print("10. Reiniciar Semana")

    print("\n0. Salir")
    option = input("\nSelecciona una opción: ")
    return option


# ==========================================
# FUNCIÓN PRINCIPAL
# ==========================================
def main():
    task_list = load_tasks()
    habit_list, weekly_history = load_habits()

    while True:
        option = main_menu()
        match option:
            # TO-DO LIST
            case "1":
                display_tasks(task_list)

            case "2":
                task = input("Agregar Pendiente: ")
                if add_task(task_list, task):
                    print("¡Agregado con éxito!")
                else:
                    print("El nombre no puede estar vacío.")

            case "3":
                clear_tasks(task_list)
                print("¡Qué gran nuevo comienzo!")

            # HABIT TRACKER
            case "4":
                display_habits(habit_list, weekly_history)

            case "5":
                name = input("Agregar Nuevo Hábito: ")
                goal_input = input("Meta semanal: ")
                if goal_input.isdigit():
                    goal = int(goal_input)
                    if add_habit(habit_list, weekly_history, name, goal ):
                        print("¡Hábito agregado con éxito!")
                    else:
                        print("Información inválida.")
                else:
                    print("Ingresa un número válido.")

            case "6":
                display_habits(habit_list, weekly_history)
                if len(habit_list) > 0:
                    index_input = input("Índice del hábito: ")
                    if index_input.isdigit():
                        index = int(index_input) - 1
                        print("\nSelecciona el día:")
                        for i in range(7):
                            print(f"{i + 1}. {DAYS[i]}")
                        day_input = input("Día: ")
                        if day_input.isdigit():
                            day = int(day_input) - 1
                            complete_habit(habit_list, weekly_history, index, day)
                        else:
                            print("Ingresa un día válido.")
                    else:
                        print("Ingresa un número válido.")

            case "7":
                clear_habits(habit_list, weekly_history)
                print("¡Qué gran nuevo comienzo!")

            case "8":
                display_statistics(habit_list, weekly_history)

            # MATRIZ SEMANAL
            case "9":
                display_weekly_matrix(habit_list, weekly_history)

            case "10":
                confirm = input("¿Deseas reiniciar el seguimiento semanal? (s/n): ")

                if confirm.lower() == "s":

                    reset_weekly_matrix(habit_list, weekly_history)
                else:
                    print("Operación cancelada.")

            case "0":
                print("Gracias por usar Shell Check.")
                break

            case _:
                print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
