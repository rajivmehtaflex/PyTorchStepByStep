import unittest

class Gtest(unittest.TestCase):

    def setUp(self):
        self.bloodyhell='0'

    def test_start(self):
        self.assertIsNotNone(self.bloodyhell)

    def test_isString(self):
        self.assertIsInstance(self.bloodyhell,str)

if __name__=='__main__':
    unittest.main(argv=[''],verbosity=1,exit=False)