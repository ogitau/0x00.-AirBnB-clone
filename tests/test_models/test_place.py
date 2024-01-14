#!/usr/bin/python3
"""test_place module
"""
import unittest
from models.place import Place
from datetime import datetime
import os
from models import storage


class TestPlace(unittest.TestCase):
    """class testing place module
    """

    @classmethod
    def setUpClass(cls):
        """Set up initial objects"""
        cls.place_instance_1 = Place()
        cls.dict_m = cls.place_instance_1.to_dict()
        cls.place_instance_1.save()
        cls.dict_n = cls.place_instance_1.to_dict()
        cls.place_instance_2 = Place(**cls.dict_m)

    def test_updated_at(self):
        """save method modifies updated_at instance attribute
        thus m and n should not be similar at updated_at values
        """
        self.assertNotEqual(TestPlace.dict_m['updated_at'], TestPlace.dict_n['updated_at'])
        self.assertEqual(TestPlace.dict_m['created_at'], TestPlace.dict_n['created_at'])

    def test_to_dict(self):
        """tests if to_dict method returns a dictionary
        """
        self.assertEqual(type(TestPlace.dict_m), dict)
        self.assertEqual(type(TestPlace.dict_n), dict)

    def test_kwargs(self):
        """tests if kwargs changes created_at and updated_at times
        from string to datetime
        """
        self.assertEqual(type(TestPlace.place_instance_2.created_at), datetime)
        self.assertEqual(type(TestPlace.place_instance_2.updated_at), datetime)

    def test_if_kwargs_works(self):
        """tests whether kwargs actually creates an object from scratch
        """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        dummy_model = Place(**TestPlace.dict_n)
        dummy_model.save()
        self.assertGreater(len(storage.all()), 0)

    def test_if_kwargs_modified_its_parent(self):
        """tests if kwargs-id and parents-id are similar
        """
        dummy = Place(**TestPlace.dict_n)
        self.assertEqual(TestPlace.place_instance_1.id, dummy.id)

    def test_uuid(self):
        """test if different instances have unique ids
        """
        my_model_z = Place()
        self.assertNotEqual(TestPlace.place_instance_1.id, my_model_z.id)

    def test_type(self):
        """tests type of instance attributes
        """
        self.assertEqual(type(TestPlace.place_instance_1.created_at), datetime)
        self.assertEqual(type(TestPlace.place_instance_1.updated_at), datetime)
        self.assertEqual(type(TestPlace.place_instance_1.id), str)

    def test_attribute_type(self):
        """tests an instance type
        """
        dummy = Place()
        dummy.price_by_night = 100
        self.assertTrue(type(dummy.price_by_night), int)

if __name__ == "__main__":
    unittest.main()

