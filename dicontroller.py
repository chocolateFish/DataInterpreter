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
            if self.model.get_all_invalid_records():
                invalid_msg = [str(len(self.model.get_all_invalid_records())) + ' invalid records skipped:']
                for r in self.model.get_all_invalid_records():
                    invalid_msg.append(", ".join(r))
                self.view.error_message('\n'.join(invalid_msg))
        except Exception as e:
            self.view.error_mesage(e)
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


