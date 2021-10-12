from typing import TypeVar, Generic, Iterable
from abc import ABC, abstractmethod
T = TypeVar('T')


class Dao (Generic[T], ABC):
    @abstractmethod
    def findAll(self) -> Iterable:
        pass

