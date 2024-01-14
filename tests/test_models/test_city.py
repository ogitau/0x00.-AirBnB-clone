#!/usr/bin/python3
"""test_city module
"""
import unittest
from models.city import City
from datetime import datetime
import os
from models import storage


class TestCity(unittest.TestCase):
    """class testing city module
    """

    @classmethod
    def setUpClass(cls):
        """Set up initial objects"""
        cls.city_instance_1 = City()
        cls.dict_m = cls.city_instance_1.to_dict()
        cls.city_instance_1.save()
        cls.dict_n = cls.city_instance_1.to_dict()
        cls.city_instance_2 = City(**cls.dict_m)

    def test_updated_at(self):
        """save method modifies updated_at instance attribute
        thus m and n should not be similar at updated_at values
        """
        self.assertNotEqual(TestCity.dict_m['updated_at'], TestCity.dict_n['updated_at'])
        self.assertEqual(TestCity.dict_m['created_at'], TestCity.dict_n['created_at'])

    def test_to_dict(self):
        """tests if to_dict method returns a dictionary
        """
        self.assertEqual(type(TestCity.dict_m), dict)
        self.assertEqual(type(TestCity.dict_n), dict)

    def test_kwargs(self):
        """tests if kwargs changes created_at and updated_at times
        from string to datetime
        """
        self.assertEqual(type(TestCity.city_instance_2.created_at), datetime)
        self.assertEqual(type(TestCity.city_instance_2.updated_at), datetime)

    def test_if_kwargs_works(self):
        """tests whether kwargs actually creates an object from scratch
        """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        dummy_model = City(**TestCity.dict_n)
        dummy_model.save()
        self.assertGreater(len(storage.all()), 0)

    def test_if_kwargs_modified_its_parent(self):
        """tests if kwargs-id and parents-id are similar
        """
        dummy = City(**TestCity.dict_n)
        self.assertEqual(TestCity.city_instance_1.id, dummy.id)

    def test_uuid(self):
        """test if different instances have unique ids
        """
        my_model_z = City()
        self.assertNotEqual(TestCity.city_instance_1.id, my_model_z.id)

    def test_type(self):
        """tests type of instance attributes
        """
        self.assertEqual(type(TestCity.city_instance_1.created_at), datetime)
        self.assertEqual(type(TestCity.city_instance_1.updated_at), datetime)
        self.assertEqual(type(TestCity.city_instance_1.id), str)

if __name__ == "__main__":
    unittest.main()

