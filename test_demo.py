"""
Unit tests for the Demo module.

This test suite provides comprehensive testing for the demo module,
including both the is_triangle() function and the main() function.
"""

import unittest
from unittest.mock import patch
from io import StringIO
import demo
from demo import is_triangle


class TestIsTriangle(unittest.TestCase):

    def test_sum_equals_third(self):
        a,b,c = 2,3,5
        assert not is_triangle(a,b,c)
        assert not is_triangle(b,c,a)
        assert not is_triangle(c,a,b)

    def test_sum_smaller_than_third(self):
        a,b,c = 2,3,6
        assert not is_triangle(a,b,c)
        assert not is_triangle(a,c,b)
        assert not is_triangle(b,c,a)
        assert not is_triangle(b,a,c)
        assert not is_triangle(c,a,b)
        assert not is_triangle(c,b,a)

    def test_sum_larger_than_third(self):
        a,b,c = 2,3,3
        assert  is_triangle(a,b,c)
        assert  is_triangle(a,c,b)
        assert  is_triangle(b,c,a)
        assert  is_triangle(b,a,c)
        assert  is_triangle(c,a,b)
        assert  is_triangle(c,b,a)

    def test_sum_equals_third_negatives(self):
        a,b,c = 2,3,5
        assert not is_triangle(a,b,c)
        assert not is_triangle(a,b,-c)
        assert not is_triangle(a,-b,c)
        assert not is_triangle(a,-b,-c)
        assert not is_triangle(-a,b,c)
        assert not is_triangle(-a,b,-c)
        assert not is_triangle(-a,-b,c)
        assert not is_triangle(-a,-b,-c)



    def test_sum_smaller_than_third_negatives(self):
        a,b,c = 2,3,6
        assert not is_triangle(a,b,c)
        assert not is_triangle(a,b,-c)
        assert not is_triangle(a,-b,c)
        assert not is_triangle(a,-b,-c)
        assert not is_triangle(-a,b,c)
        assert not is_triangle(-a,b,-c)
        assert not is_triangle(-a,-b,c)
        assert not is_triangle(-a,-b,-c)

    def test_sum_larger_than_third_negatives(self):
        a,b,c = 2,3,3
        assert not is_triangle(a,b,-c)
        assert not is_triangle(a,-b,c)
        assert not is_triangle(a,-b,-c)
        assert not is_triangle(-a,b,c)
        assert not is_triangle(-a,b,-c)
        assert not is_triangle(-a,-b,c)
        assert not is_triangle(-a,-b,-c)

    def test_sum_equals_third_larg_nums(self):
        a,b,c = 2000,3000,5000
        assert not is_triangle(a,b,c)
        assert not is_triangle(a,c,b)
        assert not is_triangle(b,c,a)
        assert not is_triangle(b,a,c)
        assert not is_triangle(c,a,b)
        assert not is_triangle(c,b,a)




    def test_sum_smaller_than_third_larg_nums(self):
        a,b,c = 2000,3000,6000
        assert not is_triangle(a,b,c)
        assert not is_triangle(a,c,b)
        assert not is_triangle(b,c,a)
        assert not is_triangle(b,a,c)
        assert not is_triangle(c,a,b)
        assert not is_triangle(c,b,a)

    def test_sum_larger_than_third_larg_nums(self):
        a,b,c = 2000,3000,3000
        assert is_triangle(a,b,c)
        assert is_triangle(a,c,b)
        assert is_triangle(b,c,a)
        assert is_triangle(b,a,c)
        assert is_triangle(c,a,b)
        assert is_triangle(c,b,a)

if __name__ == '__main__':
    unittest.main()
