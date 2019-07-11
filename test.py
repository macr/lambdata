import unittest
from lambdata_richmondtest import DataFrameWithHelpers
import pandas as pd
from random import randint
from unittest.mock import patch


class TestDataFrameWithHelpers(unittest.TestCase):

    def setUp(self):
        random_list = [(randint(1, 1000), randint(1, 1000))
                       for _ in range(1000)]
        data = pd.DataFrame(random_list, columns=['a', 'b'])
        self.data = DataFrameWithHelpers(data)

    @patch('lambdata_richmondtest.train_test_split')
    def test_train_test_val_split(self, mock_split):
        # Mock the return value to for testing second call
        mock_split.return_value = ('Train', 'Test')
        train, test, val = self.data.train_test_val_split()
        # make sure we called it twice
        self.assertEqual(mock_split.call_count, 2)
        # check that we called it with the original dataframe the first time
        self.assertTrue(mock_split.call_args_list[0][0][0].equals(self.data))
        # check that we called it with the return value of the first for 
        # the second time
        self.assertIn('Train', mock_split.call_args_list[1][0])
        # check the final values returned matches the output of the function
        self.assertEqual(train, 'Train')
        self.assertEqual(val, 'Test')


if __name__ == '__main__':
    unittest.main()
