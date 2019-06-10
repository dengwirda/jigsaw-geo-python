#cython: language_level=3
from cpython.mem cimport PyMem_Malloc, \
                         PyMem_Free
from cpython.pycapsule cimport PyCapsule_New, \
                               PyCapsule_GetPointer
from jigsawpy.cjigsaw.lib_jigsaw cimport jigsaw_init_msh_t,\
                                         jigsaw_free_msh_t
from jigsawpy.cjigsaw.jigsaw_msh_t cimport jigsaw_msh_t, \
                                           jigsaw_VERT2_t, \
                                           jigsaw_EDGE2_t, \
                                           jigsaw_BOUND_t
import numpy as np
from jigsawpy.Mesh cimport Mesh


cdef class Geom(Mesh):

    __inner_vertices = list()
        
    def __cinit__(self):
        cdef jigsaw_msh_t *_geom = <jigsaw_msh_t *> PyMem_Malloc(sizeof(jigsaw_msh_t))
        jigsaw_init_msh_t(_geom)
        cdef const char *name = "Geom.__geom"
        self.__geom = PyCapsule_New(<jigsaw_msh_t *>_geom, name, NULL)

    def __init__(self, outer_vertices, str mesh_type):
        super(Geom, self).__init__(mesh_type)
        self._outer_vertices = outer_vertices
        self.__set_flags()
        self.__set_ndim()

    def add_inner_vertices(self, vertices, id=None, bound=False):
        vertices = np.asarray(vertices)
        if self.__ndim != vertices.ndim:
            raise ValueError("Dimension mismatch between outer vertices and inner vertices.")
        _vertices = {'id': id, 'vertices': vertices, 'bound': bound}
        self.__inner_vertices.append(_vertices)

    def get_pointer(self):
        self.__set_malloc()
        if self.__ndim == 2:
            self.__set_vert2()
            self.__set_edge2()
        else:
            raise NotImplementedError('3D not yet supported.')
        # self.__set_bound()
        # return &self.__geom

    def __set_flags(self):
        cdef const char *name = "Geom.__geom"
        cdef jigsaw_msh_t *_geom = <jigsaw_msh_t *>PyCapsule_GetPointer(self.__geom, name)
        _geom._flags = self._flags

    def __set_ndim(self):
        self.__ndim = self.outer_vertices.ndim

    def __set_malloc(self):
        __malloc = len(self.outer_vertices.vertices)
        for inner_vertices in self.inner_vertices:
            __malloc += len(inner_vertices['vertices'])
        self.__malloc = __malloc

    def __set_vert2(self):
        cdef jigsaw_VERT2_t *_vert2 = <jigsaw_VERT2_t *> PyMem_Malloc(self.__malloc * sizeof(jigsaw_VERT2_t))
        if not _vert2:
            raise MemoryError()
        cdef int i = 0
        for xy in self.outer_vertices:
            _vert2[i]._ppos = xy
            _vert2[i]._itag = i
            i += 1
        for inner_vertices in self.inner_vertices:
            for xy in inner_vertices['vertices']:
                _vert2[i]._ppos = xy
                _vert2[i]._itag = i
                i += 1
        cdef const char *name = "Geom.__geom"
        cdef jigsaw_msh_t *_geom = <jigsaw_msh_t *>PyCapsule_GetPointer(self.__geom, name)
        _geom._vert2._data = _vert2
        _geom._vert2._size = self.__malloc

    def __set_edge2(self):
        cdef jigsaw_EDGE2_t *_edge2 = <jigsaw_EDGE2_t *> PyMem_Malloc(self.__malloc * sizeof(jigsaw_EDGE2_t))
        if not _edge2:
            raise MemoryError()
        cdef int i = 0
        for i, xy in enumerate(self.outer_vertices):
            if i != len(self.outer_vertices):
                _node = [i, i+1]
            else:
                _node = [i, 0]
            _edge2[i]._node = _node
            _edge2[i]._itag = i
            i += 1
        for inner_vertices in self.inner_vertices:
            _i = i
            for j in len(inner_vertices['vertices']):
                if j != len(inner_vertices['vertices']):
                    _node = [i, i+1]
                else:
                    _node = [i, _i]
                _edge2[i]._node = _node
                _edge2[i]._itag = i
                i += 1
        cdef const char *name = "Geom.__geom"
        cdef jigsaw_msh_t *_geom = <jigsaw_msh_t *>PyCapsule_GetPointer(self.__geom, name)
        _geom._edge2._data = _edge2
        _geom._edge2._size = self.__malloc

    def __set_bound(self):
        raise NotImplementedError
        cdef int _malloc = 0
        for Subdomain in self.Subdomains:
            _malloc += len(Subdomain.vertices)
        cdef jigsaw_BOUND_t *_bound = <jigsaw_BOUND_t *> PyMem_Malloc(_malloc * sizeof(jigsaw_BOUND_t))
        if not _bound:
            raise MemoryError()
        cdef int i = 0
        for Subdomain in self.Subdomains:
            for xy, _ in Subdomain.iter_segments():
                _bound[i]._itag = _itag
                _bound[i]._indx = _indx
                _bound[i]._kind = _kind
                i += 1
        cdef const char *name = "Geom.__geom"
        cdef jigsaw_msh_t *_geom = <jigsaw_msh_t *>PyCapsule_GetPointer(self.__geom, name)
        _geom._bound._data = _bound
        _geom._bound._size = _malloc

    # def __dealloc__(self):
    #     PyMem_Free(self.__geom._vert2._data)
    #     PyMem_Free(self.__geom._edge2._data)
    #     PyMem_Free(self.__geom._bound._data)
    #     jigsaw_free_msh_t(self.__geom)

    @property
    def _geom(self):
        return self.__geom

    @property
    def _flags(self):
        return self.mesh_type
    
    @property
    def outer_vertices(self):
        return self._outer_vertices

    @property
    def inner_vertices(self):
        return self.__inner_vertices

    @property
    def _outer_vertices(self):
        return self.__outer_vertices

    @_outer_vertices.setter
    def _outer_vertices(self, outer_vertices):
        outer_vertices = np.asarray(outer_vertices)
        assert outer_vertices.ndim in [2, 3]
        self.__outer_vertices = outer_vertices
