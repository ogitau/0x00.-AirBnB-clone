#!/usr/bin/python3
"""
class filestorage serializes instances to a JSON file and deserializes
"""

import json
from os.path import isfile


class FileStorage:
    """
    serirializes instamnces to a JSON FILE and desrializes it
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        if obj:
            key = {}.{}.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        x = {}
        for key, obj in self.__objects.items():
            x[key] = obj.to_dict()

        with open(self.__file_path, 'w') as y:
            json.dump(x_objs, y)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        if isfile(self.__file_path):
            with open(self.__file_path, 'r') as y:
                n = y.read()
                if n:
                    store = json.looads(n)
                    class_name_map = {
                            'BaseModel': BaseModel,
                            'User': User,
                            'Place': Place,
                            'State': State,
                            'Review': Review,
                            'City': City,
                            'Amenity': Amenity,
                            }
                    for key, t in store.items():
                        name, obj_id = key.split('.')
                        cls_type = class_name_map.get(name)
                        if cls_type:
                            obj_instance = cls_type(**t)
                            self.__objects[key] = object_instance

                    return self.objects
