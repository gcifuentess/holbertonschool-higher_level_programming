#!/usr/bin/python3
"""Base Class Test Module"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTest(unittest.TestCase):
    """Class to test Base Module"""

    def test_0_base_no_arg(self):
        """Instance with default id 1"""
        self.first = Base()
        self.assertEqual(self.first.id, 1)

    def test_1_base_no_arg_2(self):
        """Instance with default id 2. New instance without args"""
        self.second = Base()
        self.assertEqual(self.second.id, 2)

    def test_2_base_arg(self):
        """Instance with custom id -5. New instance with arg == -5"""
        self.third = Base(-5)
        self.assertEqual(self.third.id, -5)

    def test_3_base_no_arg_3(self):
        """Instance with default id 3. New instance without args after
           an instance with args
        """
        self.fourth = Base()
        self.assertEqual(self.fourth.id, 3)

    def test_4_to_json_string(self):
        """to_json_string method test"""
        ex_dict = {'one': 1, 'two': 2, 'three': 3}
        str_dict = json.dumps([ex_dict])
        base_json = Base.to_json_string([ex_dict])
        self.assertEqual(base_json, str_dict)

        ex_dict_1 = {'one': 1, 'two': 2, 'three': 3}
        str_dict_1 = json.dumps([])
        base_json_1 = Base.to_json_string(ex_dict_1)
        self.assertEqual(base_json_1, str_dict_1)

        ex_dict_2 = None
        str_dict_2 = str([])
        base_json_2 = Base.to_json_string(ex_dict_2)
        self.assertEqual(base_json_2, str_dict_2)

    def test_5_json_string_to_file(self):
        """save_to_file method test"""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            test_str = file.read()

        dict_1 = r1.to_dictionary()
        dict_2 = r2.to_dictionary()
        expect_str = Base.to_json_string([dict_1, dict_2])
        self.assertEqual(test_str, expect_str)

        s1 = Square(10, 2, 8)
        s2 = Square(4)

        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as file:
            test_str_1 = file.read()

        dict_1 = s1.to_dictionary()
        dict_2 = s2.to_dictionary()
        expect_str_1 = Base.to_json_string([dict_1, dict_2])
        self.assertEqual(test_str_1, expect_str_1)

    def test_6_from_json_string(self):
        """from_json_string method test"""

        my_list = [{'one': 1, 'two': 2, 'three': 3},
                   {'four': 4, 'five': 5, 'six': 6}]

        my_JSON_str = json.dumps(my_list)
        my_JSON_list = json.loads(my_JSON_str)

        test_str = Base.to_json_string(my_list)
        test_JSON_list = Base.from_json_string(test_str)

        self.assertEqual(test_JSON_list, my_JSON_list)

        test_JSON_list_1 = Base.from_json_string(None)

        self.assertEqual(test_JSON_list_1, [])

        test_JSON_list_2 = Base.from_json_string("[]")

        self.assertEqual(test_JSON_list_2, [])

    def test_7_create(self):
        """create method test"""

        rect_list = [{'width': 5, 'height': 4, 'x': 3, 'y': 2, 'id': 41},
                     {'height': 5, 'id': 42}]
        sq_list = [{'size': 4, 'x': 3, 'y': 2, 'id': 43},
                   {'size': 5, 'id': 44, 'x': 2}]

        rect_0 = Rectangle.create(**(rect_list[0]))
        str_test = rect_0.__str__()
        str_expect = "[Rectangle] (41) 3/2 - 5/4"
        self.assertEqual(str_test, str_expect)

        rect_1 = Rectangle.create(**rect_list[1])
        str_test_1 = rect_1.__str__()
        str_expect_1 = "[Rectangle] (42) 0/0 - 1/5"
        self.assertEqual(str_test_1, str_expect_1)

        sq_0 = Square.create(**sq_list[0])
        str_test_2 = sq_0.__str__()
        str_expect_2 = "[Square] (43) 3/2 - 4"
        self.assertEqual(str_test_2, str_expect_2)

        sq_1 = Square.create(**sq_list[1])
        str_test_3 = sq_1.__str__()
        str_expect_3 = "[Square] (44) 2/0 - 5"
        self.assertEqual(str_test_3, str_expect_3)

    def test_8_load_from_file(self):
        """load_from_file method test"""

        rect_list = [{'width': 5, 'height': 4, 'x': 3, 'y': 2, 'id': 45},
                     {'height': 5, 'id': 46}]
        sq_list = [{'size': 4, 'x': 3, 'y': 2, 'id': 47},
                   {'size': 5, 'id': 48, 'x': 2}]

        r1 = Rectangle.create(**(rect_list[0]))
        r2 = Rectangle.create(**rect_list[1])
        Rectangle.save_to_file([r1, r2])

        sq1 = Square.create(**sq_list[0])
        sq2 = Square.create(**sq_list[1])
        Square.save_to_file([sq1, sq2])

        rect_list_test = Rectangle.load_from_file()
        square_list_test = Square.load_from_file()

        rect_0 = rect_list_test[0]
        str_test = rect_0.__str__()
        str_expect = "[Rectangle] (45) 3/2 - 5/4"
        self.assertEqual(str_test, str_expect)

        rect_1 = rect_list_test[1]
        str_test_1 = rect_1.__str__()
        str_expect_1 = "[Rectangle] (46) 0/0 - 1/5"
        self.assertEqual(str_test_1, str_expect_1)

        sq_0 = square_list_test[0]
        str_test_2 = sq_0.__str__()
        str_expect_2 = "[Square] (47) 3/2 - 4"
        self.assertEqual(str_test_2, str_expect_2)

        sq_1 = square_list_test[1]
        str_test_3 = sq_1.__str__()
        str_expect_3 = "[Square] (48) 2/0 - 5"
        self.assertEqual(str_test_3, str_expect_3)
