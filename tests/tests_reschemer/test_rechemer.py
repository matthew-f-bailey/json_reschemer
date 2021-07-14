import unittest

from json_reschemer.reschemer.reschemer import Reschemer
from .complex_json import COMPLEX_LIST_JSON, SIMPLE_JSON
# from json_reschemer.reschemer.r_exceptions import MissingItemDefinitionError


class TestMappings(unittest.TestCase):

    def setUp(self) -> None:

        self.simple_mappings = {
            "ITEM_DEFINITION": "foo",
            "bar": "baz"
        }

        self.nodef_mappings = {"bar": "baz"}

    def test_pop_out_definition(self):
        """Test to verify item definition gets pulled out"""

        reschemer = Reschemer(mappings=self.simple_mappings)

        self.assertEqual(
            reschemer.item_definition,
            "foo"
        )

    def test_remaining_mappings(self):
        """Test to verify remaining mappings are valid"""

        reschemer = Reschemer(mappings=self.simple_mappings)

        self.assertEqual(
            reschemer.mappings,
            {"bar": "baz"}
        )

    def test_optional_defintion(self):
        """Test that item definition is optional"""

        reschemer = Reschemer(mappings=self.nodef_mappings)

        self.assertEqual(
            reschemer.item_definition,
            "*"
        )


class TestPathExpressions(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_pulling_ids(self):

        mappings = {
            "ITEM_DEFINITION": "[*]",
            "id": "[*].identifier",
            "name": "[*].name"
        }

        simple_mappings = {
            "foo":"thisIsBar"
        }

        reschemer = Reschemer(mappings=simple_mappings)
        print(reschemer.rescheme(SIMPLE_JSON))