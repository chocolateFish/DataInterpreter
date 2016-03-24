import unittest
import validate


class TestValidateSales(unittest.TestCase):
    """Test RecordValidator.validate_sales with valid and invalid values"""
    def setUp(self):
        self.validator = validate.RecordValidator()

    def test_validate_valid_sales(self):
        raw_data = "567"
        is_valid = self.validator.validate_sales(raw_data)
        self.assertTrue(is_valid)

    def test_validate_sales_with_trailing_white_spaces(self):
        raw_data = " 787 "
        is_valid = self.validator.validate_sales(raw_data)
        self.assertTrue(is_valid)

    def test_validate_sales_with_not_numeric_chars(self):
        raw_data = "a$3"
        is_valid = self.validator.validate_sales(raw_data)
        self.assertFalse(is_valid)

    def test_validate_sales_too_short(self):
        raw_data = "26"
        is_valid = self.validator.validate_sales(raw_data)
        self.assertFalse(is_valid)

    def test_validate_sales_too_long(self):
        raw_data = "2235"
        is_valid = self.validator.validate_sales(raw_data)
        self.assertFalse(is_valid)

    def test_validate_sales_wrong_type(self):
        raw_data = 22
        is_valid = self.validator.validate_sales(raw_data)
        self.assertFalse(is_valid)

    def test_validate_sales_empty(self):
        raw_data = ""
        is_valid = self.validator.validate_sales(raw_data)
        self.assertFalse(is_valid)


if __name__ == '__main__':
    unittest.main()
