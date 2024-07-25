from dataclasses import dataclass

from simulation.back.domain.landscape.entity import Entity


@dataclass
class Grass(Entity):

    def destroy(self) -> None:
        self.is_active = False
