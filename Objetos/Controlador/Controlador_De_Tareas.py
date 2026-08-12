import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../Modelo"))
from Tareas import Tareas
from datetime import date
from Lista_Tareas import Lista_Tareas

class Controlador_De_Tareas:
    lista=Lista_Tareas()

    def crear_tarea(self, titulo: str, descripcion: str, fecha_limite: date):
        tarea = Tareas(T=titulo, FL=fecha_limite, DT=descripcion)
        self.lista.agregar_tarea(tarea)
        return tarea