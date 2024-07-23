from abc import ABC, abstractmethod
from dataclasses import dataclass

from back.map.cell.cell import Cell


@dataclass
class BaseMap(ABC):
    height: int
    width: int
    element: Cell
    elements: list[Cell]

    @abstractmethod
    def items(self) -> list: ...

    @abstractmethod
    def map_init(self) -> None: ...
