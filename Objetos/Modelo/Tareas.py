from __future__ import annotations
from datetime import date

class Tareas:
    FC: date #fecha de creacion
    FL: date #fecha limite
    DP: int = 0 #Dias despues del plazo
    T: str = "" #Tarea
    DT: str = "" #Descripcion de la tarea
    E: str = "pendiente" #Estado
    SUBT: list[str] = [] #Subtareas

