from unittest import TestCase
from unittest.mock import mock_open, patch
from json_reschemer.loading.strategies import CSVLoadStrategy

class Test_CSV(TestCase):
    """Test for argparse"""

    DATA = "id,firstname,lastname\n1,john,testerson"
    # "2,mary,testerson\n" +
    # "3,paul,testerson\n" +

    @patch("builtins.open", mock_open(read_data=DATA))
    def test_valid_csv_load(self):

        valid = [
            dict(id='1', firstname='john', lastname='testerson'),
        ]
        csv = CSVLoadStrategy()
        data = csv.load("foo")
        self.assertEqual(data, valid)

if __name__ == '__main__':
    unittest.main()
