#!/usr/bin/python3
"""Unittest for class User
"""
import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test cases User"""
    def setUp(self):
        """
        Create a new instance of User
        """
        self.user = User()

    def tearDown(self):
        """
        Delete User instance
        """
        del self.user

    def test_ID(self):
        """
        Make that the ID is unique
        """
        user2 = User()
        self.assertNotEqual(self.user.id, user2.id)

    def test_IDtype(self):
        """
        Make sure that the type of id is a string
        """
        self.assertEqual(type(self.user.id), str)

    def test_created_at_type(self):
        """
        Make sure that the type of created_at is Datetime
        """
        self.assertEqual(type(self.user.created_at), datetime)

    def test_updated_at_type(self):
        """
        Make sure that the type of updated_at is Datetime
        """
        self.assertEqual(type(self.user.updated_at), datetime)

    def test_email_type(self):
        """
        Make sure email is string
        """
        self.assertEqual(type(User.email), str)

    def test_password_type(self):
        """
        Make sure password is string
        """
        self.assertEqual(type(User.password), str)

    def test_first_name_type(self):
        """
        Make sure first_name is string
        """
        self.assertEqual(type(User.first_name), str)

    def test_last_name_type(self):
        """
        Make sure last_name is string
        """
        self.assertEqual(type(User.last_name), str)

    def test_save(self):
        """
        Make sure that save update the updated_at
        """
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)

    def test_str(self):
        """
        Testing return of str
        """
        self.assertEqual(str(self.user), "[User] ({}) {}".
                         format(self.user.id, self.user.__dict__))

    def test_to_dict(self):
        """
        Make sure to_dict returns is right dictionary
        """
        model_json = self.user.to_dict()
        self.assertEqual(type(model_json), dict)
        self.assertTrue(hasattr(model_json, '__class__'))
        self.assertEqual(type(model_json['created_at']), str)
        self.assertEqual(type(model_json['updated_at']), str)

    def test_kwargs(self):
        """
        Test passing kwargs
        """
        json_dict = self.user.to_dict()
        user2 = User(**json_dict)
        self.assertEqual(self.user.id, user2.id)
        self.assertEqual(self.user.created_at, user2.created_at)
        self.assertEqual(self.user.updated_at, user2.updated_at)
        self.assertNotEqual(self.user, user2)
