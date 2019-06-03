
cdef extern from '../../lib/jigsaw/inc/jigsaw_const.h':

    # --------------------------------------------------------
    #  * return codes for JIGSAW.
    # --------------------------------------------------------
    cdef int JIGSAW_UNKNOWN_ERROR    = -1
    cdef int JIGSAW_NO_ERROR         = +0
    cdef int JIGSAW_FILE_NOT_LOCATED = +2
    cdef int JIGSAW_FILE_NOT_CREATED = +3
    cdef int JIGSAW_INVALID_ARGUMENT = +4

    # --------------------------------------------------------
    #  * constants for JIGSAW.
    # --------------------------------------------------------
    cdef int JIGSAW_NULL_FLAG      = -100
    cdef int JIGSAW_EUCLIDEAN_MESH = +100
    cdef int JIGSAW_EUCLIDEAN_GRID = +101
    cdef int JIGSAW_EUCLIDEAN_DUAL = +102
    cdef int JIGSAW_ELLIPSOID_MESH = +200
    cdef int JIGSAW_ELLIPSOID_GRID = +201
    cdef int JIGSAW_ELLIPSOID_DUAL = +202
    cdef int JIGSAW_POINT_TAG     =  +10
    cdef int JIGSAW_EDGE2_TAG     =  +20
    cdef int JIGSAW_TRIA3_TAG     =  +30
    cdef int JIGSAW_QUAD4_TAG     =  +40
    cdef int JIGSAW_TRIA4_TAG     =  +50
    cdef int JIGSAW_HEXA8_TAG     =  +60
    cdef int JIGSAW_WEDG6_TAG     =  +70
    cdef int JIGSAW_PYRA5_TAG     =  +80
    cdef int JIGSAW_HFUN_RELATIVE  = +300
    cdef int JIGSAW_HFUN_ABSOLUTE  = +301
    cdef int JIGSAW_KERN_DELFRONT  = +400
    cdef int JIGSAW_KERN_DELAUNAY  = +401
    cdef int JIGSAW_BNDS_TRIACELL  = +402
    cdef int JIGSAW_BNDS_DUALCELL  = +403
     