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
    
    def emptyline(self):
        """Quit the console"""
        pass

    def do_create(self, line):
        class_name = line.split()[1]
        if not class_name:
            print("** class doesn't exist **")
        if class_name in ['BaseModel']:
            new_instance = eval(f"{class_name}()")
            new_instance.save()
        else:
            print(f"** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
