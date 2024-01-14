#!/usr/bin/python3
"""Tests cases for Amenity subclass"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up a clean instance of Amenity for each test"""
        pass
       # self.amenity = Amenity()

    def test_subclass(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes_exist(self):
        """Test if Amenity has the expected attributes"""
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_default_attribute_values(self):
        """Test if Amenity attributes have default values"""
        self.assertEqual(Amenity.name, "")

    def test_attribute_types(self):
        """Test if Amenity attributes have the correct types"""
        self.assertIsInstance(Amenity.name, str)

if __name__ == "__main__":
    unittest.main()
