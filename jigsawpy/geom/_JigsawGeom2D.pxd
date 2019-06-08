#cython: language_level=3
from jigsawpy.cjigsaw.jigsaw_msh_t cimport jigsaw_msh_t


cdef class _JigsawGeom2D:
       
    cdef jigsaw_msh_t __geom
    cdef int _flags
    cdef str __mesh_type
