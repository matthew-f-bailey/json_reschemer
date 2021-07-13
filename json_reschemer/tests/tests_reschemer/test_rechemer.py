import unittest

from json_reschemer.reschemer.reschemer import Reschemer
# from json_reschemer.reschemer.r_exceptions import MissingItemDefinitionError


class TestReschemer(unittest.TestCase):

    def setUp(self) -> None:

        self.simple_mappings = {
            "ITEM_DEFINITION": "foo",
            "bar": "baz"
        }

        self.nodef_mappings = {"bar": "baz"}

    def test_pop_out_definition(self):

        reschemer = Reschemer(mappings=self.simple_mappings)

        self.assertEqual(
            reschemer.item_definition,
            "foo"
        )

    def test_remaining_mappings(self):

        reschemer = Reschemer(mappings=self.simple_mappings)

        self.assertEqual(
            reschemer.mappings,
            {"bar": "baz"}
        )

    def test_optional_defintion(self):

        reschemer = Reschemer(mappings=self.nodef_mappings)

        self.assertEqual(
            reschemer.item_definition,
            "*"
        )
