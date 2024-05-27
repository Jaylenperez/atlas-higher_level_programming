#!/usr/bin/python3

"""
Define unittest for base.py
"""

import unittest
from models.base import Base
import json
import os

class TestBase(unittest.TestCase):
    def setUp(self):
        """Reset __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_id_auto_increment(self):
        """Test that IDs auto-increment properly"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_provided(self):
        """Test that IDs are assigned correctly when provided"""
        b1 = Base(10)
        b2 = Base(20)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 20)

    def test_to_json_string_none(self):
        """Test to_json_string with None"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """Test to_json_string with an empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        """Test to_json_string with a valid list of dictionaries"""
        dict_list = [{"id": 1}, {"id": 2}]
        json_str = Base.to_json_string(dict_list)
        self.assertEqual(json.loads(json_str), dict_list)

    def test_save_to_file_none(self):
        """Test save_to_file with None"""
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Base.json")

    def test_save_to_file_empty_list(self):
        """Test save_to_file with an empty list"""
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Base.json")

    def test_save_to_file(self):
        """Test save_to_file with a valid list of Base objects"""
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        with open("Base.json", "r") as file:
            data = json.load(file)
            self.assertEqual(data, [{"id": 1}, {"id": 2}])
        os.remove("Base.json")

    def test_from_json_string_none(self):
        """Test from_json_string with None"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string"""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string(self):
        """Test from_json_string with a valid JSON string"""
        json_str = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(Base.from_json_string(json_str), [{"id": 1}, {"id": 2}])

    def test_create(self):
        """Test create method"""
        class Dummy(Base):
            def __init__(self, id=None):
                super().__init__(id)
            def update(self, id=None):
                self.id = id

        d = Dummy.create(id=1)
        self.assertEqual(d.id, 1)

    def test_load_from_file_no_file(self):
        """Test load_from_file when file doesn't exist"""
        instances = Base.load_from_file()
        self.assertEqual(instances, [])

    def test_load_from_file(self):
        """Test load_from_file with a valid file"""
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        instances = Base.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].id, 2)
        os.remove("Base.json")

if __name__ == '__main__':
    unittest.main()
