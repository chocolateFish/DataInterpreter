import unittest
import di
import dipersistence


class LoadTestCase(unittest.TestCase):

    def setUp(self):
        self.di = di.DataInterpreter()
        from unittest.mock import MagicMock
        persistence = dipersistence.DiPersistence('')
        persistence.load_csv = MagicMock(return_value=3)

    def test_load_csv(self): # use Mocks to stand in for csv loader
        file_path = r'C:\test_validdata.csv'
        expected_data_length = 1000
        expected_row_length = 6
        actual_data = self.persist.load_csv(file_path)
        actual_data_length = len(actual_data)
        actual_row = actual_data[0]
        actual_row_length = len(actual_row)
        self.assertEqual(actual_row_length, expected_row_length)
        self.assertEqual(actual_data_length, expected_data_length)

    """
    def test_add_valid_data(self):
        valid_data = [['W605','M','05','636','Obesity','313'],
                      ['E448','M','97','766','Underweight','248'],
                      ['C722','M','26','388','Underweight','22']]
        expected_valid_data = [['W605','M','05','636','Obesity','313'],
                      ['E448','M','97','766','Underweight','248'],
                      ['C722','M','26','388','Underweight','22']]
        expected_invalid_data = []
        self.di.add_data[valid_data]
        # self.assertEqual(actual_digit_str, expected_digit_str)
    """

if __name__ == '__main__':
    unittest.main()
