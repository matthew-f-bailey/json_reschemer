import json
from typing import Union
from .m_exceptions import MissingDefinitionError


class Mapping():
    """[summary]

    :raises TypeError: [description]
    :raises MissingDefinitionError: [description]
    """
    mapping_key = "ITEM_DEFINITION"

    def __init__(self, path_mappings: Union[dict, str]) -> None:

        # ! Raise Exception on type
        if not isinstance((dict, str)):
            raise TypeError(
                "Param 'mappings' must be of either dict or str; \
                Got {}".format(type(path_mappings))
            )

        # / Convert and grab Item Definition Selector
        if isinstance(path_mappings, str):
            path_mappings = json.loads(path_mappings)

        self._item_definition = path_mappings.get(Mapping.mapping_key)

        # ! Raise Exception if no item definition
        if not self._item_definition:
            raise MissingDefinitionError(
                "No key found in mappings with name {} \
                ".format(Mapping.mapping_key)
            )
