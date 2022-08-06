#!/usr/bin/python3
<<<<<<< HEAD
"""
Contains the TestCityDocs classes
from datetime import datetime
import inspect
from models import city
"""

from models.base_model import BaseModel
import pep8
import unittest
City = city.City


class TestCityDocs(unittest.TestCase):
    """Tests to check the documentation and style of City class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_f = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_city(self):
        """Test that models/city.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """Test that tests/test_models/test_city.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_city_module_docstring(self):
        """Test for the city.py module docstring"""
        self.assertIsNot(city.__doc__, None,
                         "city.py needs a docstring")
        self.assertTrue(len(city.__doc__) >= 1,
                        "city.py needs a docstring")

    def test_city_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")

    def test_city_func_docstrings(self):
        """Test for the presence of docstrings in City methods"""
        for func in self.city_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

class TestCity(unittest.TestCase):
    """Test the City class"""
    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_name_attr(self):
        """Test that City has attribute name, and it's an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

    def test_state_id_attr(self):
        """Test that City has attribute state_id, and it's an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        c = City()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in c.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        c = City()
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "City")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))
=======
"""Unittest for City class"""
import unittest
from models.city import City
from models.base_model import BaseModel
import os


class TestCity(unittest.TestCase):
    """Runs tests for City class"""

    def setUp(self):
        """Sets up the testing environment"""

        self.c1 = City()
        self.c2 = City()
        self.c2.name = "Santa_Cruz"

    def tearDown(self):
        """Breaks down the testing environment"""

        del self.c1
        del self.c2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_checks_attributes(self):
        """Checks for class specific attributes"""

        self.assertTrue(hasattr(City(), "state_id"))
        self.assertTrue(hasattr(City(), "name"))

    def test_new_instances(self):
        """Checks that new instances were created"""

        self.assertTrue(self.c1)
        self.assertTrue(self.c2)

    def test_new_instances_attribute_creation(self):
        """Checks that new instances have designated attributes"""

        self.assertIn("name", self.c2.__dict__)
        self.assertEqual(self.c2.name, "Santa_Cruz")

    def test_non_existant_instance(self):
        """Checks for a non-existant instance"""

        self.c3 = City()
        self.assertIsInstance(self.c3, City)

    def test_inheritence(self):
        """Checks to make sure City inherits from BaseModel"""

        self.assertTrue(issubclass(City, BaseModel))
>>>>>>> 2c031bb630f646cc8dd04934e2bdbc26467c3763
