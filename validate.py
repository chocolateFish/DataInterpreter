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
    INVALID_DATA_MSG_TEMPLATE = '{data} is invalid {name}'

    def __init__(self):
        self.__invalid_data = []
        self.__record_data = []
        self.__is_valid = None

    @staticmethod
    def wash_field(raw_data):
        """
        strip whitespace chars and capitalize
        :param raw_data: data to wash
        """
        try:
            return raw_data.strip().capitalize()
        except AttributeError:
            raise

    @staticmethod
    def __validate_field(field_rules, field_data):
        """
        given the name and data for a field, validate
        :param field_rules: validation rules
        :param field_data: data for the field
        :return: return True if data is valid, or False if data is invalid or throws an AttributeException
        """
        try:
            return re.fullmatch(field_rules, field_data)
        except TypeError:
            return False

    def validate_id(self, id_data):
        return self.__validate_field(self.RULES.get('id'), id_data)

    def validate_gender(self, gender_data):
        return self.__validate_field(self.RULES.get('gender'), gender_data)

    def validate_age(self, age_data):
        return self.__validate_field(self.RULES.get('age'), age_data)

    def validate_sales(self, sales_data):
        return self.__validate_field(self.RULES.get('sales'), sales_data)

    def validate_bmi(self, bmi_data):
        return self.__validate_field(self.RULES.get('bmi'), bmi_data)

    def validate_income(self, income_data):
        return self.__validate_field(self.RULES.get('income'), income_data)

    def validated_record(self):
        if self.__is_valid is None:
            # break - throw an exception? - validation has not happened yet.
            # this is weird.
            pass
        return self.__record_data

    def record_is_valid(self):
        return self.__is_valid

    def get_invalid_msg(self):
        return " ".join(self.__invalid_data)

    def validate(self, data_list):
        # empty the lists
        del self.__invalid_data[:]
        del self.__record_data[:]
        try:
            # wash data
            for data in data_list:
                self.__record_data.append(data.strip().capitalize())
            # validate data + generate invalid data msg
            self.__is_valid = True
            if not self.validate_id(self.__record_data[0]):
                self.__invalid_data.append(self.INVALID_DATA_MSG_TEMPLATE.format(self.__record_data[0], 'id'))
                self.__is_valid = False
            if not self.validate_gender(self.__record_data[1]):
                self.__invalid_data.append(self.INVALID_DATA_MSG_TEMPLATE.format(self.__record_data[1], 'gender'))
                self.__is_valid = False
            if not self.validate_age(self.__record_data[2]):
                self.__invalid_data.append(self.INVALID_DATA_MSG_TEMPLATE.format(self.__record_data[2], 'age'))
                self.__is_valid = False
            if not self.validate_sales(self.__record_data[3]):
                self.__invalid_data.append(self.INVALID_DATA_MSG_TEMPLATE.format(self.__record_data[3], 'sales'))
                self.__is_valid = False
            if not self.validate_bmi(self.__record_data[4]):
                self.__invalid_data.append(self.INVALID_DATA_MSG_TEMPLATE.format(self.__record_data[4], 'bmi'))
                self.__is_valid = False
            if not self.validate_income(self.__record_data[5]):
                self.__invalid_data.append(self.INVALID_DATA_MSG_TEMPLATE.format(self.__record_data[5], 'income'))
                self.__is_valid = False
        # exception handling/ change error message
        except IndexError:
            self.__is_valid = False
            del self.__invalid_data[:]
            self.__invalid_data.append("Data list too short.")
        except AttributeError:
            self.__is_valid = False
            del self.__invalid_data[:]
            self.__invalid_data.append("Data list contains values of invalid type.")
