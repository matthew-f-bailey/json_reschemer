from jsonpath_ng import parse

class Reschemer():
    """TestSummary
    """
    def __init__(self, mappings: dict, item_definition: str = "$") -> None:

        # Pull out item definition
        try:
            self._item_definition = mappings.pop("ITEM_DEFINITION")
        except KeyError:
            # Allow for mappings to pass in the item defintion
            self._item_definition = item_definition

        self._mappings = mappings

    def _parse(self, input):

        # Create new dict w/ destination as key and matches as values
        mapped_vals = dict()
        for mapping in self._mappings:
            expr = parse(f"{self._item_definition}.{mapping}")
            values = [match.value for match in expr.find(input)]
            if len(values)==1:
                values = values[0]
            mapped_vals.update({self.mappings[mapping]:values})
        print(mapped_vals)

    def rescheme(self, input):
        self._parse(input)

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
