from chatterbot.adapters.output import OutputAdapter
from chatterbot.utils.read_input import input_function
from colorama import init
from colorama import Fore, Back, Style



class TerminalAdapter(OutputAdapter):
    """
    A simple adapter that allows ChatterBot to
    communicate through the terminal.
    """
    def process_input(self, *args, **kwargs):
        """
        Read the user's input from the terminal.
        """
        user_input = input_function()
        return user_input

    def process_response(self, statement):
        """
        Print the response to the user's input.
        """
        init()
        print(Fore.GREEN + statement.text)
        print(Style.RESET_ALL)
        return statement.text

