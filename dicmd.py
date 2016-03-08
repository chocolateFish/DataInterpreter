# cmd view for the DataInterpreter
import cmd
import di
import dicontroller
import dipersistence
import chart


class DataInterpreterCmd(cmd.Cmd):
    """Simple command processor example."""

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.controller = None
        self.intro = "Interpret data from a csv file and generate charts "
        self.prompt = '(Data Interpreter) '

    def register_controller(self, the_controller):
        self.controller = the_controller

    def error_message(self, msg):
        """prints error message"""
        print(msg)

    def do_loadcsv(self, args):
        """
         get file name and pass to controller
         on success, update prompt to selected file
         on failure, complain
        """
        self.controller.load_csv(args)

    def help_loadcsv(self):
        # Add what happens to invalid data - printed?how?
        # Add data that is accepted (eg> ID accepts x345 or X345
        print( '\n'.join(['loads data from a valid csv file at [file_path]',
                          'Each data entry must be in following order: id, gender, age, sales, bmi, income',
                          'Rules for Data as follows',
                          '     id :[A-Z][0-9]{3} example S234',
                          '     gender: (M|F) example M ',
                          '     age: [0-9]{2} example 23',
                          '     sales: [0-9]{3} example 034',
                          '     bmi: (Normal|Overweight|Obesity|Underweight) example Normal',
                          '     income: [0-9]{2,3} example 239']))

    def do_makechart(self, args):
        result = args.split()
        x_data = result[0]
        y_data = result[1]
        title = result[2]
        self.controller.draw_chart(x_data, y_data, title)

    def help_makechart(self):
        # destination directory
        print( '\n'.join(['Generates a chart by plotting [y_data] against [x_data]',
                          '     Accepted inputs for x_data and y_data: age | income | sales',
                          '     Values are taken from file + only valid values are plotted',
                          'titled [title]',
                          'saved as [save_as]',
                          '     Image generated is stored as a .png file ',
                          '*If there is no data this command will not work']))

    def do_EOF(self, args):
        return True

    def postloop(self):
        print()

    def do_quit(self, args):
        """Quits you out of data interpreter cmd."""
        print("Quitting...")
        return 1

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

# app/ instantiate and go
if __name__ == '__main__':
    view = DataInterpreterCmd()
    controller = dicontroller.Controller(di.DataInterpreter(), view, dipersistence.DiPersistence(''),chart.ChartView())
    view.register_controller(controller)
    view.cmdloop()
