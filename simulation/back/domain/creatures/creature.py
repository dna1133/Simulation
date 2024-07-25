from abc import ABC, abstractmethod
from dataclasses import dataclass

from simulation.back.domain.landscape.entity import Entity


@dataclass
class Creature(Entity, ABC):
    speed: int
    attack_rate: int
    target: str
    direction: str

    @abstractmethod
    def destroy(self): ...

    @abstractmethod
    def move(self): ...

    @abstractmethod
    def attack(self): ...
