import json
from typing import Union

class Mapping():
    """Contains values for mapping passed in via client
    """
    mapping_key = "ITEM_DEFINITION"

    def __init__(self, path_mappings:Union[dict, str]) -> None:

        #! Raise Exception on type
        if not isinstance((dict, str)):
            raise TypeError(f"Param 'mappings' must be of either dict or str; Got {type(path_mappings)}")

        #/ Convert and grab Item Definition Selector
        path_mappings = json.loads(path_mappings) if isinstance(str) else path_mappings
        self._item_definition = path_mappings.get(Mapping.mapping_key)

        #! Raise Exception if no item definition
        if not self._item_definition:
            raise MissingDefinitionError(f"No key found in mappings with name {Mapping.mapping_key}")
