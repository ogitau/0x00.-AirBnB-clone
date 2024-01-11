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

    def do_all(self, args):
        """method that shows all objects"""
        print_list = []

        if args:
            args = args.split(' ')[0]
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for a, b in storage._FileStorage__objects.items():
                if a.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for a, b in storage._FileStorage__objects.items():
                print_list.append(str(v))

        print(print_list)

    def do_update(self, args):
        """updates objects with new info"""
        ob_name = ob_id = attr_name = attr_val = kwargs = ''

        args = args.partition(" ")
        if args[0]:
            ob_name = args[0]
        else:
            print("** class name is missing **")
            return

        if ob_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        args = args[2].partition(" ")
        if args[0]:
            ob_id = args[0]
        else:
            print("** instance id is missing **")
            return

        key = ob_name + "." + ob_id

        if key not in storage.all():
            print("** no instance found **")
            return
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []

            for a, b in kwargs.items():
                args.append(a)
                args.append(b)
        else:
            args = args[2]
            if args and args[0] == '\"':
                s_qt = arggs.find('\"', 1)
                attr_name = args[1:s_qt]
                args = args[s_qt + 1:]

            args = args.partition(' ')

            if not attr_name and args[0] != ' ':
                attr_name = args[0]

            if args[2] and args[2][0] == '\"':
                attr_val = args[2][1:args[2].find('\"', 1)]

            if not attr_val and args[2]:
                attr_val = args[2].partition(' ')[0]

            args = [attr_name, attr_val]

        
        new_dict = storage.all()[key]

        
        for i, attr_name in enumerate(args):
            if (i % 2 == 0):
                attr_val = args[i + 1]
                if not attr_name:
                    print("** attribute name missing **")
                    return
                if not attr_val:
                    print("** value missing **")
                    return
                if attr_name in HBNBCommand.types:
                    attr_val = HBNBCommand.types[attr_name](attr_val)

                new_dict.__dict__.update({attr_name: attr_val})

        new_dict.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
