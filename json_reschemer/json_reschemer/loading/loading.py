from typing import Any
from abc import ABC, abstractmethod


class LoadStrategy(ABC):
    """Abstract Load Strategy Class

    :param ABC: Abstract Base Class
    :type ABC: ABC
    """
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def load(self, data: Any) -> None:
        pass


class CSVLoadStrategy(LoadStrategy):
    """Strategy class used to load csv data


    :param LoadStrategy: Extends LoadStrategy
    :type LoadStrategy: LoadStrategy
    """
    def __init__(self) -> None:
        super().__init__()
