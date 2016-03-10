# DataInterpreter - facade for the Model
import re


class DataInterpreter:
    RULES = {'id': '[A-Z][0-9]{3}',
             'gender': '(M|F)',
             'age': '[0-9]{2}',
             'sales': '[0-9]{3}',
             'bmi': '(Normal|Overweight|Obesity|Underweight)',
             'income': '[0-9]{2,3}'}
    RECORD_COLUMNS = ['id', 'gender', 'age', 'sales', 'bmi', 'income']

    def __init__(self, persistence):
        self.__valid_records = []
        self.__invalid_records = []
        self.persistence = persistence

    def load_csv(self, file_path):
        self.__add_data(self.persistence.load_csv(file_path))

    def __add_data(self, all_data):
        """
        validate data and add valid data
        :param all_data: list containing data for multiple records
        """
        for data_list in all_data:
            if self.__validate(data_list):
                self.__valid_records.append(data_list)
            else:
                self.__invalid_records.append(data_list)

    def __validate(self, input_list):
        """
        validate data using re patterns
        :return: True or False
        """
        return len(input_list) == 6 and \
            re.compile(self.RULES.get('id')).match(input_list[0]) and \
            re.compile(self.RULES.get('gender')).match(input_list[1]) and \
            re.compile(self.RULES.get('age')).match(input_list[2]) and \
            re.compile(self.RULES.get('sales')).match(input_list[3]) and \
            re.compile(self.RULES.get('bmi')).match(input_list[4])and \
            re.compile(self.RULES.get('income')).match(input_list[5])

    def get_valid_data(self, data_name):
        assert data_name in self.RECORD_COLUMNS
        data_array = []
        for data in self.__valid_records:
            item = data[self.RECORD_COLUMNS.index(data_name)]
            data_array.append(item)
        return data_array

    def get_all_invalid_records(self):
        return self.__invalid_records

    def contains_valid_records(self):
        if self.__valid_records:
            return True
        else:
            return False
