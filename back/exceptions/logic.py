from dataclasses import dataclass

from back.exceptions.base import ApplicationException
from back.settings import APPLICATION_EXCEPTION


@dataclass
class LogicException(ApplicationException):
    @property
    def message(self):
        return APPLICATION_EXCEPTION
