#!/usr/bin/python3
"""
This module contains a command interpreter for Airbnb clone.
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that inherits from cmd.Cmd
    """

    prompt = '(hbng) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def emptyline(self):
        """
        An empty line plus ENTER should no nothing
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
