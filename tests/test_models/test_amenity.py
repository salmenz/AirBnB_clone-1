Learn more or give us feedback
#!/usr/bin/python3
"""
Unittest for class Amenity
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Test cases for class Amenity"""
    def setUp(self):
        """
        Create a new instance of Amenity before each test
        """
        self.amenity = Amenity()

    def tearDown(self):
        """
        Delete Amenity instance
        """
        del self.amenity

    def test_ID(self):
        """
        Make that the ID is unique
        """
        amenity2 = Amenity()
        self.assertNotEqual(self.amenity.id, amenity2.id)

    def test_id_type(self):
        """
        Make sure that the type of id is a string
        """
        self.assertEqual(type(self.amenity.id), str)

    def test_created_at_type(self):
        """
        Make sure that the type of created_at is Datetime
        """
        self.assertEqual(type(self.amenity.created_at), datetime)

    def test_updated_at_type(self):
        """
        Make sure that the type of updated_at is Datetime
        """
        self.assertEqual(type(self.amenity.updated_at), datetime)

    def test_name_type(self):
        """
        Make sure name is string
        """
        self.assertEqual(type(Amenity.name), str)

    def test_save(self):
        """
        Make sure that save update the updated_at
        """
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_str(self):
        """
        Testing return of str
        """
        self.assertEqual(str(self.amenity), "[Amenity] ({}) {}".
                         format(self.amenityid, self.amenity.__dict__))

    def test_to_dict(self):
        """
        Make sure to_dict returns is right dictionary
        """
        model_json = self.amenity.to_dict()
        self.assertEqual(type(model_json), dict)
        self.assertTrue(hasattr(model_json, '__class__'))
        self.assertEqual(type(model_json['created_at']), str)
        self.assertEqual(type(model_json['updated_at']), str)

    def test_kwargs(self):
        """
        Test passing kwargs
        """
        json_dict = self.amenity.to_dict()
        amenity2 = Amenity(**json_dict)
        self.assertEqual(self.amenity.id, amenity2.id)
        self.assertEqual(self.amenity.created_at, amenity2.created_at)
        self.assertEqual(self.amenity.updated_at, amenity2.updated_at)
        self.assertNotEqual(self.amenity, amenity2)
