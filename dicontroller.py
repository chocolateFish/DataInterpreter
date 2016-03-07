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
    def draw_chart(self, x_data, y_data, title, save_a):
        # broken
        # write model.get_data(label) function
        # 
        self.model.get_data(x_data)
        ages = self.model.get_valid_ages()
        incomes = self.model.get_valid_incomes()
        self.chart.draw_plot('age-gender relationship', 'ages', 'Genders', ages, incomes)
