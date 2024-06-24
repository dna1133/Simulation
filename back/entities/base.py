from abc import ABC, abstractmethod
from dataclasses import dataclass

from back.values.health import HealthValue


@dataclass
class BaseEntity(ABC):
    axis_x: int
    axis_y: int
    static: bool
    health: HealthValue
    target_in: str | None
    target_out: str | None
    speed: int
    attack_rate: int

    @abstractmethod
    def make_move(self) -> None: ...

    @abstractmethod
    def attack(self) -> None: ...

    @abstractmethod
    def is_static(self) -> bool: ...
