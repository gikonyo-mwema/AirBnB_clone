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
        """
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        args = arg.split()
        if len(args) < 1:
            print('** class name missing **')
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance = None
            for obj in BaseModel.all():
                if obj.id == args[1]:
                    instance = obj
                    break
            if instance is None:
                print("** no instance found **")
            else:
                print(instance)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        if len(args) < 1:
            print("** Class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance = None
            for obj in BaseModel.all():
                if obj.id == args[1]:
                    instance = obj
                    break
            if instance is None:
                print("** no instance found **")
            else:
                BaseModel.destroy(instance)

    def do_all(self, arg):
        """
        Prints all string representationf of ll instances
        """
        if arg:
            if arg != "BaseModel":
                print("** class doesn't exist **")
            else:
                for obj in BaseModel.all():
                    if obj.__class__.__name__ == arg:
                        print(obj)
        else:
            for obj in BaseModel.all():
                print(obj)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id or
        updating attribute
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            # find the instance with the given id
            instance = None
            for obj in BaseModel.all():
                if obj.id == args[1]:
                    instance = obj
                    break
                if instance is None:
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    setattr(instance, args[2], args[3])
                    instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
