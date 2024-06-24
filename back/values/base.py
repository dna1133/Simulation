from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, TypeVar, Generic


VT = TypeVar("VT", bound=Any)


@dataclass
class BaseValue(ABC, Generic[VT]):
    value: VT

    def __post_init__(self) -> None:
        self.validate()

    @abstractmethod
    def validate(self) -> None: ...

    @abstractmethod
    def as_generic_type() -> VT: ...
