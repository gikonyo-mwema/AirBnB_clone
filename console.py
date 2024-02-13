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


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


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
        args = parse(arg)
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
        args = parse(arg)
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
        args = parse(arg)
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
        args = parse(arg)
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
        args = parse(arg)
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
        class_name, instance_id = args[0], args[1]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) == 4:
            setattr(all_objs[key], args[2], args[3])
            all_objs[key].save()
        else:
            print("** value missing **")

    def default(self, arg):
        """
        Default behavior for cmd module when input is invalid
        """
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
