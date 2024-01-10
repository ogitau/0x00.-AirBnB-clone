#!/usr/bin/python3
""" module that contains the entry point of the cmd interpreter"""

import re
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """contains functionality of HBNB console"""

    prompt = '(hbnb) '

def do_quit(self, command):
    """method to exit the console"""
    return True

def help_quit(self):
    """prints help documentation for quit"""
    print("Exits the program with formatting\n")

def do_EOF(self, arg):
    """Handles EOF to exit the program"""
    print()
    return True
def help_EOF(self):
    """ prints help documentation for EOF"""
    print("Exits the program without formatting\n")

def emptyline(self):
    """Overides the emptyline method"""
    return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
