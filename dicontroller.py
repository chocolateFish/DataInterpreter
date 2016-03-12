# controller for the DataInterpreter


class Controller:
    def __init__(self, di_model, di_view, chart_view):
        self.model = di_model
        self.view = di_view
        self.chart = chart_view

    def load_csv(self, file_path):
        self.view.show(self.model.load_csv(file_path))

    def draw_chart(self, x_data_name, y_data_name):
        if self.model.contains_valid_records():
            try:
                x_data = [float(item)for item in self.model.get_valid_data(x_data_name)]
                y_data = [float(item)for item in self.model.get_valid_data(y_data_name)]
                self.chart.draw_plot(x_data_name.upper(), y_data_name.upper(), x_data, y_data)
            except ValueError:
                self.view.show("Chart cannot be drawn, invalid data")
            except Exception:
                # learn abt getting meaningful info out of matplotlib exception handling...
                self.view.show("Something went wrong in charting feature charting")
        else:
            self.view.show("No valid data loaded. Please load data to generate chart")
