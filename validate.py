from string import Template
import re


class RecordValidator:
    """ Validate data for a single record """
    RULES = {'id': '[A-Z][0-9]{3}',
             'gender': '(M|F)',
             'age': '[0-9]{2}',
             'sales': '[0-9]{3}',
             'bmi': '(Normal|Overweight|Obesity|Underweight)',
             'income': '[0-9]{2,3}'}
    RECORD_COLUMNS = ['id', 'gender', 'age', 'sales', 'bmi', 'income']
    # INVALID_DATA_MSG_TEMPLATE = Template('$invalid_value is invalid $value_name')

    def __init__(self):
        self.validation_msg = []
        self.validated_data = []
        self.is_valid = False

    def __wash_id(self, id_data):
        return id_data.upper()

    def __validate_field(self, field_name, raw_data, capitalize):
        try:
            is_valid = False
            data = raw_data.strip()
            if capitalize:
                data = data.capitalize()
            if re.fullmatch(self.RULES.get(field_name), data):
                self.validated_data.insert(self.RECORD_COLUMNS.index(field_name), data)
                is_valid = True
        except AttributeError:
            is_valid = False
        finally:
            return is_valid

    def validate_id(self, id_data):
        return self.__validate_field('id', id_data, True)

    def validate_gender(self, gender_data):
        return self.__validate_field('gender', gender_data, True)

    def validate_age(self, age_data):
        return self.__validate_field('age', age_data, True)

    def validate_id2(self, id_data):
        is_valid = False
        id_data = id_data.strip().upper()
        if re.fullmatch(self.RULES.get('id'), id_data):
            self.validated_data.insert(self.RECORD_COLUMNS.index('id'), id_data)
            is_valid = True
        return is_valid

    def validate_gender2(self, gender_data):
        is_valid = False
        try:
            gender_data = gender_data.strip().upper()
            if re.fullmatch(self.RULES.get('gender'), gender_data):
                self.validated_data.insert(self.RECORD_COLUMNS.index('gender'), gender_data)
                is_valid = True
        except AttributeError:
            is_valid = False
        finally:
            return is_valid

    def validate_age(self, age_data):
        is_valid = False
        try:
            age_data = age_data.strip()
            if re.fullmatch(self.RULES.get('age'), age_data):
                self.validated_data.insert(self.RECORD_COLUMNS.index('age'), age_data)
                is_valid = True
        except AttributeError:
            is_valid = False
        finally:
            return is_valid

    def validate_sales(self, sales_data):
        try:
            is_valid = False
            sales_data = sales_data.strip()
            if re.fullmatch(self.RULES.get('sales'), sales_data):
                self.validated_data.insert(self.RECORD_COLUMNS.index('age'), sales_data)
                is_valid = True
        except AttributeError:
            is_valid = False
        finally:
            return is_valid

    def validate_bmi(self, bmi_data):
        try:
            is_valid = False
            bmi_data = bmi_data.strip().capitalize()
            if re.fullmatch(self.RULES.get('bmi'), bmi_data):
                self.validated_data.insert(self.RECORD_COLUMNS.index('bmi'), bmi_data)
                is_valid = True
        except AttributeError:
            is_valid = False
        finally:
            return is_valid

    def validate_income(self, income_data):
        try:
            is_valid = False
            income_data = income_data.strip()
            if re.fullmatch(self.RULES.get('income'), income_data):
                self.validated_data.insert(self.RECORD_COLUMNS.index('income'), income_data)
                is_valid = True
        except AttributeError:
            is_valid = False
        finally:
            return is_valid

    def __validated_record(self):
        return self.validated

    def record_isValid(self):
        return self.is_valid

    def validate(self, data_list):
        self.raw_data = data_list;
