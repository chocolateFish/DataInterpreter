# cmd view for the DataInterpreter
import cmd
import di
import dicontroller
import dipersistence

class DataInterpreterCmd(cmd.Cmd):
    """Simple command processor example."""

    def __init(self):
        cmd.Cmd.__init__(self)
        self.prompt = "DataInterpreter: "
        # self.intro = "generate charts"
        self.controller = None

    def register_controller(self, the_controller):
        self.controller = the_controller
    """
    def do_digitize(self, a_string):
        # error handling - invalid input
        self.controller.digitize(a_string)

    def show_output(self, out_str):
        print(out_str)

    def help_digitize(self):
        # add info on valid characters
        print("Map the string entered to digits"
              " as on a phone key pad")
    """

    def do_loadcsv(self, file_path):
        """
         get file name and pass to controller
         on success, update prompt to selected file
         on failure, complain
        """
        self.controller.load_csv(file_path)

    def do_display_pie(self, data_selection):
        """
        pass selected item onto controller
        on success, the pretty print will be stored as a ?format
        on failure, break
        """

    def do_display_table(self, data_selection):
        """
        pass selected item onto controller
        on success, the pretty print will be stored as a ?format
        on failure, break
        """

    def do_EOF(self, line):
        return True

    def postloop(self):
        print()

    def do_quit(self, line):
        """Quits you out of data interpreter cmd."""
        print("Quitting...")
        return 1

# app/ instantiate and go

if __name__ == '__main__':
    view = DataInterpreterCmd()
    controller = dicontroller.Controller(di.DataInterpreter(), view, dipersistence.DiPersistence(r'H:\\'))
    view.register_controller(controller)
    view.cmdloop()
