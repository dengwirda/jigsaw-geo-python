#cython: language_level=3
from jigsawpy.cjigsaw.jigsaw_msh_t cimport jigsaw_msh_t

cdef class Mesh:
    
    cdef jigsaw_msh_t __mesh
    cdef str __mesh_type