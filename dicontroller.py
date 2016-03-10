# controller for the DataInterpreter
from csv import Error as csv_err


class Controller:
    def __init__(self, di_model, di_view, chart_view):
        self.model = di_model
        self.view = di_view
        self.chart = chart_view

    def load_csv(self, file_path):
        try:
            self.model.load_csv(file_path)
            if self.model.contains_invalid_records():
                self.view.error_message(self.model.get_all_invalid_records())
        except csv_err: # not sure this is the best way to catch the csv Error?
            self.view.error_message(csv_err)
        except FileNotFoundError:
            self.view.error_message("No such file. please enter a valid file path")

    def draw_chart(self, x_data_name, y_data_name):
        if self.model.contains_valid_records():
            try:
                x_data = [float(item)for item in self.model.get_valid_data(x_data_name)]
                y_data = [float(item)for item in self.model.get_valid_data(y_data_name)]
                self.chart.draw_plot(x_data_name.upper(), y_data_name.upper(), x_data, y_data)
            except ValueError as e:
                self.view.error_message("Chart cannot be drawn, invalid data")
            except Exception:
                # learn abt getting meaningful info out of matplotlib exception handling...
                self.view.error_message("Something went wrong in charting feature charting")
        else:
            self.view.error_message("No valid data loaded. Please load data to generate chart")


