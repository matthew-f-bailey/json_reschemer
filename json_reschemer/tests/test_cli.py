from unittest.mock import patch
import unittest
from json_reschemer.cli import parse_my_args


class Test_CLI_ArgInstance(unittest.TestCase):
    """Test for argparse"""

    def test_CLI(self):
        params = ['python', '--foo=test', '--bar=pest']
        with patch('argparse._sys.argv', params):
            args = parse_my_args()
            self.assertEqual(args.foo, 'test')
            self.assertEqual(args.bar, 'pest')


if __name__ == '__main__':
    unittest.main()
