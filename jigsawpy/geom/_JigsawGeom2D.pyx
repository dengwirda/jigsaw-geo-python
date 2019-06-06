#cython: language_level=3
from jigsawpy.cjigsaw.lib_jigsaw cimport jigsaw_init_jig_t
from jigsawpy.cjigsaw.jigsaw_jig_t cimport jigsaw_jig_t
from jigsawpy.cjigsaw.jigsaw_msh_t cimport jigsaw_VERT2_t, \
                                           jigsaw_EDGE2_t, \
                                           jigsaw_BOUND_t
from jigsawpy.cjigsaw.jigsaw_const cimport JIGSAW_EUCLIDEAN_MESH, \
                                           JIGSAW_EUCLIDEAN_GRID, \
                                           JIGSAW_EUCLIDEAN_DUAL, \
                                           JIGSAW_ELLIPSOID_MESH, \
                                           JIGSAW_ELLIPSOID_GRID, \
                                           JIGSAW_ELLIPSOID_DUAL

cdef class _JigsawGeom2D:

    __mesh_type = JIGSAW_EUCLIDEAN_MESH

    def __cinit__(self):
        cdef jigsaw_jig_t _geom
        jigsaw_init_jig_t(&_geom)
        self.__geom = _geom

    def __call__(self):
        self.__geom._flags = self._flags
        return self.__geom

    def __set_vert2(self, jigsaw_VERT2_t vert2):
        self.__geom._vert2._data = vert2
        raise NotImplementedError('Must determine size before proceeding.')
        self.__geom._vert2._size = None

    def __set_edge2(self, jigsaw_EDGE2_t edge2):
        self.__geom._edge2._data = edge2
        raise NotImplementedError('Must determine size before proceeding.')
        self.__geom._edge2._size = None

    def __set_bound(self, jigsaw_BOUND_t bound):
        self.__geom._bound._data = bound
        raise NotImplementedError('Must determine size before proceeding.')
        self.__geom._bound._size = None

    @property
    def mesh_type(self):
        return self.__mesh_type

    @mesh_type.setter
    def mesh_type(self, mesh_type):
        assert isinstance(mesh_type, (JIGSAW_EUCLIDEAN_MESH,
                                      JIGSAW_EUCLIDEAN_GRID,
                                      JIGSAW_EUCLIDEAN_DUAL,
                                      JIGSAW_ELLIPSOID_MESH,
                                      JIGSAW_ELLIPSOID_GRID,
                                      JIGSAW_ELLIPSOID_DUAL))
        self.__mesh_type = mesh_type

    @property
    def _flags(self):
        return self.mesh_type
