#!/usr/bin/python3
"""
Unittest for BaseModel
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel"""
    def setUp(self):
        """
        Create an instance of BaseModel
        """
        self.base = BaseModel()

    def tearDown(self):
        """
        Delete BaseModel instance
        """
        del self.base

    def test_ID(self):
        """
        Make sure all ID are unique
        """
        base2 = BaseModel()
        self.assertNotEqual(self.base.id, base2.id)

    def test_ID_type(self):
        """
        Make sure id is a string
        """
        self.assertEqual(type(self.base.id), str)

    def test_created_at_type(self):
        """
        Make sure created_at type is Datetime
        """
        self.assertEqual(type(self.base.created_at), datetime)

    def test_updated_at_type(self):
        """
        Make sure updated_at type is Datetime
        """
        self.assertEqual(type(self.base.updated_at), datetime)

    def test_save(self):
        """
        Make sure that save update the updated_at
        """
        old_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(old_updated_at, self.base.updated_at)

    def test_kwargs(self):
        """
        Test the kwargs passed to the BaseModel
        """
        json_dict = self.base.to_dict()
        base2 = BaseModel(**json_dict)
        self.assertEqual(self.base.id, base2.id)
        self.assertEqual(self.base.created_at, base2.created_at)
        self.assertEqual(self.base.updated_at, base2.updated_at)
        self.assertNotEqual(self.base, base2)

    def test_str(self):
        """
        Test the return of str
        """
        self.assertEqual(str(self.base), "[BaseModel] ({}) {}".
                         format(self.base.id, self.base.__dict__))

    def test_to_dict(self):
        """
        Make sure to_dict returns is right dictionary
        """
        model_json = self.base.to_dict()
        self.assertEqual(type(model_json), dict)
        self.assertTrue(hasattr(model_json, '__class__'))
        self.assertEqual(type(model_json['created_at']), str)
        self.assertEqual(type(model_json['updated_at']), str)

    def test_save2(self):
        """Tests the public instance method save()."""

        base = BaseModel()
        time.sleep(0.5)
        now = datetime.now()
        base.save()
        d = base.updated_at - now
        self.assertTrue(abs(d.total_seconds()) < 0.01)
