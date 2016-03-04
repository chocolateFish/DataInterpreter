# controller for the DataInterpreter


class Controller:
    def __init__(self, di_model, di_view, di_persistence):
        self.model = di_model
        self.view = di_view
        self.persistence = di_persistence

    def load_csv(self, file_path):
        try:
            self.model.add_data(self.persistence.load_csv(file_path))
        # except csv.Error:
            # self.view.error_mesage("Error in data")
        except FileNotFoundError:
            self.view.error_message("No such file. please enter a valid file path")

    #move to ChartController
    def chart(self, x_data, y_data, title):
        """
        :param x_data:
        :param y_data:
        :param title:
        :return:
        get x_data array from model (eg. age or income)
        get y_data array from model
        pass to view.
        """
