#!/usr/bin/python3
"""
Unittest for class Review
"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """Test cases for Review"""
    def setUp(self):
        """
        Create a new instance of Review
        """
        self.review = Review()

    def tearDown(self):
        """
        Delete Review instance
        """
        del self.review

    def test_ID(self):
        """
        Make sure that the ID is unique
        """
        review2 = Review()
        self.assertNotEqual(self.review1.id, review2.id)

    def test_id_type(self):
        """
        Make sure id is a string
        """
        self.assertEqual(type(self.review.id), str)

    def test_created_at_type(self):
        """
        Make sure that the type of created_at is Datetime
        """
        self.assertEqual(type(self.review.created_at), datetime)

    def test_updated_at_type(self):
        """
        Make sure that the type of updated_at is Datetime
        """
        self.assertEqual(type(self.review.updated_at), datetime)

    def test_place_id(self):
        """
        Make sure place_id is string
        """
        self.assertEqual(type(Review.place_id), str)

    def test_user_id(self):
        """
        Make sure user_id is string
        """
        self.assertEqual(type(Review.user_id), str)

    def test_text(self):
        """
        Make sure text is string
        """
        self.assertEqual(type(Review.text), str)

    def test_save(self):
        """
        Make sure that save update the updated_at
        """
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(old_updated_at, self.review.updated_at)

    def test_str(self):
        """
        Testing return of str
        """
        self.assertEqual(str(self.review), "[Review] ({}) {}".
                         format(self.review.id, self.review.__dict__))

    def test_to_dict(self):
        """
        Make sure to_dict returns is right dictionary
        """
        model_json = self.review.to_dict()
        self.assertEqual(type(model_json), dict)
        self.assertTrue(hasattr(model_json, '__class__'))
        self.assertEqual(type(model_json['created_at']), str)
        self.assertEqual(type(model_json['updated_at']), str)

    def test_kwargs(self):
        """
        Test passing kwargs
        """
        json_dict = self.review.to_dict()
        review2 = Review(**json_dict)
        self.assertEqual(self.review.id, review2.id)
        self.assertEqual(self.review.created_at, review2.created_at)
        self.assertEqual(self.review.updated_at, review2.updated_at)
        self.assertNotEqual(self.review, review2)
