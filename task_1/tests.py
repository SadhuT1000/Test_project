import unittest
import math
from task_1.calculate import Circle, Triangle, get_area


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(1)
        self.assertAlmostEqual(get_area(circle), math.pi)

        circle = Circle(5)
        self.assertAlmostEqual(get_area(circle), math.pi * 25)

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(-1)
        with self.assertRaises(ValueError):
            Circle(0)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(get_area(triangle), 6.0)

        triangle = Triangle(5, 5, 5)
        self.assertAlmostEqual(get_area(triangle), 10.825317547305483)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 5)
        with self.assertRaises(ValueError):
            Triangle(-1, 2, 3)
        with self.assertRaises(ValueError):
            Triangle(0, 0, 0)

    def test_right_triangle(self):
        self.assertTrue(Triangle(3, 4, 5).is_right())
        self.assertTrue(Triangle(5, 12, 13).is_right())
        self.assertTrue(Triangle(7, 24, 25).is_right())

        self.assertFalse(Triangle(5, 5, 5).is_right())
        self.assertFalse(Triangle(5, 5, 7).is_right())

    def test_get_area_function(self):
        self.assertAlmostEqual(get_area(Circle(2)), math.pi * 4)
        self.assertAlmostEqual(get_area(Triangle(3, 4, 5)), 6.0)


if __name__ == '__main__':
    unittest.main()