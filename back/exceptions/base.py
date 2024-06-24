from dataclasses import dataclass

from back.settings import APPLICATION_EXCEPTION


@dataclass
class ApplicationException(Exception):
    @property
    def message(self):
        return APPLICATION_EXCEPTION
