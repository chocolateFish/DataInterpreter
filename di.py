# DataInterpreter - facade for the Model
import re



class DataInterpreter():
    id_pattern = re.compile('[A-Z][0-9]{3}')
    gender_pattern = re.compile('(M|F)')
    age_pattern = re.compile('[0-9]{2}')
    sales_pattern = re.compile('[0-9]{3}')
    bmi_pattern = re.compile('(Normal|Overweight|Obesity|Underweight)')
    income_pattern = re.compile('[0-9]{2,3}')

    def __init__(self):
        self.__all_valid_data = []
        self.__all_invalid_data = []

    def add_data(self, all_data_list):
        """
        validate data and add valid data
        :return: None
        """
        for data_list in all_data_list:
            if self.__validate(data_list):
                self.__all_valid_data.append(data_list)
            else:
                self.__all_invalid_data.append(data_list)

    def __validate(self, data_list ):
        """
        validate data using re patterns
        :return: True or False
        """
        return self.id_pattern.match(data_list[0]) and \
               self.gender_pattern.match(data_list[1]) and \
               self.age_pattern.match(data_list[2]) and \
               self.sales_pattern.match(data_list[3]) and \
               self.bmi_pattern.match(data_list[4])and \
               self.income_pattern.match(data_list[5])

    def get_valid_incomes(self):
        """
        return a list of ids
        :return: [str] of data (eg. id)
        """
        income_array = []
        for data in self.__all_valid_data:
            income_array.append(float(data[5]))
        income_array.sort()
        return income_array

    def get_valid_ages(self):
        """
        return a list of ages
        :return: [str] of age data
        """
        age_array = []
        for data in self.__all_valid_data:
            age_array.append(float(data[2]))
        age_array.sort()
        return age_array



