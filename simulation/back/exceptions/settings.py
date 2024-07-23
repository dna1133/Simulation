from dataclasses import dataclass

from simulation.back.exceptions.base import ApplicationException
from simulation.back.settings import SETTINGS_EXCEPTION_MESSAGE


@dataclass
class SettingsException(ApplicationException):
    @property
    def message(self):
        return SETTINGS_EXCEPTION_MESSAGE
