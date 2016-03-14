# DataInterpreter - facade for the Model
import re
from csv import Error as csv_err


class DataInterpreter:
    RULES = {'id': '[A-Z][0-9]{3}',
             'gender': '(M|F)',
             'age': '[0-9]{2}',
             'sales': '[0-9]{3}',
             'bmi': '(Normal|Overweight|Obesity|Underweight)',
             'income': '[0-9]{2,3}'}
    RECORD_COLUMNS = ['id', 'gender', 'age', 'sales', 'bmi', 'income']

    def __init__(self, persistence, validator):
        self.__valid_records = []
        self.__persistence = persistence
        self.__load_status = ""
        self.validator = validator

    def load_csv(self, file_path):
        try:
            self.__add_data(self.__persistence.load_csv(file_path))
        except FileNotFoundError:
            self.__load_status = "No file found at " + file_path + ". Please enter a valid file path."
        except csv_err:  # not sure this is the best way to catch the csv Error?
            self.__load_status = "csv_err"

    def __add_data(self, all_data):
        """
        add valid data
        :param all_data: list containing data for multiple records
        """
        count_invalid = 0
        count_valid = 0
        invalid_data_ids = []
        status = []
        for data_list in all_data:
            if self.__validated(data_list):
                self.__valid_records.append(self.__validated(data_list))
                count_valid += 1
            else:
                invalid_data_ids.append(data_list[0])
                count_invalid += 1
        status.append(str(count_valid) + ' records added')
        if count_invalid:
            status.append(str(count_invalid) + ' invalid records skipped')
            status.append('Invalid data at id = ' + ' '.join(invalid_data_ids))
        self.__load_status = '\n'.join(status)

    def __validated(self, input_list):
        """
        validate data using re patterns
        if The input_list is valid return input_list else return None
        data that raises an exception returns None
        :return: Validated input_list or None
        """
        validated = None
        washed = []
        try:
            # fix case on alphabetic characters
            input_list[0], input_list[1], input_list[4] = \
                input_list[0].upper(), input_list[1].upper(), input_list[4].capitalize()
            for in_str in input_list:
                washed.append(str(in_str.strip()))
            is_valid = re.fullmatch(self.RULES.get('id'), washed[0]) and \
                       re.fullmatch(self.RULES.get('gender'), washed[1]) and \
                       re.fullmatch(self.RULES.get('age'), washed[2]) and \
                       re.fullmatch(self.RULES.get('sales'), washed[3]) and \
                       re.fullmatch(self.RULES.get('bmi'), washed[4])and \
                       re.fullmatch(self.RULES.get('income'), washed[5])
            if is_valid:
                validated = washed
        except TypeError:
            pass
        except IndexError:
            pass
        finally:
            return validated

    def __washed(self, input_list):
            # trim whitespace
            washed = []
            for in_str in input_list:
                washed.append(str(in_str.strip()))
            # fix case on alphabetic characters
            washed[0] = washed[0].upper()
            washed[1] = washed[1].upper()
            washed[4] = washed[4].capitalize()
            return washed

    def get_load_status(self):
        return self.__load_status

    def get_valid_data(self, data_name):
        assert data_name in self.RECORD_COLUMNS
        data_array = []
        for data in self.__valid_records:
            item = data[self.RECORD_COLUMNS.index(data_name)]
            data_array.append(item)
        return data_array

    def contains_valid_records(self):
        if self.__valid_records:
            return True
        return False

    # for testing purposes
    def get_all_valid_records(self):
        return self.__valid_records

if __name__ == "__main__":
    import doctest
    doctest.testmod()