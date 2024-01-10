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

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Handles EOF to exit the program"""
        return True
    
    def emptyline(self):
        """Overides the emptyline method"""
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
