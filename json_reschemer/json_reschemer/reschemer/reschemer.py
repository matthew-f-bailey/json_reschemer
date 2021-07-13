

class Reschemer():
    """TestSummary
    """
    def __init__(self, mappings: dict, item_definition: str = "*") -> None:

        # Pull out item definition
        try:
            self._item_definition = mappings.pop("ITEM_DEFINITION")
        except KeyError:
            # Allow for mappings to pass in the item defintion
            self._item_definition = item_definition

        self._mappings = mappings

    # Getters/Setters
    @property
    def item_definition(self):
        return self._item_definition

    @item_definition.setter
    def item_definition(self, value):
        self._item_definition = value

    @property
    def mappings(self):
        return self._mappings

    @mappings.setter
    def mappings(self, value):
        self._mappings = value
