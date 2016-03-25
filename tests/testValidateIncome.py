import unittest
import validate


class TestValidateIncome(unittest.TestCase):
    """Test RecordValidator.validate_income with valid and invalid values"""
    def setUp(self):
        self.validator = validate.RecordValidator()

    def test_validate_valid_income_two_chars(self):
        raw_data = "01"
        is_valid = self.validator.validate_income(raw_data)
        self.assertTrue(is_valid)

    def test_validate_valid_income_three_chars(self):
        raw_data = "567"
        is_valid = self.validator.validate_income(raw_data)
        self.assertTrue(is_valid)

    def test_validate_income_with_trailing_white_spaces(self):
        raw_data = " 78 "
        is_valid = self.validator.validate_income(raw_data)
        self.assertFalse(is_valid)

    def test_validate_income_with_not_numeric_chars(self):
        raw_data = "a$"
        is_valid = self.validator.validate_income(raw_data)
        self.assertFalse(is_valid)

    def test_validate_income_too_short(self):
        raw_data = "2"
        is_valid = self.validator.validate_income(raw_data)
        self.assertFalse(is_valid)

    def test_validate_income_too_long(self):
        raw_data = "2235"
        is_valid = self.validator.validate_income(raw_data)
        self.assertFalse(is_valid)

    def test_validate_income_wrong_type(self):
        raw_data = 22
        is_valid = self.validator.validate_income(raw_data)
        self.assertFalse(is_valid)

    def test_validate_income_empty(self):
        raw_data = ""
        is_valid = self.validator.validate_income(raw_data)
        self.assertFalse(is_valid)


if __name__ == '__main__':
    unittest.main()
