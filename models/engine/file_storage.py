#!/usr/bin/python3
"""
class filestorage serializes instances to a JSON file and deserializes
"""

import json
from os.path import isfile
from collections import OrderedDict


class FileStorage:
    """
    serializes instances to a JSON FILE and deserializes it
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
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        x_objs = OrderedDict()
        for key, value in self.__objects.items():
            x_objs[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as y:
            x_objs = OrderedDict()
            for key, value in self.__objects.items():
                x_objs[key] = value.to_dict()

            json.dump(x_objs, y, ensure_ascii=False, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        """
        from models.base_model import BaseModel
        if isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as y:
                n = y.read()
                if n:
                    store = json.loads(n)
                    for key, t in store.items():
                        name, obj_id = key.split('.')
                        if name in self.classes:
                            cls_type = self.classes[name]
                            obj_instance = cls_type(**t)
                            if 'created_at' in value:
                                obj.created_at = datetime.strptime(value['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                                if 'updated_at' in value:
                                    obj.updated_at = datetime.strptime(value['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                                    self.__objects[key] = obj_instance

                    return self.__objects
    @property
    def classes(self):
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


        classes = {
                'BaseModel': BaseModel,
                'User': User,
                'Place': Place,
                'State': State,
                'Review': Review,
                'City': City,
                'Amenity': Amenity,
                }
        return classes
