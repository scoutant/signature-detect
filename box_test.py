import unittest
from craft import is_corner,is_nw,is_se

class BoxTest(unittest.TestCase):

    def test_photologo(self):
        box = [[0.82584153, 0.79851147], [0.89945924, 0.83282135], [0.8927885, 0.91054388], [0.81917073, 0.876234]]  # photologo-1-1.jpg
        self.assertTrue(is_corner(box))

    def test_not_nw(self):
        box = [[0.0, 0.0], [0.2, 0.0], [0.2, 0.3], [0.0, 0.3]] # not entirely fitting in corner
        self.assertFalse(is_nw(box))
        self.assertFalse(is_corner(box))

    def test_not_se(self):
        box = [[0.6, 0.6], [1.0, 0.6], [1.0, 1.0], [0.6, 1.0]] # not entirely fitting in corner
        self.assertFalse(is_se(box))
        self.assertFalse(is_corner(box))

