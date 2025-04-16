from datetime import datetime
from models.tareas import Tareas
from models.enviar_tarea import ManagerTareas

"""Módulo principal para la gestión de la aplicación"""

opcion = ""

while True:
    print("\n--Bienvenido--")
    print("Por favor elegir una opción")
    print("1 - Agregar tarea\n2 - Para ver la lista de Tareas\n0 - Para salir")
    opcion = input("\nPor favor selecciones una opción: ").strip()

    if not opcion in ["0", "1", "2"]:
        print(f"{opcion} no es una opción correcta")

    elif opcion == "1":
        nombre_tarea = input("Agregar nombre de tarea: ").lower().strip()
        descripcion_tarea = input("Agregar descripción de tarea: ")
        dias_ans_tarea = int(input("Agregar días de ANS: ").strip())
        nueva_tarea = Tareas(nombre_tarea, descripcion_tarea, datetime.now(), dias_ans_tarea)
        lista = ManagerTareas(nueva_tarea)

    elif opcion == "2":
        ver_tarea = ManagerTareas.guardar_tarea(lista)