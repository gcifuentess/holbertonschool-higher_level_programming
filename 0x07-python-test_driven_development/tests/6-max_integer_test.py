#!/usr/bin/python3
"""Unittest for max_integer()"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer"""
    def test_no_arg(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([98]), 98)

    def test_identical(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_start(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_ordered(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_ordered_larger(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]), 20)

    def test_unordered(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_unordered_larger(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([23, 58, 91, 24, 1024, 89, 98,
                                     108, 256, 512]), 1024)

    def test_positives_and_negatives(self):
        """Unittest for max_integer"""
        self.assertEqual(
            max_integer([-23, 58, 91, 24, -1024, 89, 98, 108, -256, -512]),
            108)

    def test_positives_and_negatives_large(self):
        """Unittest for max_integer"""
        self.assertEqual(
            max_integer(
                [7474, -2513, 5721, 2319, 74, 7946, -5544, 7693, -7013,
                 -6683, 715, -8738, 9678, -1081, 4730, -1376, 9126,
                 -8394, 9732, 1695, -4932, -2100, -6920, 2219, -7319,
                 -1193, -422, 9312, 9508, -2690, -9206, 4461, 2997, -6753,
                 -7824, 3097, 1681, 3401, 7221, 1758, -1990, 4958, 4347,
                 7054, 545, 3492, -7285, -1672, 2230, -4576, -3121,
                 -6736, -537, 9823, 4281, -8003, 327, 1824, -1973, -9844,
                 29, 3596, 1108, 6702, 4873, -9452, -5949, -9640, -2156,
                 -4104, 5772, 5121, -2186, -4870, -4116, 6443, -9381,
                 -9388, 8552, 3582, 3500, 7924, 211, -2976, 6346, -5405,
                 899, -3432, -2550, -3353, 6944, 9623]), 9823)

    def test_negatives(self):
        """Unittest for max_integer"""
        self.assertEqual(
            max_integer(
                [-967891, -4663691, -71562, -7153670, -8038202,
                 -7893047, -9350883, -1132134, -3675971, -8495354,
                 -9158229, -9310087, -6319598, -8961209, -4906000,
                 -386471, -639929, -2676965, -6881679, -6258057,
                 -5490677, -1107298, -4199148, -5933601, -9917695,
                 -7759849, -7045734, -4885806, -9485075, -5119579,
                 -5272933, -4952516, -6115545, -8333464, -7271456,
                 -4097027, -4342575, -8400559, -8235052, -4373818,
                 -8054214, -8565596, -639225, -2292452, -4269529,
                 -7202853, -6891036, -4379807, -7955196, -1536591,
                 -2839083, -2586661, -9941097, -3136620]), -71562)

    def test_ints_and_floats(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [10, 99.8, -100, -0.1, 1000, 9999, -100000, 9998.9]), 9999)

    def test_ints_and_floats_large(self):
        """Unittest for max_integer"""
        self.assertEqual(
            max_integer(
                [120549.90322580645, 30889.777777777777, 986136.4,
                 393382.5416666667, 15441.826086956522, 2503567,
                 176118.87179487178, 372359.4, 142747.61538461538,
                 128534.875, 61069.433333333334, 37142.71951219512,
                 51481.13114754098, 571618.5, 35977.166666666664,
                 142333.11764705883, 199123.75]), 2503567)

    def test_floats(self):
        """Unittest for max_integer"""
        self.assertEqual(
            max_integer(
                [.02345, .23423434, .45675674, .678678,
                 .867090, .74653, .5745375]), 0.86709)

    def test_floats_large(self):
        """Unittest for max_integer"""
        self.assertEqual(
            max_integer(
                [17.269673745943177, 7.040663644666581,
                 0.47120480947220955, 2.5056796257122915,
                 1.3349487122618868, 0.08451917751917885,
                 1.0157082402123356, 29.496355326217376,
                 10.171800729369348, 1.1263544935158727,
                 0.47572929035550277, 3.712323073375754,
                 0.5742929278531704, 0.43940976988732966,
                 0.09537099783126887, 1.4936141049902174,
                 0.20607476376994402, 0.9497689034126077,
                 2.1498649449691807]), 29.496355326217376)

    def test_numeric_string(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer("192834754"), "9")

    def test_string(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_lists(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_str_list(self):
        """Unittest for max_integer"""
        self.assertEqual(
            max_integer([["test_1"], ["test_2"], ["abc"], ["def"], ["ghi"]]),
            ["test_2"])

    def test_inf(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([99, 1e30000, 1e30000]),
                         1e30000)

    def test_nan(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([99, float('nan'), 100]), 100)

    def test_mixed_list(self):
        """Unittest for max_integer"""
        with self.assertRaises(TypeError):
            max_integer([[], [2], [4], [2, 9], 99, "test"])

    def test_mixed_list_int_str(self):
        """Unittest for max_integer"""
        with self.assertRaises(TypeError):
            max_integer([99, "test"])

    def test_none(self):
        """Unittest for max_integer"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_dict(self):
        """Unittest for max_integer"""
        with self.assertRaises(TypeError):
            max_integer([{20: 23, 14: 45}, {"a": "b"}])

    def test_int(self):
        """Unittest for max_integer"""
        with self.assertRaises(TypeError):
            max_integer(98)

    def test_float(self):
        """Unittest for max_integer"""
        with self.assertRaises(TypeError):
            max_integer(9.8)

if __name__ == '__main__':
    unittest.main()
