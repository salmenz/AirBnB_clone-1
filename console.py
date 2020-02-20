#!/usr/bin/python3


import cmd
import sys
import inspect
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
""" program called console.py that contains the entry point of the command
interpreter """


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    if not sys.stdin.isatty():
        prompt += '\n'
    file = None

    @staticmethod
    def checkClass(arg, cmdtype):
        """- If the class name is missing, print ** class name missing **
        (ex: $ create)
        - If the class name doesn’t exist, print ** class doesn't exist **
        (ex: $ create MyModel)
        - If the id is missing, print ** instance id missing **
        (ex: $ show BaseModel)
        - If the instance of the class name doesn’t exist for the id,
        print ** no instance found ** (ex: $ show BaseModel 121212)
        """
        if len(arg) == 0 and cmdtype not in ("all"):
            print("** class name missing **")
            return False
        try:
            if cmdtype == "all":
                if len(arg) == 0:
                    return True
            arg = arg.split(" ")
            if inspect.isclass(eval(arg[0])) is True:
                if issubclass(eval(arg[0]), BaseModel) is True:
                    if cmdtype == "all":
                        return arg[0]
                    if cmdtype in ("show", "destroy", "update"):
                        if len(arg) <= 1:
                                print("** instance id missing **")
                                return False
                        key = arg[0] + "." + arg[1]
                        if key in storage.all():
                            if cmdtype == "show":
                                return storage.all()[key]
                            elif cmdtype == "destroy":
                                return key
                            elif cmdtype == "update":
                                if len(arg) <= 2:
                                    print("** attribute name missing **")
                                    return False
                                if len(arg) <= 3:
                                    print("** value missing **")
                                    return False

                        else:
                            print("** no instance found **")
                            return False
                    return True
            else:
                raise Exception
                return False
        except Exception as e:
            print("** class doesn't exist **")

    def emptyline(cmd):
        "An empty line + ENTER shouldn’t execute anything"
        pass

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    def do_EOF(self, arg):
        "Quit command to exit the program"
        print("")
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id. Ex: $ create BaseModel"""

        if self.checkClass(arg, "create") is True:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234."""
        res = self.checkClass(arg, "show")
        if res not in (False, None):
            print(res)

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id (save the
        change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234."""
        res = self.checkClass(arg, "destroy")
        if res not in (False, None):
            del storage.all()[res]
            storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances based or not on
        the class name. Ex: $ all BaseModel or $ all."""
        res = self.checkClass(arg, "all")
        allstr = []
        if res is True:
            for i in storage.all():
                allstr.append(str(storage.all()[i]))
            print(allstr)
        else:
            if res not in (False, None):
                for res in storage.all():
                    allstr.append(str(storage.all()[res]))
                print(allstr)

    def do_update(self, arg):
        """Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        res = self.checkClass(arg, "update")
        if res not in (False, None):
            arg = arg.split(" ")
            key = arg[0] + "." + arg[1]
            setattr(storage.all()[key], arg[2], arg[3].replace("\"", ""))
            storage.save()

    def precmd(self, line):
        """retrieve all instances of a class
        Usage : <class name>.all().
        -------------------------------------------
        retrieve the number of instances of a class
        Usage : <class name>.count().
        -------------------------------------------
        retrieve an instance based on its ID:
        Usage : <class name>.show(<id>).
        -------------------------------------------
        destroy an instance based on his ID
        Usage : <class name>.destroy(<id>).
        -------------------------------------------
        update an instance based on his ID
        Usage : <class name>.update(<id>, <attribute name>, <attribute value>).
        -------------------------------------------
        update an instance based on his ID with a dictionary:
        Usage : <class name>.update(<id>, <dictionary representation>).
        """
        myargs = line.split(" ")
        args = line.split(" ")
        try:
            args = args[0].split(".")
            if inspect.isclass(eval(args[0])) is True:
                method = args[1].split("(")
                if args[1] == "all()":
                    self.do_all(args[0])
                    return ""
                elif args[1] == "count()":
                    i = 0
                    for args[0] in storage.all():
                        i += 1
                    print(i)
                    return ""
                elif method[0] in ("show", "destroy", "update"):
                    arg = args[0] + " " + method[1].split(")")[0]
                    if method[0] == "show":
                        self.do_show(arg)
                    elif method[0] == "destroy":
                        self.do_destroy(arg)
                    elif method[0] == "update":
                        myargs = "".join(myargs)
                        myargs = myargs.split("(")[1]
                        myargs = myargs.replace(")", "")
                        """ check if arg after id is dict or not """
                        oid = myargs.split(",", 1)[0].replace("\"", "")
                        checkDict = myargs.split(",", 1)[1]
                        try:
                            checkDict = eval(checkDict)
                            if type(checkDict) is dict:
                                for k, v in checkDict.items():
                                    arg = args[0] + " " + str(oid) + " " + \
                                            str(k) + " " + str(v)
                                    self.do_update(arg)
                                return ""
                        except Exception as e:
                            print(e)
                            pass
                        myargs = myargs.replace(",", " ")
                        arg = args[0] + " " + myargs
                        arg = arg.replace("\"", "")
                        self.do_update(arg)
                    return ""
        except Exception as e:
            pass
        return line


if __name__ == "__main__":
    HBNBCommand().cmdloop()
