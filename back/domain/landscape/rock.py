from dataclasses import dataclass

from back.domain.landscape.entity import Entity


@dataclass
class Rock(Entity):
    type: str
    is_active: bool
    transparensy: bool
    x_pos: int
    y_pos: int
    health: int
    image: str

    def destroy(self): ...
