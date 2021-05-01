import argparse
from unittest.mock import MagicMock, Mock, patch
import unittest

from json_reschemer.cli import parse_my_args


class Test_CLI_ArgInstance(unittest.TestCase):
    """Test for argparse"""
    with patch('argparse._sys.argv', ['python', '--foo=test', '--bar=pest']):
        args = parse_my_args()
        assert(args.foo=='test')
        assert(args.bar=='pest')

if __name__ == '__main__':
    unittest.main()