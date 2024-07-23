from dataclasses import dataclass

from back.map.cell.base import BaseCell


@dataclass
class Cell(BaseCell):
    axis_x: int
    axis_y: int
    empty: bool
    inside_object: str | None

    def is_empty(self) -> bool:
        return self.empty
