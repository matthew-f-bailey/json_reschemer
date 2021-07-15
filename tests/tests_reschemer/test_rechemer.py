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
            "$"
        )


class TestPathExpressions(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_simple_parse_mapping_values(self):

        simple_mappings = {
            "foo": "thisIsBar"
        }

        expected = {
            "thisIsBar": "bar"
        }

        reschemer = Reschemer(mappings=simple_mappings)
        self.assertEqual(
            reschemer._parse_mapping_values(SIMPLE_JSON),
            expected
        )

    def test_complex_parse_mapping_values(self):

        mappings = {
            "ITEM_DEFINITION": "[*]",
            "id": "identifiers",
            "batters.batter[*].id": "batter_ids"
        }

        expected = {
            "identifiers": ['0001', '0002', '0003'],
            "batter_ids": [
                '1001',
                '1002',
                '1003',
                '1004',
                '1001',
                '1001',
                '1002',
            ]
        }

        reschemer = Reschemer(mappings=mappings)
        self.assertEqual(
            reschemer._parse_mapping_values(COMPLEX_LIST_JSON),
            expected
        )