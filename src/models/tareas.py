"""Clase Tarea:

    Atributos:
        nombre (str) : nombre único por tarea.
        descripcion (str) : detalle de la tarea
        fecha_creacion (datetime) : se agrega de manera automatica
        dias_ans (int) : Cantidad de días dispobibles para la tarea
        fecha de limite (datetime) : se agrega de manera automatica sumando los días ans para la tarea"""

from datetime import timedelta

class Tareas:
    def __init__(self, nombre, descripcion, fecha_creacion, dias_ans):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.dias_ans = dias_ans
        self.fecha_limite = self.fecha_creacion + timedelta(days=self.dias_ans)

    """def ver_tarea(self):
        return f"{self.nombre} - {self.descripcion} - {self.fecha_creacion} - {self.fecha_limite} - {self.completada}"


    def tarea_vencida(self):
        if self.fecha_limite < datetime.now():
            return f"La tarea {self.nombre} esta vencida"
        else:
            return"""
        