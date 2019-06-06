import unittest
from jigsawpy import geom
from matplotlib.path import Path


class MeshBoundariesTestCase(unittest.TestCase):

    def setUp(self):
        self.OuterRing = Path([[0., 0.],
                               [3., 0.],
                               [3., 3.],
                               [0., 3.]], closed=True)
        self.InnerRings = [Path([[1., 1.],
                                 [2., 1.],
                                 [2., 2.],
                                 [1., 2.]], closed=True)]

    def test_empty(self):
        with self.assertRaises(TypeError) as context:
            geom._MeshBoundaries()
        self.assertTrue(
            "__init__() missing 1 required positional argument: 'OuterRing'"
            in str(context.exception))

    def test_init_OuterRing_wrong_type(self):
        with self.assertRaises(TypeError) as context:
            geom._MeshBoundaries(object)
        self.assertTrue(
                    "OuterRing must be of type <class 'matplotlib.path.Path'>"
                    in str(context.exception))

    def test_init_InnerRings_wrong_type(self):
        with self.assertRaises(TypeError) as context:
            geom._MeshBoundaries(self.OuterRing, object)
        self.assertTrue(
                    "InnerRing must be of type <class 'matplotlib.path.Path'>"
                    in str(context.exception))

    def test_init(self):
        geom._MeshBoundaries(self.OuterRing, *self.InnerRings)
