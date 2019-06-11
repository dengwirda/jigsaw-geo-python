#cython: language_level=3
from jigsawpy.cjigsaw.jigsaw_jig_t cimport jigsaw_jig_t
from jigsawpy.cjigsaw.jigsaw_msh_t cimport jigsaw_msh_t
# from jigsawpy.cjigsaw.lib_jigsaw cimport jigsaw

cdef class Jigsaw:
    
    cdef object __Geom
    cdef object __Hfun
    cdef object __Mesh
    cdef int __verbosity
    cdef jigsaw_jig_t *__jcfg
    cdef jigsaw_msh_t *__geom
    cdef jigsaw_msh_t *__init
    cdef jigsaw_msh_t *__hfun
    cdef jigsaw_msh_t *__mesh

