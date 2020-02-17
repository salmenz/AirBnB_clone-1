#!/usr/bin/python3


import cmd
import sys
import inspect
from models import BaseModel 
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
            if inspect.isclass(eval(arg)) is True:
                if issubclass(eval(arg), BaseModel) is True:
                    return True
        except Exception:
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
        if self.checkClass(arg, "show") is True:
            pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
