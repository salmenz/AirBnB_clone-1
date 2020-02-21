#!/usr/bin/python3
"""
Unittest for class State
"""
import unittest
from models.base_model import BaseModel
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """Test cases for State"""
    def setUp(self):
        """
        Create a new instance of State
        """
        self.state = State()

    def tearDown(self):
        """
        Delete State instance
        """
        del self.state

    def test_ID(self):
        """
        Make sure that ID is unique
        """
        state2 = State()
        self.assertNotEqual(self.state.id, state2.id)

    def test_id_type(self):
        """
        Make sure id is a string
        """
        self.assertEqual(type(self.state.id), str)

    def test_created_at_type(self):
        """
        Make sure that the type of created_at is Datetime
        """
        self.assertEqual(type(self.state.created_at), datetime)

    def test_updated_at_type(self):
        """
        Make sure that the type of updated_at is Datetime
        """
        self.assertEqual(type(self.state.updated_at), datetime)

    def test_name_type(self):
        """
        Make sure name is string
        """
        self.assertEqual(type(State.name), str)

    def test_save(self):
        """
        Make sure taht save update the updated_at
        """
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)

    def test_str(self):
        """
        Testing return of str
        """
        self.assertEqual(str(self.state), "[State] ({}) {}".
                         format(self.state.id, self.state.__dict__))

    def test_to_dict(self):
        """
        Make sure to_dict returns is right dictionary
        """
        model_json = self.state.to_dict()
        self.assertEqual(type(model_json), dict)
        self.assertTrue(hasattr(model_json, '__class__'))
        self.assertEqual(type(model_json['created_at']), str)
        self.assertEqual(type(model_json['updated_at']), str)

    def test_kwargs(self):
        """
        Test passing kwargs
        """
        json_dict = self.state.to_dict()
        state2 = State(**json_dict)
        self.assertEqual(self.state.id, state2.id)
        self.assertEqual(self.state.created_at, state2.created_at)
        self.assertEqual(self.state.updated_at, state2.updated_at)
        self.assertNotEqual(self.state, state2)
