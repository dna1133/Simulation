from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Entity(ABC):
    type: str
    is_active: bool
    transparensy: bool
    x_pos: int
    y_pos: int
    health: int
    image: str

    @abstractmethod
    def destroy(self): ...
