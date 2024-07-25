from dataclasses import dataclass

from simulation.back.domain.landscape.entity import Entity


@dataclass
class Tree(Entity):

    def destroy(self): ...
