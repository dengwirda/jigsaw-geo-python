import unittest
from jigsawpy import Jigsaw, Geom


class JigsawTestCase(unittest.TestCase):

    def setUp(self):
        outer_vertices = [[0., 0.],
                          [3., 0.],
                          [3., 3.],
                          [0., 3.]]

        self.JigsawGeom2D = Geom(outer_vertices, 'euclidean_mesh')

        inner_vertices = [[1., 1.],
                          [2., 1.],
                          [2., 2.],
                          [1., 2.]]

        self.JigsawGeom2D.add_inner_vertices(inner_vertices, bound=False)

    def test_Jigsaw2D(self):
        _Jigsaw = Jigsaw(self.JigsawGeom2D)
        print(_Jigsaw)
