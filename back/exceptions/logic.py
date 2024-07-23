from dataclasses import dataclass

from back.exceptions.base import ApplicationException
from back.settings import APPLICATION_EXCEPTION_MESSAGE


@dataclass
class LogicException(ApplicationException):
    @property
    def message(self):
        return APPLICATION_EXCEPTION_MESSAGE
