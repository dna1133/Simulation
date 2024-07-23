from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseCell(ABC):
    axis_x: int
    axis_y: int
    empty: bool
    inside_object: str | None

    @abstractmethod
    def is_empty(self) -> bool: ...
