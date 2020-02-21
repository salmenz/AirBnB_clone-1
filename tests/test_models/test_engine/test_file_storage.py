#!/usr/bin/python3
"""
Unittest for class FileStorage
"""
import unittest
import models
from models.state import State
from models.city import City
from models import storage
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage"""
    def setUp(self):
        """Store objects in variable"""
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path

    def test_objects(self):
        """Test the type of objects"""
        self.assertTrue(isinstance(self.objects, dict))

    def test_file_path(self):
        """Test the type of file_path"""
        self.assertTrue(isinstance(self.file_path, str))

    def test_new(self):
        """Test new one"""
        base = BaseModel()
        len = len(self.objects)
        models.storage.new(base)
        self.assertTrue(len == len(self.objects))

    def test_reload(self):
        """Test reload"""
        self.assertTrue(isinstance(self.objects, dict))

    def test_all(self):
        """Test reload"""
        self.assertTrue(isinstance(self.objects, dict))

class TestBaseModelFileStorage(unittest.TestCase):
    """Test BaseModel"""
    def setUp(self):
        """
        Create a new instance of BaseModel and store private
        attributes in more readable attribute names
        """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.base = BaseModel()
        self.base.save()

    def test_basemodel_object_update(self):
        """Test whether new BaseModel objects get added to the objects"""
        self.assertIn('BaseModel.{}'.format(self.base.id), self.objects.keys())

    def test_basemodel_dict(self):
        """Test if the new BaseModel objects dict get added to the objects"""
        base_dict = self.base.to_dict()
        self.assertIn(base_dict, self.objects.values())


class TestUserFileStorage(unittest.TestCase):
    """Test User"""
    def setUp(self):
        """
        Create a new instance of User and store private
        attributes in more readable attribute names
        """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.user = User()
        self.user.save()

    def test_user_object_update(self):
        """Test whether new User objects get added to objects"""
        self.assertIn('User.{}'.format(self.user.id), self.objects.keys())

    def test_user_dict(self):
        """Test whether new User objects dict get added to objects"""
        user_dict = self.user.to_dict()
        self.assertIn(user_dict, self.objects.values())


class TestStateFileStorage(unittest.TestCase):
    """Test State"""
    def setUp(self):
        """
        Create a new instance of State object and store private
        attributes in more readable attribute names
        """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.state = State()
        self.state.save()

    def test_state_object_update(self):
        """Test whether new State objects get added to objects"""
        self.assertIn('State.{}'.format(self.state.id), self.objects.keys())

    def test_state_dict(self):
        """Test whether new State objects dict get added to objects"""
        state_dict = self.state.to_dict()
        self.assertIn(state_dict, self.objects.values())


class TestCityFileStorage(unittest.TestCase):
    """Test City"""
    def setUp(self):
        """
        Create a new instance of City object and store private
        attributes in more readable attribute names
        """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.city = City()
        self.city.save()

    def test_city_object_update(self):
        """Test whether new City objects get added to objects"""
        self.assertIn('City.{}'.format(self.city.id), self.objects.keys())

    def test_city_dict(self):
        """Test whether new City objects dict get added to objects"""
        city_dict = self.city.to_dict()
        self.assertIn(city_dict, self.objects.values())


class TestAmenityFileStorage(unittest.TestCase):
    """Test Amenity"""
    def setUp(self):
        """
        Create a new instance of Amenity object and store private
        attributes in more readable attribute names
        """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.amenity = Amenity()
        self.amenity.save()

    def test_amenity_object_update(self):
        """Test whether new Amenity objects get added to objects"""
        self.assertIn('Amenity.{}'.format(self.amenity.id), self.objects.keys())

    def test_amenity_dict(self):
        """Test whjether new Amenity objects dict get added to objects"""
        amenity_dict = self.amenty.to_dict()
        self.assertIn(amenity_dict, self.objects.values())


class TestPlaceFileStorage(unittest.TestCase):
    """Test Place"""
    def setUp(self):
        """
        Create a new instance of Place object and store private
        attributes in more readable attribute names
        """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.place = Place()
        self.place.save()

    def test_place_object_update(self):
        """Test whether new Place objects get added to objects"""
        self.assertIn('Place.{}'.format(self.place.id), self.objects.keys())

    def test_place_dict(self):
        """Test whether new Place objects dict get added to objects"""
        place_dict = self.place.to_dict()
        self.assertIn(place_dict, self.objects.values())


class TestReviewFileStorage(unittest.TestCase):
    """Test Review"""
    def setUp(self):
        """
        Create a new instance of Review object and store private
        attributes in more readable attribute names
        """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.review = Review()
        self.review.save()

    def test_review_object_update(self):
        """Test whether new Review objects get added to objects"""
        self.assertIn('Review.{}'.format(self.review.id), self.objects.keys())

    def test_review_dict(self):
        """Test whether new Review objects dict get added to objects"""
        review_dict = self.review.to_dict()
        self.assertIn(review_dict, self.objects.values())
