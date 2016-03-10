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
        add valid data
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
        if The data is valid return True else return False
        :return: True or False

        >>>__validate("W605","M","05","636","Obesity","313")
        True
        >>>__validate("T604","F","32","636","Normal","31")
        True
        >>>__validate("F","32","636","Normal","31")
        True
        >>>__validate("582","M","52","21","Obesity","36")
        False
        >>>__validate("","M","42","617","Normal","82")
        False
        >>>__validate("B*&@", "F","6","511","Normal","25")
        False
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
        invalid_msg = [str(len(self.__invalid_records)) + ' invalid records skipped:']
        for r in self.__invalid_records:
            invalid_msg.append(", ".join(r))
        return '\n'.join(invalid_msg)

    def contains_valid_records(self):
        if self.__valid_records:
            return True
        return False

    def contains_invalid_records(self):
        if self.__invalid_records:
            return True
        return False