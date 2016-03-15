import unittest
import di
import dipersistence
from unittest.mock import MagicMock


class LoadTestCase(unittest.TestCase):

    def setUp(self):
        persistence = dipersistence.DiPersistence()
        persistence.load_csv = MagicMock()
        self.mock_load = persistence.load_csv
        self.di = di.DataInterpreter(persistence)

    def test_load_valid_record(self):
        file_contents = [['W605', 'M', '05', '636', 'Obesity', '313'],
                         ['E448', 'M', '97', '766', 'Underweight', '248'],
                         ['C722', 'M', '26', '388', 'Underweight', '22']]
        expected_data = [['W605', 'M', '05', '636', 'Obesity', '313'],
                         ['E448', 'M', '97', '766', 'Underweight', '248'],
                         ['C722', 'M', '26', '388', 'Underweight', '22']]
        self.mock_load.return_value = file_contents
        file_path = 'some_file.csv'
        self.di.load_csv(file_path)
        actual_data = self.di.get_all_valid_records()
        self.assertSequenceEqual(actual_data, expected_data)

    def test_load_invalid_records_to_correct_case(self):
        file_contents = [['j487', 'm', '76', '274','Underweight', '956'],
                         ['L613', 'f', '71', '753', 'UNDERWEIGHT', '36'],
                         ['S658', 'F', '40', '307', 'normal', '05'],
                         ['n036', 'F', '49', '628', 'UndeRWEIght', '656']]
        expected_data = [['J487', 'M', '76', '274', 'Underweight', '956'],
                         ['L613', 'F', '71', '753', 'Underweight', '36'],
                         ['S658', 'F', '40','307', 'Normal', '05'],
                         ['N036', 'F', '49', '628', 'Underweight', '656']]
        self.mock_load.return_value = file_contents
        file_path = 'some_file.csv'
        self.di.load_csv(file_path)
        actual_data = self.di.get_all_valid_records()
        # self.mock_load.assert_called_with(file_path)
        self.assertSequenceEqual(actual_data, expected_data)

    def test_load_records_with_invalid_id_data(self):
        file_contents = [['j487', 'M', '76', '274', 'Underweight', '956'],
                         ['605', 'M', '05', '636','Obesity', '313'],
                         ['E44', 'M', '97', '766', 'Underweight', '248'],
                         ['C7224', 'M', '26', '388', 'Underweight', '22'],
                         ['N#%6', 'F', '49', '628', 'Underweight', '656'],
                         ['', 'F', '40', '307', 'Normal', '05']]
        expected_data = [['J487', 'M', '76', '274', 'Underweight', '956']]
        self.mock_load.return_value = file_contents
        file_path = 'some_file.csv'
        self.di.load_csv(file_path)
        actual_data = self.di.get_all_valid_records()
        # self.mock_load.assert_called_with(file_path)
        self.assertSequenceEqual(actual_data, expected_data)

    def test_load_records_with_invalid_gender_data(self):
        file_contents = [['S605', ' M ', '05', '636', 'Obesity', '313'],
                         ['E440', ' m ', '97', '766', 'Underweight', '248'],
                         ['C724', 'm', '26', '388', 'Underweight', '22'],
                         ['N246', ' f ', '49', '628', 'Underweight', '656'],
                         ['W245', '', '40', '307', 'Normal', '05'],
                         ['W245', '4', '40', '307', 'Normal', '05']]
        expected_data = [['S605', 'M', '05', '636','Obesity', '313'],
                         ['E440', 'M', '97', '766', 'Underweight', '248'],
                         ['C724', 'M', '26', '388', 'Underweight', '22'],
                         ['N246', 'F', '49', '628', 'Underweight', '656']]
        self.mock_load.return_value = file_contents
        file_path = 'some_file.csv'
        self.di.load_csv(file_path)
        actual_data = self.di.get_all_valid_records()
        # self.mock_load.assert_called_with(file_path)
        self.assertSequenceEqual(actual_data, expected_data)

    def test_load_records_with_invalid_age_data(self):
        file_contents = [['W605', 'M', '5', '636', 'Obesity', '313'],
                         ['E448', 'M', '979', '766', 'Underweight', '248'],
                         ['E448', 'M', '97 ', '766', 'Underweight', '248'],
                         ['C722', 'M', '0', '388', 'Underweight', '22'],
                         ['C722', 'M', '', '388', 'Underweight', '22']]
        expected_data = [['E448', 'M', '97', '766', 'Underweight', '248']]
        self.mock_load.return_value = file_contents
        file_path = 'some_file.csv'
        self.di.load_csv(file_path)
        actual_data = self.di.get_all_valid_records()
        self.assertSequenceEqual(actual_data, expected_data)

    def test_load_records_with_invalid_sales_data(self):
        file_contents = [['W605', 'M', '05', '63', 'Obesity', '313'],
                         ['E448', 'M', '97', ' 766 ', 'Underweight', '248'],
                         ['C722', 'M', '26', '3886', 'Underweight', '22']]
        expected_data = [['E448', 'M', '97', '766', 'Underweight', '248']]
        self.mock_load.return_value = file_contents
        file_path = 'some_file.csv'
        self.di.load_csv(file_path)
        actual_data = self.di.get_all_valid_records()
        self.assertSequenceEqual(actual_data, expected_data)

    def test_load_records_with_invalid_bmi_data(self):
        # !should actually be repeated with invalid vales for each value
        file_contents = [['W605', 'M', '05', '636', 'OBESITY', '313'],
                         ['E448', 'M', '97', '766', ' Obesity ', '248'],
                         ['C722', 'M', '26', '388', 'undeRWEIght', '22']]
        expected_data = [['W605', 'M', '05', '636', 'Obesity', '313'],
                         ['E448', 'M', '97', '766', 'Obesity', '248'],
                         ['C722', 'M', '26', '388', 'Underweight', '22']]
        self.mock_load.return_value = file_contents
        file_path = 'some_file.csv'
        self.di.load_csv(file_path)
        actual_data = self.di.get_all_valid_records()
        self.assertSequenceEqual(actual_data, expected_data)

    def test_load_records_with_invalid_income_data(self):
        file_contents = [['W605', 'M', '05', '636', 'Obesity', '3130'],
                         ['E448', 'M', '97', '766', 'Underweight', '2'],
                         ['C722', 'M', '26', '388', 'Underweight', ''],
                         ['C722', 'M', '26', '388', 'Underweight', ' 22 ']]
        expected_data = [['C722', 'M', '26', '388', 'Underweight', '22']]
        self.mock_load.return_value = file_contents
        file_path = 'some_file.csv'
        self.di.load_csv(file_path)
        actual_data = self.di.get_all_valid_records()
        self.assertSequenceEqual(actual_data, expected_data)


if __name__ == '__main__':
    unittest.main()
