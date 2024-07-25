from typing import Callable, Hashable
from simulation.back.domain.creatures.creature import Creature
from simulation.back.domain.creatures.herbivore import Herbivore
from simulation.back.domain.creatures.predator import Predator
from simulation.back.domain.landscape.entity import Entity
from simulation.back.domain.landscape.grass import Grass
from simulation.back.domain.landscape.rock import Rock
from simulation.back.domain.landscape.tree import Tree
from simulation.back.exceptions.service import ServiceException
from simulation.back.services.domain.direction_builder import DirectionBuilder
from simulation.back.settings import (
    ATTACK_RATE,
    CREATURES,
    HEALTH,
    IMAGE,
    LANDSCAPE,
    SPEED,
    TARGET,
    TRANSPARENSY,
)


class EntityBuilder(Creature, Entity):
    @staticmethod
    def get(class_name: Hashable, position: tuple[int, int]) -> Entity:
        classes: dict[Hashable, Callable[..., Entity]] = {
            "Rock": Rock,
            "Grass": Grass,
            "Tree": Tree,
            "Herbivore": Herbivore,
            "Predator": Predator,
        }

        class_ = classes.get(class_name, None)
        if class_ is not None:
            x_pos, y_pos = position
            if class_name in LANDSCAPE:
                return class_(
                    type=class_name,
                    is_active=True,
                    transparensy=TRANSPARENSY[class_name],
                    x_pos=x_pos,
                    y_pos=y_pos,
                    health=HEALTH[class_name],
                    image=IMAGE[class_name],
                )
            elif class_name in CREATURES:
                return class_(
                    type=class_name,
                    is_active=True,
                    transparensy=TRANSPARENSY[class_name],
                    x_pos=x_pos,
                    y_pos=y_pos,
                    health=HEALTH[class_name],
                    image=IMAGE[class_name],
                    speed=SPEED[class_name],
                    attack_rate=ATTACK_RATE[class_name],
                    target=TARGET[class_name],
                    direction=DirectionBuilder.create_direction(),
                )

        raise ServiceException


# def main():
#     test_class = EntityBuilder.get("Predator", (1, 1))
#     print(test_class.type)
#     print(test_class.x_pos)


# if __name__ == "__main__":
#     main()
