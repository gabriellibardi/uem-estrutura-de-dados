from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    proximo: No | None
