#!/usr/bin/python3
"""Unittest for class City
"""
import unittest
from models.base_model import BaseModel
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """Test cases for City"""
    def setUp(self):
        """
        Create a new instance of City
        """
        self.city = City()

    def tearDown(self):
        """
        Delete City instance
        """
        del self.city

    def test_ID(self):
        """
        Make sure taht the ID is unique
        """
        city2 = City()
        self.assertNotEqual(self.city.id, city2.id)

    def test_id_type(self):
        """
        Make sure id is a string
        """
        self.assertEqual(type(self.city.id), str)

    def test_created_at_type(self):
        """
        Make sure that the type of created_at is Datetime
        """
        self.assertEqual(type(self.city.created_at), datetime)

    def test_updated_at_type(self):
        """
        Make sure that the type of updated_at is Datetime
        """
        self.assertEqual(type(self.city.updated_at), datetime)

    def test_name_type(self):
        """
        Make sure name is string
        """
        self.assertEqual(type(City.name), str)

    def test_state_id_type(self):
        """
        Make sure state_id is string
        """
        self.assertEqual(type(City.state_id), str)

    def test_save(self):
        """
        Make sure that save update the updated_at
        """
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)

    def test_str(self):
        """
        Testing return of str
        """
        self.assertEqual(str(self.city), "[City] ({}) {}".
                         format(self.city.id, self.city.__dict__))

    def test_to_dict(self):
        """
        Make sure to_dict returns is right dictionary
        """
        model_json = self.city.to_dict()
        self.assertEqual(type(model_json), dict)
        self.assertTrue(hasattr(model_json, '__class__'))
        self.assertEqual(type(model_json['created_at']), str)
        self.assertEqual(type(model_json['updated_at']), str)

    def test_kwargs(self):
        """
        Test passing kwargs
        """
        json_dict = self.city.to_dict()
        city2 = City(**json_dict)
        self.assertEqual(self.city.id, city2.id)
        self.assertEqual(self.city.created_at, city2.created_at)
        self.assertEqual(self.city.updated_at, city2.updated_at)
        self.assertNotEqual(self.city, city2)
