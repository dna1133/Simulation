from dataclasses import dataclass

from back.domain.creatures.creature import Creature


@dataclass
class Predator(Creature):
    type: str
    is_active: bool
    transparensy: bool
    x_pos: int
    y_pos: int
    health: int
    image: str
    speed: int
    attack_rate: int

    def destroy(self) -> None:
        self.is_active = False

    def move(self): ...

    def attack(self): ...
