#!/usr/bin/python3
"""This module contains the entry point for the console"""

import cmd

class HBNBCommand(cmd.Cmd):
    """The console command interpreter class"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit the console"""
        return True
    
    def do_EOF(self, line):
        """Quit the console"""
        return True
    
    def do_help(self, arg):
        """Show this help message"""
        print("__doc__")

    def emptyline(self):
        return cmd.Cmd.emptyline(self)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
