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
        self.__invalid_data_msg = []
        self.__record_data = []
        self.__is_valid = None

    @staticmethod
    def wash_field(raw_data):
        """
        strip whitespace chars and capitalize
        """
        try:
            return raw_data.strip().capitalize()
        except AttributeError:
            raise

    def validate_id(self, id_data):
        try:
            return re.fullmatch(self.RULES.get('id'), id_data)
        except TypeError:
            return False

    def validate_gender(self, gender_data):
        try:
            return re.fullmatch(self.RULES.get('gender'), gender_data)
        except TypeError:
            return False

    def validate_age(self, age_data):
        try:
            return re.fullmatch(self.RULES.get('age'), age_data)
        except TypeError:
            return False

    def validate_sales(self, sales_data):
        try:
            return re.fullmatch(self.RULES.get('sales'), sales_data)
        except TypeError:
            return False

    def validate_bmi(self, bmi_data):
        try:
            return re.fullmatch(self.RULES.get('bmi'), bmi_data)
        except TypeError:
            return False

    def validate_income(self, income_data):
        try:
            return re.fullmatch(self.RULES.get('income'), income_data)
        except TypeError:
            return False

    def validated_record(self):
        if self.__is_valid is None:
            # break - throw an exception? - validation has not happened yet.
            # this is weird.
            pass
        return self.__validated_data

    def record_is_valid(self):
        return self.__is_valid

    def get_invalid_msg(self):
        return " ".join(self.__invalid_data_msg)

    def validate(self, data_list):
        try:
            for data in data_list:
                self.__record_data.append(data.strip().capitalize())

            self.__is_valid = self.validate_id(self.__record_data[0]) and \
                              self.validate_gender(self.__record_data[1]) and \
                              self.validate_age(self.__record_data[2]) and \
                              self.validate_sales(self.__record_data[3]) and \
                              self.validate_bmi(self.__record_data[4]) and \
                              self.validate_income(self.__record_data[5])

        except IndexError:
            self.__invalid_data_msg = "Data list too short."
        finally:
            return True



