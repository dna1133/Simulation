from dataclasses import dataclass

from back.entities.base import BaseEntity
from back.settings import ATTACK_RATE, HEALTH, SPEED
from back.values.health import HealthValue


@dataclass
class Rock(BaseEntity):

    speed: int
    attack_rate: int
    health: HealthValue

    def __post_init__(self) -> None:
        self.health = HealthValue(value=HEALTH.get(self.__class__.__name__))
        self.speed = SPEED.get(self.__class__.__name__)
        self.attack_rate = ATTACK_RATE.get(self.__class__.__name__)

    def make_move(self) -> None: ...

    def attack(self) -> None: ...

    def is_static(self) -> bool: ...

    @property
    def health(self) -> int:
        return self.health.as_generic_type()

    @health.setter
    def health(self, damage: int) -> None:
        self.health.value = self.health.as_generic_type() - damage


@dataclass
class Tree(BaseEntity):
    def __init__(self) -> None:
        super.__init__()


@dataclass
class Grass(BaseEntity):
    def __init__(self) -> None:
        super.__init__()


@dataclass
class Creature(BaseEntity):
    def __init__(self) -> None:
        super.__init__()


@dataclass
class Predator(BaseEntity):
    def __init__(self) -> None:
        super.__init__()


@dataclass
class Herbivore(BaseEntity):
    def __init__(self) -> None:
        super.__init__()
