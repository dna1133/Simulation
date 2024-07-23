from dataclasses import dataclass, field
from functools import lru_cache

from back.map.cell.cell import Cell
from back.map.map.base import BaseMap
from back.settings import ENTITIES


@dataclass
class Map(BaseMap):
    height: int
    width: int
    element: Cell
    elements: list[Cell] = field(
        default_factory=list[Cell],
        kw_only=True,
    )

    def items(self) -> list:
        return [cell.inside_object for cell in self.elements]

    @lru_cache(maxsize=1)
    def map_init(self, entity_dict: dict = ENTITIES) -> None: ...
