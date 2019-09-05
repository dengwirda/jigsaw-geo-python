
import ctypes as ct

indx_t = ct.c_int32
real_t = ct.c_double


class jigsaw_def_t:
    # --------------------------------- return codes for JIGSAW .

    JIGSAW_UNKNOWN_ERROR = -  1

    JIGSAW_NO_ERROR = +  0

    JIGSAW_FILE_NOT_LOCATED = +  2
    JIGSAW_FILE_NOT_CREATED = +  3

    JIGSAW_INVALID_ARGUMENT = +  4

# --------------------------------- constants for libJIGSAW .

    JIGSAW_NULL_FLAG = -100

    JIGSAW_EUCLIDEAN_MESH = +100
    JIGSAW_EUCLIDEAN_GRID = +101
    JIGSAW_EUCLIDEAN_DUAL = +102

    JIGSAW_ELLIPSOID_MESH = +200
    JIGSAW_ELLIPSOID_GRID = +201
    JIGSAW_ELLIPSOID_DUAL = +202

    JIGSAW_POINT_TAG = + 10
    JIGSAW_EDGE2_TAG = + 20
    JIGSAW_TRIA3_TAG = + 30
    JIGSAW_QUAD4_TAG = + 40
    JIGSAW_TRIA4_TAG = + 50
    JIGSAW_HEXA8_TAG = + 60
    JIGSAW_WEDG6_TAG = + 70
    JIGSAW_PYRA5_TAG = + 80

    JIGSAW_HFUN_RELATIVE = +300
    JIGSAW_HFUN_ABSOLUTE = +301

    JIGSAW_KERN_DELFRONT = +400
    JIGSAW_KERN_DELAUNAY = +401

    JIGSAW_BNDS_TRIACELL = +402
    JIGSAW_BNDS_DUALCELL = +403
