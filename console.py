#!/usr/bin/python3


import cmd
import sys
import inspect
from models import BaseModel
from models import storage
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
        if len(arg) == 0:
            print("** class name missing **")
            return False
        try:
            arg = arg.split(" ")
            if inspect.isclass(eval(arg[0])) is True:
                if issubclass(eval(arg[0]), BaseModel) is True:
                    if cmdtype in ("show", "destroy"):
                        if len(arg) <= 1:
                                print("** instance id missing **")
                                return False
                        key = arg[0] + "." + arg[1]
                        if key in storage.all():
                            if cmdtype == "show":
                                return storage.all()[key]
                            elif cmdtype == "destroy":
                                return key
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
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234."""
        res = self.checkClass(arg, "show") 
        if res is not False:
            print(res)

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id (save the 
        change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.""" 
        res = self.checkClass(arg, "destroy") 
        if res is not False:
            del storage.all()[res]
            storage.save()
    
    def all(self, arg):
        """ Prints all string representation of all instances based or not on 
        the class name. Ex: $ all BaseModel or $ all."""
        pass



if __name__ == "__main__":
    HBNBCommand().cmdloop()
