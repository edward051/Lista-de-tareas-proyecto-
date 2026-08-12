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
    FCOMP: date | None = None
    ID: int = field(init=False)

    def __init__(self, T: str, FL: date, DT: str = "", FC: date = field(default_factory=date.today), DP: int = 0, E: str = "pendiente", ID: int = 0, SUBT: int | None = None):
        self.T = T
        self.FL = FL
        self.FC = FC
        self.DP = DP
        self.DT = DT
        self.E = E
        self.ID = ID
        self.SUBT = SUBT


