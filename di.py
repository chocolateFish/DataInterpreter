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

    def __init__(self, persistence):
        self.__valid_records = []
        self.persistence = persistence

    def load_csv(self, file_path):
        status = ""
        try:
            status = self.__add_data(self.persistence.load_csv(file_path))
        except FileNotFoundError:
            status = "No file found at " + file_path + ". Please enter a valid file path."
        except csv_err:  # not sure this is the best way to catch the csv Error?
            status = "csv_err"
        except Exception as e:
            status = e
        finally:
            return status

    def __add_data(self, all_data):
        """
        add valid data
        :param all_data: list containing data for multiple records
        """
        count_invalid = 0
        count_valid = 0
        invalid_data = 'Invalid data at id ='
        for data_list in all_data:
            if self.__validated(data_list):
                self.__valid_records.append(self.__validated(data_list))
                count_valid += 1
            else:
                # self.__invalid_records.append(data_list)
                invalid_data += " " + data_list[0]
                count_invalid += 1
        status = str(count_valid) + ' records added'
        if count_invalid:
            status += '\n' + str(count_invalid) + ' invalid records skipped:\n' + invalid_data
        return status

    def __validated(self, input_list):
        """
        validate data using re patterns
        if The input_list is valid return input_list else return None
        :return: Validated input_list or None
        >>>__validated("W605","M","05","636","Obesity","313")
        ["W605","M","05","636","Obesity","313"]
        >>>__validated("T604","f","32","636","Normal","31")
        ["T604","F","32","636","Normal","31"]
        >>>__validated("F","32","636","Normal","31")
        None
        >>>__validated("582","M","52","210","OBESITY","36")
        None
        >>>__validated("","M","42","617","Normal","82")
        None
        >>>__validated("B*&@", "F","6","511","Normal","25")
        None
        """
        validated = None
        try:
            is_valid = re.fullmatch(self.RULES.get('id'), input_list[0].upper()) and \
                       re.fullmatch(self.RULES.get('gender'), input_list[1].upper()) and \
                       re.fullmatch(self.RULES.get('age'), input_list[2]) and \
                       re.fullmatch(self.RULES.get('sales'), input_list[3]) and \
                       re.fullmatch(self.RULES.get('bmi'), input_list[4].capitalize())and \
                       re.fullmatch(self.RULES.get('income'), input_list[5])
            if is_valid:
                validated = input_list
        except TypeError:
            pass
        except IndexError:
            pass
        finally:
            return validated

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
