import unittest
from jigsawpy.cjigsaw.tests import test_1, \
                                   test_2, \
                                   test_3, \
                                   test_4, \
                                   test_5, \
                                   test_6


class CjigsawTestCase(unittest.TestCase):
    # Checks that return status code is 0.
    def test_1(self):
        assert test_1.main(verbosity=0) == 0

    def test_2(self):
        assert test_2.main(verbosity=0) == 0

    def test_3(self):
        assert test_3.main(verbosity=0) == 0

    def test_4(self):
        assert test_4.main(verbosity=0) == 0

    def test_5(self):
        assert test_5.main(verbosity=0) == 0

    def test_6(self):
        assert test_6.main(verbosity=0) == 0
