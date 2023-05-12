#!/usr/bin/python3

"""Defines the HBnB console."""
import re
import cmd
from shlex import split as parse
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

def parse_arg(arg):
    """
    Parses the input argument to find either curly braces or brackets,
    which are then extracted along with any text before them.

    Returns the extracted text as a list with commas stripped from each token.
    """
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in arg.split()]
        else:
            return parse_brackets(arg, brackets)
    else:
        return parse_curly_braces(arg, curly_braces)

    def parse_brackets(arg, brackets):
        lexer = arg[:brackets.span()[0]].split()
        retl = [i.strip(",") for i in lexer]
        retl.append(brackets.group())
        return retl
    def parse_curly_braces(arg, curly_braces):
        lexer = arg[:curly_braces.span()[0]].split()
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

class HBNBCommand(cmd, Cmd):
    """a class that contains the entry point of the command interpreter.
       Attributes:
        prompt (str): The command prompt.
    """
    prompt = '(hbnb) '
    class_list = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place',
                  'Review']


    def emptyline(self):
        """method to do nothing when an empty line is inputed.
        """
        pass

    def do_quit(self, args):
        """ Quit command to exit the program.
        """
        return True

    def do_EOF(self, args):
        """EOF command to exit the program.
        """
        return True

    def do_create(self, arg):
        """Create command to create a new instance of BaseModel, save it in a
        JSON file and prints the id.

        Attributes:
            args (str): inputted line in command prompt.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Show command that prints the string representation of an instance
        based on the class name and id.

        Attributes:
           args (str): inputted line in command prompt.
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Destroy command that deletes an instance based on the class name
        and id. Save the change in JSON file.

        Attributes:
            args (str): inputted line in command prompt.
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name.
        """
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def default(self, arg):
        """Default method that is called when the inputted command starts
        with a class name.

        Attributes:
            args (str): The inputted line string
        """
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match:
                command = [argl[1][:match.span()[0]], match.group(1)[1:-1]]
                if command[0] in argdict:
                    if hasattr(self, argdict[command[0]].__name__):
                        call = "{} {}".format(argl[0], command[1])
                        return argdict[command[0]](self, call)
                    else:
                        raise NotImplementedError("Method {} not implemented".format(argdict[command[0]].__name__))
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_update(self, arg):
       """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        argl = parse(arg)
        objdict = storage.all()

        try:
            if not argl[0]:
                print("** class name missing **")
                return False
            elif argl[0] not in HBNBCommand.class_list:
                print("** class doesn't exist **")
                return False
            elif not argl[1]:
                print("** instance id missing **")
                return False
            elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
                print("** no instance found **")
                return False
            elif not argl[2]:
                print("** attribute name missing **")
                return False
            elif not argl[3]:
                print("** value missing **")
                return False
        except IndexError:
            print("** instance id missing **")
            return False

        obj = objdict["{}.{}".format(argl[0], argl[1])]

        try:
            valtype = type(obj.__class__.__dict__[argl[2]])
            obj.__dict__[argl[2]] = valtype(argl[3])
        except KeyError:
            obj.__dict__[argl[2]] = argl[3]
        storage.save()

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = sum(1 for obj in storage.all().values() if argl[0] == obj.__class__.__name__)
        print(count)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
