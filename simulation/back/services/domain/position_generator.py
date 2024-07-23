from random import randint
from simulation.back.settings import HEIGHT, WIDTH


class PositionGenerator:
    @staticmethod
    def generate(
        exept_list: list[tuple[int, int]], width: int = WIDTH, height: int = HEIGHT
    ) -> tuple[int, int]:
        position = (randint(0, width), randint(0, height))
        if exept_list and (position in exept_list):
            PositionGenerator.generate(exept_list)
        else:
            return position
