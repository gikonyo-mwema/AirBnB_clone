#!/usr/bin/python3
"""
This module contains a command interpreter for Airbnb clone.
"""

import cmd
import json
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that inherits from cmd.Cmd
    """

    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "State", "City",
                     "Place", "Amenity", "Review"]

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print("")
        return True

    def emptyline(self):
        """
        An empty line plus ENTER should do nothing
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id.
        """
        args = arg.split()
        if len(args) < 2:
            print('** class name missing **' if not args
                  else '** instance id missing **')
            return

        class_name, instance_id = args[0], args[1]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the
        change into the JSON file).
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
        all_objs = storage.all()
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not
        on the class name.
        """
        args = arg.split()
        if arg and args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        instances = [str(obj) for obj in all_objs.values()
                     if isinstance(obj, eval(args[0]))]
        print(instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        args = arg.split()
        if len(args) < 4:
            if len(args) < 1:
                print("** class name missing **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            else:
                print("** value missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        attr_name = args[2]
        attr_value = args[3]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()
        if key in all_objs:
            instance = all_objs[key]
            if hasattr(instance, attr_name):
                if attr_name not in ['id', 'created_', 'updated_at']:
                    attr_type = type(getattr(instance, attr_name))
                try:
                    setattr(instance, attr_name, attr_type(attr_value))
                    storage.save()
                except ValueError:
                    print("** value missing **")
            else:
                print("** no instance found **")
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
