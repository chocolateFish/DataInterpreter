#DataInterpreter - facade for the Model
import model.loader
import model.validator


class DataInterpreter():
    def __init__(self, loader, validator):
        self.loader = loader
        self.validator = validator
        self.allData = []

    def load(self, fileName):
        """
        load data using the available loader
        into allWorkerData
        """

    def validate(self):
        """
        validate data
        :return: ? True or False + where the data was wrong?
        """

    def find_data_by_selection(self, selections):
        """
        :param selections:
        :return: ?collection - what does the printing module need?
        """

