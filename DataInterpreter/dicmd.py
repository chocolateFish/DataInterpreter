# cmd view for the DataInterpreter
import cmd
import model.di
import dicontroller


class DataInterpreterCmd(cmd.Cmd):
    """Simple command processor example."""

    def __init(self):
        cmd.Cmd.__init__(self)
        # self.prompt = "PhoneKeyPad: "
        self.intro = "Enter a string to digitize: "

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

    def do_load(self, file_name):
        """
         get file name and pass to controller
         on success, update prompt to selected file
         on failure, complain
        """

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
        """Quits you out of PhoneKeyPad."""
        print("Quitting...")
        return 1

# app/ instantiate and go
"""
if __name__ == '__main__':
    view = KeyPadCmd()
    controller = kpcontroller.Controller(kpmodel.PhoneKeyPad(), view)
    view.register_controller(controller)
    view.cmdloop()
"""