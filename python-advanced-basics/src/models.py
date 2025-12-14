from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: int
    name: str
    email: str
    is_active: bool = True
    age: Optional[int] = None
