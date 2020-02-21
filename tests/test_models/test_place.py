#!/usr/bin/python3
"""Unittest for class Place
"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Test cases for Place"""
    def setUp(self):
        """
        Create a new instance of Place
        """
        self.place = Place()

    def tearDown(self):
        """
        Delete Place instance
        """
        del self.place

    def test_ID(self):
        """
        Make sure that the ID is unique
        """
        place2 = Place()
        self.assertNotEqual(self.place.id, place2.id)

    def test_id_type(self):
        """
        Make sure that the type of id is a string
        """
        self.assertEqual(type(self.place.id), str)

    def test_created_at_type(self):
        """
        Make sure that the type of created_at is Datetime
        """
        self.assertEqual(type(self.place.created_at), datetime)

    def test_updated_at_type(self):
        """
        Make sure that the type of the updated_at is Datetime
        """
        self.assertEqual(type(self.place.updated_at), datetime)

    def test_name_type(self):
        """
        Make sure name is string
        """
        self.assertEqual(type(Place.name), str)

    def test_city_id(self):
        """
        Make sure city_id is string
        """
        self.assertEqual(type(Place.city_id), str)

    def test_user_id(self):
        """
        Make sure user_id is string
        """
        self.assertEqual(type(Place.user_id), str)

    def test_description(self):
        """
        Make sure description is string
        """
        self.assertEqual(type(Place.description), str)

    def test_number_rooms(self):
        """
        Make sure number_rooms is integer
        """
        self.assertEqual(type(Place.number_rooms), int)

    def test_number_bathrooms(self):
        """
        Make sure number_bathrooms is integer
        """
        self.assertEqual(type(Place.number_bathrooms), int)

    def test_max_guest(self):
        """
        Make sure max_guest is integer
        """
        self.assertEqual(type(Place.max_guest), int)

    def test_price_by_night(self):
        """
        Make sure price_by_night is integer
        """
        self.assertEqual(type(Place.price_by_night), int)

    def test_latitutde(self):
        """
        Make sure latitude is float
        """
        self.assertEqual(type(Place.latitude), float)

    def test_longitude(self):
        """
        Make sure longitude is float
        """
        self.assertEqual(type(Place.longitude), float)

    def test_amenity_ids(self):
        """
        Make sure amenity_ids is a list
        """
        self.assertEqual(type(Place.amenity_ids), list)

    def test_save(self):
        """
        Make sure that save update the updated_at
        """
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(old_updated_at, self.place.updated_at)

    def test_str(self):
        """
        Testing return of str
        """
        self.assertEqual(str(self.place), "[Place] ({}) {}".
                         format(self.place.id, self.place.__dict__))

    def test_to_dict(self):
        """
        Make sure to_dict returns is right dictionary
        """
        model_json = self.place.to_dict()
        self.assertEqual(type(model_json), dict)
        self.assertTrue(hasattr(model_json, '__class__'))
        self.assertEqual(type(model_json['created_at']), str)
        self.assertEqual(type(model_json['updated_at']), str)

    def test_kwargs(self):
        """
        Test passing kwargs
        """
        json_dict = self.place.to_dict()
        place2 = Place(**json_dict)
        self.assertEqual(self.place.id, place2.id)
        self.assertEqual(self.place.created_at, place2.created_at)
        self.assertEqual(self.place.updated_at, place2.updated_at)
        self.assertNotEqual(self.place, place2)
