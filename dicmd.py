# cmd view for the DataInterpreter
import cmd
import di
import dicontroller
import dipersistence


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

    def do_loadcsv(self, file_path):
        """
         get file name and pass to controller
         on success, update prompt to selected file
         on failure, complain
        """
        self.controller.load_csv(file_path)

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


    def do_chart(self, x_data, y_data, title):
        """
        pass selected item onto controller
        on success, the pretty print will be stored as a ?format
        on failure, break
        only take in a fixed  set of values
        """
        self.controller.chart(self, x_data, y_data, title)

    def help_chart(self):
        """
        fixed set of values
        :return:
        """

    #
    def do_EOF(self, line):
        return True

    def postloop(self):
        print()

    def do_quit(self):
        """Quits you out of data interpreter cmd."""
        print("Quitting...")
        return 1

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

# app/ instantiate and go
if __name__ == '__main__':
    view = DataInterpreterCmd()
    controller = dicontroller.Controller(di.DataInterpreter(), view, dipersistence.DiPersistence(''))
    view.register_controller(controller)
    view.cmdloop()
