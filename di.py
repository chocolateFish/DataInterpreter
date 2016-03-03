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

    def find_data_by_selection(self, selections):
        """
        :param selections:
        :return: ?collection - what does the printing module need?
        """
