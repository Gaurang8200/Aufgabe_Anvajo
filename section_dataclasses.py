from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    hobbies: List[str]
    nickname: Optional[str] = None
