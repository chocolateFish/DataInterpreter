# cmd view for the DataInterpreter
import cmd
import di
import dicontroller
import dipersistence
import chart


class DataInterpreterCmd(cmd.Cmd):
    """Simple command processor example."""
    CHART_OPTIONS = ['age income', 'income age', 'age sales', 'sales age', 'income sales', 'sales income']

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.controller = None
        self.intro = "Interpret data from a csv file and generate charts "
        self.prompt = '(Data Interpreter) '

    def register_controller(self, the_controller):
        self.controller = the_controller

    @staticmethod
    def error_message(msg):
        """
        prints error message
        :param msg: str to print
        """
        print("Whoops! ", msg)

    def do_loadcsv(self, file_path):
        """
         get file_path and pass to controller
         :param file_path: file path as a str
        """
        self.controller.load_csv(file_path)

    def help_loadcsv(self):
        # Add what happens to invalid data - printed?how?
        # Add data that is accepted (eg> ID accepts x345 or X345
        print('\n'.join(['loads data from a valid csv file at [file_path]',
                         'Each data entry must be in following order: id, gender, age, sales, bmi, income',
                         'Rules for Data as follows',
                         '     id :[A-Z][0-9]{3} example S234',
                         '     gender: (M|F) example M ',
                         '     age: [0-9]{2} example 23',
                         '     sales: [0-9]{3} example 034',
                         '     bmi: (Normal|Overweight|Obesity|Underweight) example Normal',
                         '     income: [0-9]{2,3} example 239']))

    def do_chart(self, options):
        """
        if options are valid input, otherwise do error
        :param options: string, one of CHART_OPTIONS
        """
        if options and options in self.CHART_OPTIONS:
            result = options.split()
            x_data = result[0]
            y_data = result[1]
            self.controller.draw_chart(x_data, y_data)
        else:
            print("invalid option selected")

    def complete_chart(self, text, line, begidx, endidx):
        if not text:
            completions = self.CHART_OPTIONS[:]
        else:
            completions = [o
                           for o in self.CHART_OPTIONS
                           if o.startswith(text)]
        return completions

    def help_chart(self):
        # destination directory
        print('\n'.join(['Generates a chart using plotting options',
                         'Accepted inputs are:',
                         '     age income',
                         '     income age',
                         '     age sales',
                         '     sales age',
                         '     income sales',
                         '     sales income'
                         '     data values are taken from file and only valid values are plotted',
                         '     Image generated is stored as a .png file ',
                         '!If there is no data this command will not work!']))

    def do_EOF(self, args):
        return True

    def postloop(self):
        print()

    def do_quit(self, args):
        """Quits you out of the Data Interpreter"""
        print("Quitting...")
        return 1

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

# app/ instantiate and go
if __name__ == '__main__':
    view = DataInterpreterCmd()
    controller = dicontroller.Controller(di.DataInterpreter(dipersistence.DiPersistence('')), view, chart.ChartView())
    view.register_controller(controller)
    view.cmdloop()
