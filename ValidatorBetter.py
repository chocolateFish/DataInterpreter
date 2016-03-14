from string import Template
import re

class RecordValidator2:
    """ Validate data for a single record """
    RULES = {'id': '[A-Z][0-9]{3}',
             'gender': '(M|F)',
             'age': '[0-9]{2}',
             'sales': '[0-9]{3}',
             'bmi': '(Normal|Overweight|Obesity|Underweight)',
             'income': '[0-9]{2,3}'}
    # INVALID_DATA_MSG_TEMPLATE = Template('$invalid_value is invalid $value_name')

    def __init__(self):
        self.validation_msg = []
        self.raw_data = []
        self.validated_data = []
        self.invalid_data = []
        self.is_valid = False

    def __validate_id(self):
        rec_id = self.raw_data[0].strip().upper()
        if re.fullmatch(self.RULES.get('id'), rec_id):
            self.validated_data[0] = rec_id
            return True
        else:
            self.validation_msg.append(rec_id + " is not a valid id")
            return False

    def __validate_gender(self):
        gender = self.raw_data[1].upper()
        if re.fullmatch(self.RULES.get('gender'), gender):
            self.validated_data[0] = gender
            return gender

    def __validate_age(self, age):
        age = age.strip()
        if re.fullmatch(self.RULES.get('age'), age):
            return age

    def __validate_sales(self, sales):
        sales = sales.strip()
        if re.fullmatch(self.RULES.get('sales'), sales):
            return sales

    def __validate_bmi(self, bmi):
        bmi = bmi.strip().capitalize()
        if re.fullmatch(self.RULES.get('bmi'), bmi):
            return bmi

    def __validate_income(self, income):
        income = income.strip()
        if re.fullmatch(self.RULES.get('income'), income):
            return income

    def __validated_record(self):
        return self.validated

    def record_isValid(self):
        return self.is_valid

    def validate(self, data_list):
        self.raw_data = data_list;
