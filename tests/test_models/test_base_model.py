#!/usr/bin/python3
"""TestBaseModel module
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
from models import storage


class TestBaseModel(unittest.TestCase):
    """Class to test the BaseModel module
    """
    instance_1 = BaseModel()
    dict_m = instance_1.to_dict()
    instance_1.save()
    dict_n = instance_1.to_dict()
    instance_2 = BaseModel(**dict_m)

    def test_updated_at(self):
        """Ensure the save method modifies the updated_at attribute
        and dict_m and dict_n should have different updated_at values
        """
        self.assertNotEqual(TestBaseModel.dict_m['updated_at'], TestBaseModel.dict_n['updated_at'])
        self.assertEqual(TestBaseModel.dict_m['created_at'], TestBaseModel.dict_n['created_at'])

    def test_to_dict(self):
        """Verify that the to_dict method returns a dictionary
        """
        self.assertEqual(type(TestBaseModel.dict_m), dict)
        self.assertEqual(type(TestBaseModel.dict_n), dict)

    def test_kwargs(self):
        """Check if kwargs changes created_at and updated_at attributes
        from string to datetime
        """
        self.assertEqual(type(TestBaseModel.instance_2.created_at), datetime)
        self.assertEqual(type(TestBaseModel.instance_2.updated_at), datetime)

    def test_if_kwargs_works(self):
        """Ensure that kwargs creates an object from scratch
        """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        dummy_model = BaseModel(**TestBaseModel.dict_n)
        dummy_model.save()
        self.assertGreater(len(storage.all()), 0)

    def test_if_kwargs_modified_its_parent(self):
        """Check if kwargs-id and parent's id are similar
        """
        dummy = BaseModel(**TestBaseModel.dict_n)
        self.assertEqual(TestBaseModel.instance_1.id, dummy.id)

    def test_uuid(self):
        """Verify that different instances have unique ids
        """
        my_model_z = BaseModel()
        self.assertNotEqual(TestBaseModel.instance_1.id, my_model_z.id)

    def test_type(self):
        """Check the types of instance attributes
        """
        self.assertEqual(type(TestBaseModel.instance_1.created_at), datetime)
        self.assertEqual(type(TestBaseModel.instance_1.updated_at), datetime)
        self.assertEqual(type(TestBaseModel.instance_1.id), str)

    def test_instance_type(self):
        """Check the instance type
        """
        self.assertTrue(isinstance(TestBaseModel.instance_1, BaseModel))


if __name__ == "__main__":
    unittest.main()

