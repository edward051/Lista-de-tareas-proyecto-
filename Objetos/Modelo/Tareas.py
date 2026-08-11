from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date

@dataclass
class Tareas:
    T: str
    FL: date
    FC: date = field(default_factory=date.today)
    DP: int = 0
    DT: str = ""
    E: str = "pendiente"
    SUBT: int | None = None
    ID: int = field(init=False)


