from abc import ABC, abstractmethod
from dataclasses import dataclass

from back.domain.landscape.entity import Entity


@dataclass
class Creature(Entity, ABC):
    type: str
    is_active: bool
    transparensy: bool
    x_pos: int
    y_pos: int
    health: int
    image: str
    speed: int
    attack_rate: int

    @abstractmethod
    def destroy(self): ...

    @abstractmethod
    def move(self): ...

    @abstractmethod
    def attack(self): ...
