from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional


class Label(Enum):
    EMPTY = auto()
    FULL = auto()
    UNKOWN = auto()

@dataclass 
class Sample:
    name: str
    volume__m3: float
    label: Optional[Label] = None
    volume__l: int = field(init=False) 
    #initalization of volume__l in __post_init__().

    def __post_init__(self):
        self.volume__l = int(self.volume__m3 * 1e3)

