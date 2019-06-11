#cython: language_level=3
from jigsawpy.Mesh cimport Mesh

cdef class Geom(Mesh):
    
    cdef object __geom
    cdef object __outer_vertices
    cdef object __Geom
    # cdef object __Mesh
    # cdef object __Hfun
    cdef int __ndim
    cdef int __malloc
    cdef int __scal
    cdef int _flags
