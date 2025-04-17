"""Módulo principal para la gestión de la aplicación"""

"""App para la gestión de tareas, módulo intectivo para la gestión de tareas
    Invoca tanto a Tareas y MangerTareas para gestionar la creación de objetos tipo Tarea"""

from datetime import datetime
from models.tareas import Tareas
from models.enviar_tarea import ManagerTareas

manager = ManagerTareas()

while True:
    print("\n--Bienvenido--")
    print("Por favor elegir una opción")
    print("1 - Agregar tarea\n2 - Para guardar la tarea\n0 - Para salir")
    opcion = input("\nPor favor selecciones una opción: ").strip()

    if not opcion in ["0", "1", "2"]:
        print(f"{opcion} no es una opción correcta")

    elif opcion == "1":
        nombre = input("Agregar nombre de tarea: ").lower().strip()
        descripcion = input("Agregar descripción de tarea: ")
        dias_ans = int(input("Agregar días de ANS: ").strip())
        ahora = datetime.now()
        tarea  = Tareas(nombre, descripcion, ahora, dias_ans)
        manager.nueva_tarea(tarea)
        print("Tarea agregada.")

    elif opcion == "2":
        manager.guardar_tarea(tarea)

    else:
        print("Gracias por visitarnos")
        break   