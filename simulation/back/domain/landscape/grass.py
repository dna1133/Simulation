from dataclasses import dataclass

from simulation.back.domain.landscape.entity import Entity


@dataclass
class Grass(Entity):
    type: str
    is_active: bool
    transparensy: bool
    x_pos: int
    y_pos: int
    health: int
    image: str

    def destroy(self) -> None:
        self.is_active = False
