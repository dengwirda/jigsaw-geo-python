#cython: language_level=3
from jigsawpy.cjigsaw.jigsaw_jig_t cimport jigsaw_jig_t

cdef class _JigsawGeom2D:
	cdef jigsaw_jig_t __geom