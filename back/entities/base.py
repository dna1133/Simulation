from abc import ABC, abstractmethod
from dataclasses import dataclass

from back.values.health import HealthValue


@dataclass
class BaseEntity(ABC):

    speed: int
    attack_rate: int
    health: HealthValue

    @abstractmethod
    def make_move(self) -> None: ...

    @abstractmethod
    def attack(self) -> None: ...

    @abstractmethod
    def is_static(self) -> bool: ...

    @property
    @abstractmethod
    def health(self) -> int:
        return self.health.as_generic_type()

    @health.setter
    @abstractmethod
    def health(self, damage: int) -> None:
        self.health.value = self.health.as_generic_type() - damage
