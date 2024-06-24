from dataclasses import dataclass

from back.entities.base import BaseEntity
from back.settings import SPEED
from back.values.health import HealthValue


@dataclass
class Rock(BaseEntity):
    axis_x: int
    axis_y: int
    static: bool = True
    health: HealthValue
    target_in: str | None = None
    target_out: str | None = None
    speed: int = SPEED[__dict__.__class__.__name__]
    attack_rate: int

    def make_move(self) -> None: ...

    def attack(self) -> None: ...

    def is_static(self) -> bool: ...


@dataclass
class Tree(BaseEntity):
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
class Grass(BaseEntity):
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
