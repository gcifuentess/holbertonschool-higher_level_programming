"""Test Square Module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from contextlib import redirect_stdout
import io


class testSquare(unittest.TestCase):
    """Rectangle test class"""

    initial_ids = 0

    def check_initial_ids(self):
        """checks if there are ids already initialized"""
        if '_Base__nb_objects' in dir(Square):
            type(self).initial_ids = Square.__dict__['_Base__nb_objects'] - 1

    def setUp(self):
        """creates a Rectangle with the minum args"""
        self.sq_0 = Square(2)

    def test_00_is_Rectangle_class(self):
        """test if square inherits from Rectangle class"""
        self.check_initial_ids()
        self.assertTrue(issubclass(type(self.sq_0), Rectangle) and
                        type(self.sq_0) != Rectangle)

    def test_01_id(self):
        """test the correct creation of the id of the new instance"""
        self.assertEqual(self.sq_0.id, 2 + self.initial_ids)

    def test_02_square_attributes(self):
        """test the correct creation of the attributes of the new instance
           with default arguments
        """
        self.assertEqual(self.sq_0.width, 2)
        self.assertEqual(self.sq_0.height, 2)
        self.assertEqual(self.sq_0.x, 0)
        self.assertEqual(self.sq_0.y, 0)

    def test_03_square_attributes_with_args(self):
        """test the correct creation of the attributes of the new instance
           with custom arguments
        """
        sq_1 = Square(4, 1, 2, -5)
        self.assertEqual(sq_1.width, 4)
        self.assertEqual(sq_1.height, 4)
        self.assertEqual(sq_1.x, 1)
        self.assertEqual(sq_1.y, 2)
        self.assertEqual(sq_1.id, -5)

    def test_04_square_id_after_serveral_instances(self):
        """test the correct creation of the id of a new square
           after the creation of several previous instances
        """
        self.assertEqual(self.sq_0.id, 5 + self.initial_ids)

    def test_05_size_integer(self):
        """test if size is integer"""
        with self.assertRaises(TypeError):
            sq = Square('a')

    def test_06_size_less_than_1(self):
        """test if size is less than 1"""
        with self.assertRaises(ValueError):
            sq = Square(0)

    def test_07_x_integer(self):
        """test if x is integer"""
        with self.assertRaises(TypeError):
            sq = Square(1, 'a')  # id 9

    def test_08_x_less_than_0(self):
        """test if x is less than 0"""
        with self.assertRaises(ValueError):
            sq = Square(2, -1)  # id 11

    def test_09_y_integer(self):
        """test if y is integer"""
        with self.assertRaises(TypeError):
            sq = Square(1, 0, 'a')  # id 13

    def test_10_y_integer(self):
        """test if y is less than 0"""
        with self.assertRaises(ValueError):
            sq = Square(1, 0, -1)  # id 15

    def test_11_area_no_args(self):
        """test the area of square with minimum args"""
        self.assertEqual(self.sq_0.area(), 4)

    def test_12_area_full_args(self):
        """test the area of square with minimum args"""
        sq = Square(4, 1, 2, -5)  # id -5
        self.assertEqual(sq.area(), 16)

    def test_13_square_display_1(self):
        """test the printing of a 2 * 2 square"""
        sq = Square(2)  # id 19
        screen = io.StringIO()
        with redirect_stdout(screen):
            sq.display()
        self.assertEqual(screen.getvalue()[:-1], "##\n##")

    def test_14_square_display_2(self):
        """test the printing of a 5 * 5 rectangle"""
        sq = Square(5)  # id 21
        screen = io.StringIO()
        with redirect_stdout(screen):
            sq.display()
        self.assertEqual(screen.getvalue()[:-1], "#####\n#####\n#####\n" +
                         "#####\n#####")

    def test_15_square_str_1(self):
        """test the value of __str__ full args"""
        sq = Square(4, 1, 2, -5)
        str_test = "[Square] (-5) 1/2 - 4"
        str_org = sq.__str__()
        self.assertEqual(str_org, str_test)

    def test_16_square_str_2(self):
        """test the value of __str__ minimun args"""
        sq = Square(3)  # id 24
        str_test = "[Square] ({}) 0/0 - 3".format(24 + self.initial_ids)
        str_org = sq.__str__()
        self.assertEqual(str_org, str_test)

    def test_17_square_display_3(self):
        """test the printing of a 2 * 2 square with x=4, y=5"""
        sq = Square(2, 4, 5)
        screen = io.StringIO()
        with redirect_stdout(screen):
            sq.display()
        self.assertEqual(screen.getvalue()[:-1], "\n\n\n\n\n    ##\n    ##")

    def test_18_update_method(self):
        """test the update method"""
        sq = Square(1, 1, 1, 20)
        str_test = "[Square] (20) 1/1 - 1"
        str_org = sq.__str__()
        self.assertEqual(str_org, str_test)

        """test update 1 *arg"""
        sq.update(21)
        str_test = "[Square] (21) 1/1 - 1"
        str_org = sq.__str__()
        self.assertEqual(str_org, str_test)

        """test update 2 *arg"""
        sq.update(22, 2)
        str_test = "[Square] (22) 1/1 - 2"
        str_org = sq.__str__()
        self.assertEqual(str_org, str_test)

        """test update full *arg"""
        sq.update(23, 1, 3, 4)
        str_test = "[Square] (23) 3/4 - 1"
        str_org = sq.__str__()
        self.assertEqual(str_org, str_test)

        """test update full *arg wrong arg"""
        with self.assertRaises(TypeError):
            sq.update(23, 'a', 3, 4)

        """test update full *arg wrong arg"""
        with self.assertRaises(ValueError):
            sq.update(23, -5, 3, 4)

        """test update full *arg wrong second arg"""
        with self.assertRaises(TypeError):
            sq.update(23, 1, 'a', 4)

    def test_19_update_method_kwargs(self):
        """test the update method with kwargs"""

        sq = Square(1, 1, 1, 30)
        str_test = "[Square] (30) 1/1 - 1"
        str_org = sq.__str__()
        self.assertEqual(str_org, str_test)

        """test update 1 *arg, 1 **kwarg"""
        sq.update(31, size=2)
        str_test = "[Square] (31) 1/1 - 1"
        str_org = sq.__str__()
        self.assertEqual(str_org, str_test)

        """test update 5 **kwarg"""
        sq.update(size=2, id=32, y=4, x=5)
        str_test = "[Square] (32) 5/4 - 2"
        str_org = sq.__str__()
        self.assertEqual(str_org, str_test)

    def test_20_dictionary_1(self):
        """test to_dictionary method v1"""
        sq = Square(1, 3, 4, 41)
        this_dict = sq.to_dictionary()
        expected_dict = {'size': 1, 'x': 3, 'y': 4, 'id': 41}
        self.assertEqual(this_dict, expected_dict)

    def test_21_dictionary_2(self):
        """test to_dictionary method v2"""
        sq = Square(4, 2, 1, 42)
        this_dict = sq.to_dictionary()
        expected_dict = {'y': 1, 'id': 42, 'x': 2, 'size': 4}
        self.assertEqual(this_dict, expected_dict)
