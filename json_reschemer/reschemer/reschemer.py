from jsonpath_ng import parse

class Reschemer():
    """TestSummary
    """
    def __init__(self, mappings: dict, item_definition: str = "$") -> None:
        """Initalize Res

        :param mappings: [description]
        :type mappings: dict
        :param item_definition: [description], defaults to "$"
        :type item_definition: str, optional
        """
        # Pull out item definition
        try:
            self._item_definition = mappings.pop("ITEM_DEFINITION")
        except KeyError:
            # Allow for mappings to pass in the item defintion
            self._item_definition = item_definition

        self._mappings = mappings

    def _parse_mapping_values(self, input) -> dict:
        """Takes some collection input repr of json, finds the jsonpath
        values within the input, and resassigns them to a new dict
        containing the values new reschemed location

        :param input: a collection represting json
        :type input: dict, list
        :return: new dictionary with keys of jsonpath pointing to new
        reschemed location and their corresponding values
        :rtype: dict
        """

        # Create new dict w/ destination as key and matches as values
        mapped_vals = dict()
        for mapping in self._mappings:
            # Root Item Def plus mapping
            full_path = "{}.{}".format(self._item_definition, mapping)
            # Parse out current mapping
            expr = parse(full_path)
            # pull out all values for mapping
            values = [match.value for match in expr.find(input)]
            # If only 1 matched, make it a string
            if len(values)==1:
                values = values[0]
            # Add to new dict with key as the mapping value
            mapped_vals.update({self._mappings[mapping]:values})

        return mapped_vals

    def rescheme(self, input):
        """method to call steps needed for rescheming the input

        :param input: a collection represting json
        :type input: dict, list
        """
        remapped = self._parse_mapping_values(input)

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
