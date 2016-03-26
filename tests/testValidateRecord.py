import unittest
import validate


class TestValidateRecord(unittest.TestCase):
    """Test RecordValidator - validate data for a single record"""
    def setUp(self):
        self.validator = validate.RecordValidator()

    def test_validate_valid_record(self):
        raw_data = ['W605', 'F', '05', '636', 'Obesity', '313']
        expected_record = ['W605', 'F', '05', '636', 'Obesity', '313']
        expected_invalid_data_msg = ""
        self.validator.validate(raw_data)
        is_valid = self.validator.record_is_valid()
        actual_record = self.validator.validated_record()
        actual_invalid_data_msg = self.validator.get_invalid_msg()
        self.assertTrue(is_valid)
        self.assertSequenceEqual(actual_record, expected_record)
        self.assertEquals(actual_invalid_data_msg, expected_invalid_data_msg)

    def test_validate_valid_record2(self):
        raw_data = ['C722', 'M', '26', '388', 'Underweight', '22']
        expected_record = ['C722', 'M', '26', '388', 'Underweight', '22']
        expected_invalid_data_msg = ""
        self.validator.validate(raw_data)
        is_valid = self.validator.record_is_valid()
        actual_record = self.validator.validated_record()
        actual_invalid_data_msg = self.validator.get_invalid_msg()
        self.assertTrue(is_valid)
        self.assertSequenceEqual(actual_record, expected_record)
        self.assertEquals(actual_invalid_data_msg, expected_invalid_data_msg)


if __name__ == '__main__':
    unittest.main()
