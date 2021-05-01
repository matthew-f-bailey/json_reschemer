from json_reschemer.loading.loading import LoadStrategy
from json_reschemer.mapping.mapping import Mapping


class Reschemer():
    """[summary]
    """
    def __init__(self, strategy: LoadStrategy, mappings: Mapping) -> None:
        self._load_strategy = strategy
        self._mappings = mappings

    def rescheme(self) -> None:
        """
        The template method defines the skeleton of an algorithm.
        """
        pass

    @property
    def mappings(self):
        return self._mappings

    @mappings.setter
    def mappings(self, mappings: Mapping):

        # ! Throw if not a Mapping object
        if not isinstance(mappings, Mapping):
            raise TypeError(
                "Mappings attribute must be of type {}; \
                Got {}".format(type(mappings), mappings)
            )

        self._mappings = mappings

    @property
    def load_strategy(self):
        return self._load_strategy

    @load_strategy.setter
    def load_strategy(self, strategy: LoadStrategy):

        # ! Throw if not a LoadStrategy object
        if not isinstance(strategy, LoadStrategy):
            raise TypeError(
                "Mappings attribute must be of type {}; \
                Got {}".format(type(strategy), strategy)
            )

        self._load_strategy = strategy
