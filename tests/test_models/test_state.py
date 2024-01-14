#!/usr/bin/python3
"""TestState module
"""
import unittest
from models.state import State
from datetime import datetime
import os
from models import storage


class TestState(unittest.TestCase):
    """Test class for the State model
    """
    @classmethod
    def setUpClass(cls):
        """Set up initial objects for testing
        """
        cls.state_instance_1 = State()
        cls.dict_m = cls.state_instance_1.to_dict()
        cls.state_instance_1.save()
        cls.dict_n = cls.state_instance_1.to_dict()
        cls.state_instance_2 = State(**cls.dict_m)

    def test_updated_at(self):
        """Verify that the save method modifies the updated_at instance attribute
        and m and n should have different updated_at values
        """
        self.assertNotEqual(TestState.dict_m['updated_at'], TestState.dict_n['updated_at'])
        self.assertEqual(TestState.dict_m['created_at'], TestState.dict_n['created_at'])

    def test_to_dict(self):
        """Check if the to_dict method returns a dictionary
        """
        self.assertEqual(type(TestState.dict_m), dict)
        self.assertEqual(type(TestState.dict_n), dict)

    def test_kwargs(self):
        """Test if kwargs changes created_at and updated_at attributes
        from string to datetime
        """
        self.assertEqual(type(TestState.state_instance_2.created_at), datetime)
        self.assertEqual(type(TestState.state_instance_2.updated_at), datetime)

    def test_if_kwargs_works(self):
        """Ensure that kwargs creates an object from scratch
        """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        dummy_model = State(**TestState.dict_n)
        dummy_model.save()
        self.assertGreater(len(storage.all()), 0)

    def test_if_kwargs_modified_its_parent(self):
        """Verify that kwargs-id and parent's id are similar
        """
        dummy = State(**TestState.dict_n)
        self.assertEqual(TestState.state_instance_1.id, dummy.id)

    def test_uuid(self):
        """Check if different instances have unique ids
        """
        my_model_z = State()
        self.assertNotEqual(TestState.state_instance_1.id, my_model_z.id)

    def test_type(self):
        """Check the types of instance attributes
        """
        self.assertEqual(type(TestState.state_instance_1.created_at), datetime)
        self.assertEqual(type(TestState.state_instance_1.updated_at), datetime)
        self.assertEqual(type(TestState.state_instance_1.id), str)

    def test_attribute_type(self):
        """Check the attribute type of an instance
        """
        dummy = State()
        self.assertTrue(isinstance(dummy.name, str))


if __name__ == "__main__":
    unittest.main()

