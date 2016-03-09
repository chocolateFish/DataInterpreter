# controller for the DataInterpreter


class Controller:
    def __init__(self, di_model, di_view, di_persistence, chart_view):
        self.model = di_model
        self.view = di_view
        self.persistence = di_persistence
        self.chart = chart_view

    def load_csv(self, file_path):
        try:
            self.model.add_data(self.persistence.load_csv(file_path))
        # except csv.Error:
        # self.view.error_mesage("Error in data")
        except FileNotFoundError:
            self.view.error_message("No such file. please enter a valid file path")

    #move to ChartController
    def draw_chart(self, x_data_name, y_data_name):
        if self.model.contains_valid_data():
            try:
                x_data = [float(item)for item in self.model.get_valid_data(x_data_name)]
                y_data = [float(item)for item in self.model.get_valid_data(y_data_name)]
                self.chart.draw_plot(x_data_name.upper(), y_data_name.upper(), x_data, y_data)
            except ValueError as e:
                self.view.error_message(e.args[0])
            except Exception:
                self.view.error_message("Something went wrong with the charting")
        else:
            self.view.error_message("No valid data loaded. Please load data to generate chart")


