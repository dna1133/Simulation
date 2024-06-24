from dataclasses import dataclass

from back.exceptions.base import ApplicationException
from back.settings import SETTINGS_EXCEPTION


@dataclass
class SettingsException(ApplicationException):
    @property
    def message(self):
        return SETTINGS_EXCEPTION
