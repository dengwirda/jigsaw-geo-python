#cython: language_level=3
from jigsawpy.cjigsaw.jigsaw_msh_t cimport jigsaw_msh_t
from jigsawpy.cjigsaw.lib_jigsaw cimport jigsaw_init_msh_t, \
                                         jigsaw_free_msh_t
from jigsawpy.cjigsaw.jigsaw_const cimport JIGSAW_EUCLIDEAN_MESH, \
                                           JIGSAW_EUCLIDEAN_GRID, \
                                           JIGSAW_EUCLIDEAN_DUAL, \
                                           JIGSAW_ELLIPSOID_MESH, \
                                           JIGSAW_ELLIPSOID_GRID, \
                                           JIGSAW_ELLIPSOID_DUAL


cdef class Mesh:
    
    def __cinit__(self):
        cdef jigsaw_msh_t _mesh
        jigsaw_init_msh_t(&_mesh)
        self.__mesh = _mesh

    def __init__(self, mesh_type, vertices=None, elements=None):
        self._mesh_type = mesh_type

    # def __dealloc__(self):
    #     jigsaw_free_msh_t(self.__mesh)

    @property
    def mesh_type(self):
        return self._mesh_type

    @property
    def _mesh_type(self):
        return self.__mesh_type

    @_mesh_type.setter
    def _mesh_type(self, str mesh_type):
        if mesh_type == "JIGSAW_EUCLIDEAN_MESH":
           self.__geom._flags = JIGSAW_EUCLIDEAN_MESH
        elif mesh_type == "JIGSAW_EUCLIDEAN_GRID":
            self.__geom._flags = JIGSAW_EUCLIDEAN_GRID
        elif mesh_type == "JIGSAW_EUCLIDEAN_DUAL":
            self.__geom._flags = JIGSAW_EUCLIDEAN_DUAL
        elif mesh_type == "JIGSAW_ELLIPSOID_MESH":
            self.__geom._flags = JIGSAW_ELLIPSOID_MESH
        elif mesh_type == "JIGSAW_ELLIPSOID_GRID":
            self.__geom._flags = JIGSAW_ELLIPSOID_GRID
        elif mesh_type == "JIGSAW_ELLIPSOID_DUAL":
            self.__geom._flags = JIGSAW_ELLIPSOID_DUAL
        else:
            TypeError('mesh_type argument must be one of '
                                 + '{}'.format(["JIGSAW_EUCLIDEAN_MESH",
                                                "JIGSAW_EUCLIDEAN_GRID",
                                                "JIGSAW_EUCLIDEAN_DUAL",
                                                "JIGSAW_ELLIPSOID_MESH",
                                                "JIGSAW_ELLIPSOID_GRID",
                                                "JIGSAW_ELLIPSOID_DUAL"]))
        self.__mesh_type = mesh_type
