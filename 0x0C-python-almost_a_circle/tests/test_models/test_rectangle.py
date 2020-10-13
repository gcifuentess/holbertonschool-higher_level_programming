#!/usr/bin/python3
"""Rectangle Test Module"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
from contextlib import redirect_stdout


class testRectangle(unittest.TestCase):
    """Rectangle test class"""

    initial_ids = 0

    def check_initial_ids(self):
        """checks if there are ids already initialized"""
        if '_Base__nb_objects' in dir(Rectangle):
            nb_objs = Rectangle.__dict__['_Base__nb_objects'] - 1
            type(self).initial_ids = nb_objs

    def setUp(self):
        """creates a Rectangle with the minum args"""
        self.rect_0 = Rectangle(1, 1)

    def test_00_is_base_class(self):
        """test if rectangle inherits from Base class"""
        self.check_initial_ids()
        self.assertTrue(issubclass(type(self.rect_0), Base) and
                        type(self.rect_0) != Base)

    def test_01_width_is_private(self):
        """test if the width property is private"""
        self.assertTrue('_Rectangle__width' in
                        dir(self.rect_0))

    def test_02_height_is_private(self):
        """test if the height property is private"""
        self.assertTrue('_Rectangle__height' in
                        dir(self.rect_0))

    def test_03_x_is_private(self):
        """test if the x property is private"""
        # with self.assertRaises(AttributeError):
        #     print(self.rect_0.x)
        self.assertTrue('_Rectangle__x' in
                        dir(self.rect_0))

    def test_04_y_is_private(self):
        """test if the height property is private"""
        self.assertTrue('_Rectangle__y' in
                        dir(self.rect_0))

    def test_05_id(self):
        """test the correct creation of the id of the new instance"""
        self.assertEqual(self.rect_0.id, 6 + self.initial_ids)

    def test_06_rectangle_attributes(self):
        """test the correct creation of the attributes of the new instance
           with default arguments
        """
        self.assertEqual(self.rect_0.width, 1)
        self.assertEqual(self.rect_0.height, 1)
        self.assertEqual(self.rect_0.x, 0)
        self.assertEqual(self.rect_0.y, 0)

    def test_07_rectangle_attributes_with_args(self):
        """test the correct creation of the attributes of the new instance
           with custom arguments
        """
        self.rect_1 = Rectangle(4, 2, 1, 2, -5)
        self.assertEqual(self.rect_1.width, 4)
        self.assertEqual(self.rect_1.height, 2)
        self.assertEqual(self.rect_1.x, 1)
        self.assertEqual(self.rect_1.y, 2)
        self.assertEqual(self.rect_1.id, -5)

    def test_08_rectangle_id_after_serveral_instances(self):
        """test the correct creation of the id of a new rectangle
           after the creation of several previous instances
        """
        self.assertEqual(self.rect_0.id, 9 + self.initial_ids)

    def test_09_width_integer(self):
        """test if width is integer"""
        with self.assertRaises(TypeError):
            self.rect_2 = Rectangle('a', 1)

    def test_10_width_less_than_1(self):
        """test if width is less than 0"""
        with self.assertRaises(ValueError):
            self.rect_3 = Rectangle(-5, 1)

    def test_11_height_integer(self):
        """test if height is integer"""
        with self.assertRaises(TypeError):
            self.rect_4 = Rectangle(1, 'a')

    def test_12_height_less_than_1(self):
        """test if height is less than 0"""
        with self.assertRaises(ValueError):
            self.rect_5 = Rectangle(1, -5)

    def test_13_x_integer(self):
        """test if x is integer"""
        with self.assertRaises(TypeError):
            self.rect_6 = Rectangle(1, 1, 'a')

    def test_14_x_less_than_0(self):
        """test if x is less than 0"""
        with self.assertRaises(ValueError):
            self.rect_7 = Rectangle(1, 1, -5)

    def test_15_y_integer(self):
        """test if y is integer"""
        with self.assertRaises(TypeError):
            self.rect_8 = Rectangle(1, 1, 1, 'a')

    def test_16_y_integer(self):
        """test if y is less than 0"""
        with self.assertRaises(ValueError):
            self.rect_9 = Rectangle(1, 1, 1, -5)

    def test_17_area_no_args(self):
        """test the area of rectangle with minimum args"""
        self.assertEqual(self.rect_0.area(), 1)

    def test_18_area_full_args(self):
        """test the area of rectangle with minimum args"""
        self.rect_1 = Rectangle(4, 2, 1, 2, -5)
        self.assertEqual(self.rect_1.area(), 8)

    def test_19_rectangle_display_1(self):
        """test the printing of a 3 * 2 rectangle"""
        self.rect_10 = Rectangle(3, 2)
        screen = io.StringIO()
        with redirect_stdout(screen):
            self.rect_10.display()
        self.assertEqual(screen.getvalue()[:-1], "###\n###")

    def test_20_rectangle_display_2(self):
        """test the printing of a 5 * 10 rectangle"""
        self.rect_11 = Rectangle(5, 10)
        screen = io.StringIO()
        with redirect_stdout(screen):
            self.rect_11.display()
        self.assertEqual(screen.getvalue()[:-1], "#####\n#####\n#####\n" +
                         "#####\n#####\n#####\n#####\n#####\n#####\n#####")

    def test_21_rectangle_str_1(self):
        """test the value of __str__ full args"""
        rect_1 = Rectangle(4, 2, 1, 2, -5)
        str_test = "[Rectangle] (-5) 1/2 - 4/2"
        str_org = rect_1.__str__()
        self.assertEqual(str_org, str_test)

    def test_21_rectangle_str_2(self):
        """test the value of __str__ minimun args"""
        rect = Rectangle(2, 3)
        str_test = "[Rectangle] ({}) 0/0 - 2/3".format(34 + self.initial_ids)
        str_org = rect.__str__()
        self.assertEqual(str_org, str_test)

    def test_22_rectangle_display_3(self):
        """test the printing of a 3 * 2 rectangle with x=4, y=5"""
        rect = Rectangle(3, 2, 4, 5)
        screen = io.StringIO()
        with redirect_stdout(screen):
            rect.display()
        self.assertEqual(screen.getvalue()[:-1], "\n\n\n\n\n    ###\n    ###")

    def test_22_update_method(self):
        """test the update method"""
        rect = Rectangle(1, 1, 1, 1, 20)
        str_test = "[Rectangle] (20) 1/1 - 1/1"
        str_org = rect.__str__()
        self.assertEqual(str_org, str_test)

        """test update 1 *arg"""
        rect.update(21)
        str_test = "[Rectangle] (21) 1/1 - 1/1"
        str_org = rect.__str__()
        self.assertEqual(str_org, str_test)

        """test update 2 *arg"""
        rect.update(22, 2)
        str_test = "[Rectangle] (22) 1/1 - 2/1"
        str_org = rect.__str__()
        self.assertEqual(str_org, str_test)

        """test update full *arg"""
        rect.update(23, 1, 2, 3, 4)
        str_test = "[Rectangle] (23) 3/4 - 1/2"
        str_org = rect.__str__()
        self.assertEqual(str_org, str_test)

        """test update full *arg wrong arg"""
        with self.assertRaises(TypeError):
            rect.update(23, 'a', 2, 3, 4)

        """test update full *arg wrong arg"""
        with self.assertRaises(ValueError):
            rect.update(23, -5, 2, 3, 4)

        """test update full *arg wrong second arg"""
        with self.assertRaises(TypeError):
            rect.update(23, 1, 'a', 3, 4)

    def test_23_update_method_kwargs(self):
        """test the update method with kwargs"""

        rect = Rectangle(1, 1, 1, 1, 30)
        str_test = "[Rectangle] (30) 1/1 - 1/1"
        str_org = rect.__str__()
        self.assertEqual(str_org, str_test)

        """test update 1 *arg, 1 **kwarg"""
        rect.update(31, height=2)
        str_test = "[Rectangle] (31) 1/1 - 1/1"
        str_org = rect.__str__()
        self.assertEqual(str_org, str_test)

        """test update 5 **kwarg"""
        rect.update(height=2, id=32, width=3, y=4, x=5)
        str_test = "[Rectangle] (32) 5/4 - 3/2"
        str_org = rect.__str__()
        self.assertEqual(str_org, str_test)

    def test_24_dictionary_1(self):
        """test to_dictionary method v1"""
        rect = Rectangle(1, 2, 3, 4, 41)
        this_dict = rect.to_dictionary()
        expected_dict = {'width': 1, 'height': 2, 'x': 3, 'y': 4, 'id': 41}
        self.assertEqual(this_dict, expected_dict)

    def test_25_dictionary_2(self):
        """test to_dictionary method v2"""
        rect = Rectangle(4, 3, 2, 1, 42)
        this_dict = rect.to_dictionary()
        expected_dict = {'y': 1, 'height': 3, 'id': 42, 'x': 2, 'width': 4}
        self.assertEqual(this_dict, expected_dict)
