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
    
    def do_create(self, args):
        """creates classes objects"""
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args]()
        storage.save()
        print(new_instance.id)
        storage.save()
   
    def do_show(self, args):
       """method to show objects"""
       n = args.partition(" ")
       ob_name = n[0]
       ob_id = n[2]

       if ob_id and ' ' in ob_id:
           ob_id = ob_id.partition(' ')[0]

       if not ob_name:
           print("** class name missing **")
           return
        
       if ob_name not in HBNBCommand.classes:
            print("** class doen't exist **")
            return

       if not ob_id:
            print("** instance id missing **")
            return

       key = ob_name + "." + ob_id

       try:
           print(storage._FileStorage__objects[key])
       except KeyError:
           print("** no instance found **")
    
    def do_destroy(self, args):
        """Destroys indicated object"""
        n = args.partition(" ")
        ob_name = n[0]
        ob_id = n[2]

        if ob_id and ' ' in ob_id:
            ob_id = ob_id.partition(' ')[0]

        if not ob_name:
            print("** class name missing **")
            return

        if ob_name not in HBNBCommand.classes:
            print("** class doen't exist **")
            return

        if not ob_id:
            print("** instance id missing **")
            return

        key = ob_name + "." + ob_id

        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
