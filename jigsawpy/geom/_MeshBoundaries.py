from jigsawpy.geom._JigsawGeom2D import _JigsawGeom2D
from matplotlib.path import Path


class _MeshBoundaries(_JigsawGeom2D):

    def __init__(self, OuterRing, *InnerRings):
        super(_MeshBoundaries, self).__init__()
        self._OuterRing = OuterRing
        self._InnerRings = InnerRings

    @property
    def OuterRing(self):
        return self._OuterRing

    @property
    def InnerRings(self):
        return self._InnerRings

    @property
    def _OuterRing(self):
        return self.__OuterRing

    @property
    def _InnerRings(self):
        return self.__InnerRings

    @_OuterRing.setter
    def _OuterRing(self, OuterRing):
        if not isinstance(OuterRing, Path):
            raise TypeError('OuterRing must be of type {}'.format(Path))
        self.__OuterRing = OuterRing

    @_InnerRings.setter
    def _InnerRings(self, InnerRings):
        for InnerRing in InnerRings:
            if not isinstance(InnerRing, Path):
                raise TypeError('InnerRing must be of type {}'.format(Path))
        self.__InnerRings = InnerRings
