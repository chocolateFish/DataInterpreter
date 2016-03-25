import unittest
import validate


class TestWashFieldData(unittest.TestCase):
    """Test RecordValidator.wash_field"""
    def setUp(self):
        self.validator = validate.RecordValidator()

    def test_wash_id_with_trailing_white_spaces(self):
        raw_data = ' J487'
        actual_washed = self.validator.wash_field(raw_data)
        expected_washed = "J487"
        self.assertEquals(actual_washed, expected_washed)

    def test_wash_id_with_lower_case(self):
        raw_data = 'j487'
        actual_washed = self.validator.wash_field(raw_data)
        expected_washed = "J487"
        self.assertEquals(actual_washed, expected_washed)

    def test_wash_gender_lowercase(self):
        raw_data = "f"
        actual_washed = self.validator.wash_field(raw_data)
        expected_washed = "F"
        self.assertEquals(actual_washed, expected_washed)

    def test_wash_gender_with_trailing_white_spaces(self):
        raw_data = " M"
        actual_washed = self.validator.wash_field(raw_data)
        expected_washed = "M"
        self.assertEquals(actual_washed, expected_washed)

    def test_wash_gender_lowercase_with_trailing_white_spaces(self):
        raw_data = " f "
        actual_washed = self.validator.wash_field(raw_data)
        expected_washed = "F"
        self.assertEquals(actual_washed, expected_washed)

    def test_wash_age_with_trailing_white_spaces(self):
        raw_data = " 78 "
        actual_washed = self.validator.wash_field(raw_data)
        expected_washed = "78"
        self.assertEquals(actual_washed, expected_washed)

    def test_wash_bmi_lowercase_overweight(self):
        raw_data = "overweight"
        actual_washed = self.validator.wash_field(raw_data)
        expected_washed = "Overweight"
        self.assertEquals(actual_washed, expected_washed)

    def test_wash_bmi_mixed_case_underweight(self):
        raw_data = "unDERweigHt"
        actual_washed = self.validator.wash_field(raw_data)
        expected_washed = "Underweight"
        self.assertEquals(actual_washed, expected_washed)

    def test_wash_bmi_with_trailing_white_spaces(self):
        raw_data = " normal "
        actual_washed = self.validator.wash_field(raw_data)
        expected_washed = "Normal"
        self.assertEquals(actual_washed, expected_washed)

    def test_wash_income_with_trailing_white_spaces(self):
        raw_data = " 34 "
        actual_washed = self.validator.wash_field(raw_data)
        expected_washed = "34"
        self.assertEquals(actual_washed, expected_washed)

    def test_wash_sales_with_trailing_white_spaces(self):
        raw_data = " 256 "
        actual_washed = self.validator.wash_field(raw_data)
        expected_washed = "256"
        self.assertEquals(actual_washed, expected_washed)


if __name__ == '__main__':
    unittest.main()
