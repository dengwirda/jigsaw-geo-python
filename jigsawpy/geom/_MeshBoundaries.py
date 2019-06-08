from jigsawpy.geom._JigsawGeom2D import _JigsawGeom2D
from matplotlib.path import Path


class _MeshBoundaries(_JigsawGeom2D):

    def __init__(self, OuterRing, InnerRings=list(), Subdomains=list(),
                 mesh_type='JIGSAW_EUCLIDEAN_MESH'):
        self._OuterRing = OuterRing
        self._InnerRings = InnerRings
        self._Subdomains = Subdomains
        super(_MeshBoundaries, self).__init__(mesh_type)

    @property
    def OuterRing(self):
        return self._OuterRing

    @property
    def InnerRings(self):
        return self._InnerRings

    @property
    def Subdomains(self):
        return self._Subdomains

    @property
    def _OuterRing(self):
        return self.__OuterRing

    @property
    def _InnerRings(self):
        return self.__InnerRings

    @property
    def _Subdomains(self):
        return self.__Subdomains

    @_OuterRing.setter
    def _OuterRing(self, OuterRing):
        if not isinstance(OuterRing, Path):
            raise TypeError('OuterRing must be of type {}'.format(Path))
        if OuterRing.codes is None:
            raise Exception('Path instances must be explicitly closed.')
        self.__OuterRing = OuterRing

    @_InnerRings.setter
    def _InnerRings(self, InnerRings):
        for InnerRing in list(InnerRings):
            if not isinstance(InnerRing, Path):
                raise TypeError('InnerRings must be of a list of '
                                + '{} instances.'.format(Path))
            if InnerRing.codes is None:
                raise Exception('Path instances must be explicitly closed.')
        self.__InnerRings = InnerRings

    @_Subdomains.setter
    def _Subdomains(self, Subdomains):
        for Subdomain in list(Subdomains):
            if not isinstance(Subdomain, Path):
                raise TypeError('Subdomains must be of a list of '
                                + '{} instances.'.format(Path))
            if Subdomain.codes is None:
                raise Exception('Path instances must be explicitly closed.')
        self.__Subdomains = Subdomains
