from dataclasses import dataclass
from random import choices

from simulation.back.settings import DIR_LIST


@dataclass
class DirectionBuilder:

    @staticmethod
    def create_direction():
        return choices(DIR_LIST, k=1)[0]
