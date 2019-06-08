#cython: language_level=3
from jigsawpy.cjigsaw.lib_jigsaw cimport jigsaw_init_msh_t
from jigsawpy.cjigsaw.jigsaw_msh_t cimport jigsaw_msh_t, \
                                           jigsaw_VERT2_t, \
                                           jigsaw_EDGE2_t, \
                                           jigsaw_BOUND_t
from jigsawpy.cjigsaw.jigsaw_const cimport JIGSAW_EUCLIDEAN_MESH, \
                                           JIGSAW_EUCLIDEAN_GRID, \
                                           JIGSAW_EUCLIDEAN_DUAL, \
                                           JIGSAW_ELLIPSOID_MESH, \
                                           JIGSAW_ELLIPSOID_GRID, \
                                           JIGSAW_ELLIPSOID_DUAL
from libc.stdlib cimport malloc, free
import numpy as np

cdef class _JigsawGeom2D:

    def __cinit__(self):
        cdef jigsaw_msh_t _geom
        jigsaw_init_msh_t(&_geom)
        self.__geom = _geom

    def __init__(self, str mesh_type):
        self._mesh_type  = mesh_type
        self._set_vert2()
        self._set_edge2()
        # self._set_bound()

    def _set_vert2(self):
        cdef int _malloc
        _malloc = len(self.OuterRing.vertices)
        for InnerRing in self.InnerRings:
            _malloc += len(InnerRing.vertices)
        for Subdomain in self.Subdomains:
            _malloc += len(Subdomain.vertices)
        cdef jigsaw_VERT2_t *_vert2 = <jigsaw_VERT2_t *> malloc(_malloc * sizeof(jigsaw_VERT2_t))
        if not _vert2:
            raise MemoryError()
        cdef int i = 0
        for xy, _ in self.OuterRing.iter_segments():
            _vert2[i]._ppos = xy
            _vert2[i]._itag = i
            i += 1
        for InnerRing in self.InnerRings:
            for xy, _ in InnerRing.iter_segments():
                _vert2[i]._ppos = xy
                _vert2[i]._itag = i
                i += 1
        for Subdomain in self.Subdomains:
            for xy, _ in Subdomain.iter_segments():
                _vert2[i]._ppos = xy
                _vert2[i]._itag = i
                i += 1
        self.__geom._vert2._data = _vert2
        self.__geom._vert2._size = _malloc

    def _set_edge2(self):
        cdef int _malloc
        _malloc = len(self.OuterRing.vertices)
        for InnerRing in self.InnerRings:
            _malloc += len(InnerRing.vertices)
        for Subdomain in self.Subdomains:
            _malloc += len(Subdomain.vertices)
        cdef jigsaw_EDGE2_t *_edge2 = <jigsaw_EDGE2_t *> malloc(_malloc * sizeof(jigsaw_EDGE2_t))
        if not _edge2:
            raise MemoryError()
        cdef int i = 0
        for xy, code in self.OuterRing.iter_segments():
            if code != 79:
                _node = [i, i+1]
            else:
                _node = [i, 0]
            _edge2[i]._node = _node
            _edge2[i]._itag = i
            i += 1
        for InnerRing in self.InnerRings:
            _i = i
            for xy, code in InnerRing.iter_segments():
                if code != 79:
                    _node = [i, i+1]
                else:
                    _node = [i, _i]
                _edge2[i]._node = _node
                _edge2[i]._itag = i
                i += 1
        for Subdomain in self.Subdomains:
            for xy, code in Subdomain.iter_segments():
                if code != 79:
                    _node = [i, i+1]
                else:
                    _node = [i, 0]
                _edge2[i]._node = _node
                _edge2[i]._itag = i
                i += 1
        self.__geom._edge2._data = _edge2
        self.__geom._edge2._size = _malloc

    def _set_bound(self):
        raise NotImplementedError
    #     cdef int _malloc = 0
    #     for Subdomain in self.Subdomains:
    #         _malloc += len(Subdomain.vertices)
    #     cdef jigsaw_BOUND_t *_bound = <jigsaw_BOUND_t *> malloc(_malloc * sizeof(jigsaw_BOUND_t))
    #     if not _bound:
    #         raise MemoryError()
    #     cdef int i = 0
    #     for Subdomain in self.Subdomains:
    #         for xy, _ in Subdomain.iter_segments():
    #             _bound[i]._itag = _itag
    #             _bound[i]._indx = _indx
    #             _bound[i]._kind = _kind
    #             i += 1
    #     self.__geom._bound._data = _bound
    #     self.__geom._bound._size = _malloc

    def __dealloc__(self):
        free(self.__geom._vert2._data)
        free(self.__geom._edge2._data)
        free(self.__geom._bound._data)

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
