from dataclasses import dataclass

from simulation.back.domain.landscape.entity import Entity


@dataclass
class Rock(Entity):

    def destroy(self): ...
