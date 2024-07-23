from dataclasses import dataclass

from simulation.back.exceptions.base import ApplicationException
from simulation.back.settings import SERVICE_EXCEPTION_MESSAGE


@dataclass
class ServiceException(ApplicationException):
    @property
    def message(self):
        return SERVICE_EXCEPTION_MESSAGE
