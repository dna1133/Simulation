from dataclasses import dataclass

from back.entities.base import BaseEntity
from back.values.health import HealthValue


@dataclass
class Creature(BaseEntity):
    axis_x: int
    axis_y: int
    static: bool
    health: HealthValue
    target_in: str | None
    target_out: str | None
    speed: int
    attack_rate: int

    def make_move(self) -> None: ...

    def attack(self) -> None: ...

    def is_static(self) -> bool: ...


@dataclass
class Predator(BaseEntity):
    axis_x: int
    axis_y: int
    static: bool
    health: HealthValue
    target_in: str | None
    target_out: str | None
    speed: int
    attack_rate: int

    def make_move(self) -> None: ...

    def attack(self) -> None: ...

    def is_static(self) -> bool: ...


@dataclass
class Herbivore(BaseEntity):
    axis_x: int
    axis_y: int
    static: bool
    health: HealthValue
    target_in: str | None
    target_out: str | None
    speed: int
    attack_rate: int

    def make_move(self) -> None: ...

    def attack(self) -> None: ...

    def is_static(self) -> bool: ...
