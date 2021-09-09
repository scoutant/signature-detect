import unittest
from craft import detect
class DetectionTest(unittest.TestCase):

    def test_detection(self):
        self.assertTrue( detect( 'data/photologo-1-1.jpg') )

    def test_photologo_3(self):
        self.assertTrue( detect( 'data/photologo-3.jpg') ) # [0.79375001 0.78643433] [0.98125001 0.78643433] [0.98125001 0.94372123] [0.79375001 0.94372123]

    def test_no_detection(self):
        self.assertFalse( detect( 'data/sky.jpg') ) # no text at all

    def test_no_detection_ny(self):
        self.assertFalse( detect( 'data/times-square.jpg') ) # 10 text boxes, but no signature here : only text in the wild

