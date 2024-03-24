#!/usr/bin/python3
"""This module contains the entry point for the console"""

import cmd
from models.base_model import BaseModel
from models import FileStorage


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
        class_name = line.split()[0]
        if not class_name:
            print("** class name missing **")
        if class_name in ['BaseModel']:
            eval(f"{class_name}().save()")
        else:
            print(f"** class doesn't exist **")

    def do_show(self, line):
        class_name = line.split()[0]
        if not class_name:
            print("** class name missing **")
        if class_name in ['BaseModel']:
            instance_id = line.split()[1]
            if not instance_id:
                print("** instance id missing **")
            else:
                instances = FileStorage.__objects
                for key, value in instances.items():
                    if key.split()[1] == instance_id:
                        print(value)
                        return
                print("** no instance found **")
        else:
            print(f"** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
