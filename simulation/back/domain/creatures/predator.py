from dataclasses import dataclass

from simulation.back.domain.creatures.creature import Creature


@dataclass
class Predator(Creature):

    def destroy(self) -> None:
        self.is_active = False

    def move(self): ...

    def attack(self): ...
