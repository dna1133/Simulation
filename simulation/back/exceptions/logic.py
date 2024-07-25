from dataclasses import dataclass

from simulation.back.exceptions.base import ApplicationException
from simulation.back.settings import APPLICATION_EXCEPTION_MESSAGE


@dataclass(eq=False)
class LogicException(ApplicationException):
    @property
    def message(self):
        return APPLICATION_EXCEPTION_MESSAGE
