#!/usr/bin/python3
"""
This module contains a command interpreter for Airbnb clone.
"""


import cmd
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that inherits from cmd.Cmd
    """

    prompt = '(hbnb) '
    valid_classes = ["BaseModel"]

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        An empty line plus ENTER should no nothing
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it and prints id

        Usage: create <class name>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance

        Usage: show <class name> <id>
        """
        args = arg.split()
        if len(args) < 2:
            print('** class name missing **' if not args
                  else '** instance id missing **')
            return

        class_name, instance_id = args[0], args[1]
        if class_name not in self.valid_classes:
            print("** class doen't exist **")
            return
        key = "{}.{}".format(class_name, instance_id)
        if key in BaseModel.__objects:
            print(BaseModel.__objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id

        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **" if not args
                  else "** instance id missing **")
            return
        class_name, instance_id = args[0], args[1]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, instance_id)
        if key in BaseModel.__objects:
            del BaseModel.__objects[key]
            BaseModel.save_to_file()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representationf of ll instances

        Usage: arg.split()
        """
        args = arg.split()
        if arg and args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        instances = [str(obj) for obj in BaseModel.__objects.values()]
        print(instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name, instance_id, attr_name, attr_value =
        args[0], args[1], args[2], args[3]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, instance_id)
        if key in BaseModel.__objects:
            instance = BaseModel.__objects[key]
            if hasattr(instance, attr_name):
                attr_type = type(getattr(instance, attr_name))
                try:
                    setattr(instance, attr_name, attr_type(attr_value))
                    BaseModel.save_to_file()
                except ValueError:
                    print("** value missing **")
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
