from datetime import datetime
import os

ruta_script = os.path.dirname(__file__)
ruta_archivo = os.path.join(ruta_script, "d:\\Documentos\\Diego\\programas\\todolist\\src\\data\\archivo.txt")


class ManagerTareas():
    def __init__(self, tareas):
        self.tareas = []
    
    def nueva_tarea(self, tareas):
        self.tareas.append(tareas)


    def guardar_tarea(self):
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            for tarea in self.tareas:
                    archivo.writelines(self.tareas)
                    print("Copia guardada")
        

