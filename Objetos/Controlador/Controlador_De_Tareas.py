from "../Modelo/Tareas" import Tareas
from "Controlador_De_ID" import Controlador_ID
class Controlador_De_Tareas:
     def crear_tarea(self, fecha_limite: date, tarea: str, descripcion: str, subtareas: list[str]) -> Tareas:
          ID=Controlador_ID().get_id()