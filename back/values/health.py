from dataclasses import dataclass

from back.exceptions.logic import LogicException
from back.exceptions.settings import SettingsException
from back.values.base import BaseValue


@dataclass
class HealthValue(BaseValue):
    value: int

    def validate(self) -> None:
        if not type(self.value) == int:
            raise SettingsException
        if self.value < 0:
            raise LogicException

    def as_generic_type(self) -> int:
        return int(self.value)
