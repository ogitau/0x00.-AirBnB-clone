#!/usr/bin/python3
"""TestUser module
"""
import unittest
from models.user import User
from datetime import datetime
import os
from models import storage


class TestUser(unittest.TestCase):
    """Test class for the User model
    """
    @classmethod
    def setUpClass(cls):
        """Set up initial objects for testing
        """
        cls.user_instance_1 = User()
        cls.dict_m = cls.user_instance_1.to_dict()
        cls.user_instance_1.save()
        cls.dict_n = cls.user_instance_1.to_dict()
        cls.user_instance_2 = User(**cls.dict_m)

    def test_updated_at(self):
        """Verify that the save method modifies the updated_at instance attribute
        and m and n should have different updated_at values
        """
        self.assertNotEqual(TestUser.dict_m['updated_at'], TestUser.dict_n['updated_at'])
        self.assertEqual(TestUser.dict_m['created_at'], TestUser.dict_n['created_at'])

    def test_to_dict(self):
        """Check if the to_dict method returns a dictionary
        """
        self.assertEqual(type(TestUser.dict_m), dict)
        self.assertEqual(type(TestUser.dict_n), dict)

    def test_kwargs(self):
        """Test if kwargs changes created_at and updated_at attributes
        from string to datetime
        """
        self.assertEqual(type(TestUser.user_instance_2.created_at), datetime)
        self.assertEqual(type(TestUser.user_instance_2.updated_at), datetime)

    def test_if_kwargs_works(self):
        """Ensure that kwargs creates an object from scratch
        """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        dummy_model = User(**TestUser.dict_n)
        dummy_model.save()
        self.assertGreater(len(storage.all()), 0)

    def test_if_kwargs_modified_its_parent(self):
        """Verify that kwargs-id and parent's id are similar
        """
        dummy = User(**TestUser.dict_n)
        self.assertEqual(TestUser.user_instance_1.id, dummy.id)

    def test_uuid(self):
        """Check if different instances have unique ids
        """
        my_model_z = User()
        self.assertNotEqual(TestUser.user_instance_1.id, my_model_z.id)

    def test_type(self):
        """Check the types of instance attributes
        """
        self.assertEqual(type(TestUser.user_instance_1.created_at), datetime)
        self.assertEqual(type(TestUser.user_instance_1.updated_at), datetime)
        self.assertEqual(type(TestUser.user_instance_1.id), str)

    def test_instance_type(self):
        """Check if the instance is of type User
        """
        self.assertTrue(isinstance(TestUser.user_instance_1, User))

    def test_assigned_attribute(self):
        """Test assigned attributes
        """
        dummy = User()
        dummy.first_name = 'test'
        self.assertTrue(isinstance(dummy.first_name, str))


if __name__ == "__main__":
    unittest.main()

