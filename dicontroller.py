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
