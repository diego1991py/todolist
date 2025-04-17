"""Clase ManagerTareas():
:

    Atributos:
        Lista de objetos Tarea
        
        metodos:
            cargar_tareas : Carga datos de archivo.txt y los almacena como objetos
            nueva_tarea : Array
            guardar_tarea: Recibe el array guarda en archivo.txt
: """


from datetime import datetime
import os

ruta_script = os.path.dirname(__file__)
ruta_archivo = os.path.join(ruta_script, "..\\data", "archivo.txt") 
os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)

class ManagerTareas():
    def __init__(self):
        self.tareas = []

    def cargar_tareas(self):
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                return [linea.strip() for linea in archivo.readlines()]
        return []
    
    def nueva_tarea(self, tarea):
        self.tareas.append(tarea)
        return self.tareas


    def guardar_tarea(self, tarea):
            with open(ruta_archivo, "a", encoding="utf-8") as archivo: 
                for tarea in self.tareas:
                        linea = f"{tarea.nombre}|{tarea.descripcion}|{tarea.fecha_creacion}|{tarea.fecha_limite}\n"
                        archivo.write(f"{str(linea)}\n")
                
                print("Tareas guardadas")
        

        

