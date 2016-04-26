import unittest
import validate


class TestValidateID(unittest.TestCase):
    """Test RecordValidator.validate_id with valid and invalid values"""
    def setUp(self):
        self.validator = validate.RecordValidator()

    def test_validate_valid_id(self):
        raw_id_data = 'H567'
        is_valid = self.validator.validate_id(raw_id_data)
        self.assertTrue(is_valid)

    def test_validate_id_with_trailing_white_spaces(self):
        raw_id_data = ' J487 '
        is_valid = self.validator.validate_id(raw_id_data)
        self.assertFalse(is_valid)

    def test_validate_id_with_lower_case(self):
        raw_id_data = 'j487'
        is_valid = self.validator.validate_id(raw_id_data)
        self.assertFalse(is_valid)

    def test_validate_id_with_only_whitespace_chars(self):
        """ Given id containing only whitespaces, return false"""
        raw_id_data = '    '
        is_valid = self.validator.validate_id(raw_id_data)
        self.assertFalse(is_valid)

    def test_validate_id_with_not_alphanumeric_chars(self):
        """ Given non alphanumeric character in id , return false"""
        raw_id_data = 'N#%6'
        is_valid = self.validator.validate_id(raw_id_data)
        self.assertFalse(is_valid)

    def test_validate_id_too_short(self):
        """Given len(id) < 4 return false."""
        raw_id_data = '605'
        is_valid = self.validator.validate_id(raw_id_data)
        self.assertFalse(is_valid)

    def test_validate_id_too_long(self):
        """Given len(id) > 4 return false."""
        raw_id_data = 'C7224'
        is_valid = self.validator.validate_id(raw_id_data)
        self.assertFalse(is_valid)

    def test_validate_id_with_missing_alpha_character(self):
        """Given an input of the correct length, with missing alphabetic character at the start, return false."""
        raw_id_data = "6758"
        is_valid = self.validator.validate_id(raw_id_data)
        self.assertFalse(is_valid)

    def test_validate_id_with_missing_numeric_character(self):
        """Given an input of the correct length, with more than one alphabetic character at the start, return false."""
        raw_id_data = "AC67"
        is_valid = self.validator.validate_id(raw_id_data)
        self.assertFalse(is_valid)

    def test_validate_id_empty(self):
        raw_id_data = ""
        is_valid = self.validator.validate_id(raw_id_data)
        self.assertFalse(is_valid)


if __name__ == '__main__':
    unittest.main()
