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

    def __str__(self):
        return f"{self.nombre} - {self.descripcion} (Vence: {self.fecha_limite}"
        