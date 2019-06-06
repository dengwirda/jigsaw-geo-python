#cython: language_level=3
"""
Use JIGSAW to mesh a simple domain, but starting from
user-defined initial-conditions.
"""
from jigsawpy.cjigsaw.lib_jigsaw cimport jigsaw_init_jig_t
from jigsawpy.cjigsaw.lib_jigsaw cimport jigsaw_init_msh_t
from jigsawpy.cjigsaw.lib_jigsaw cimport jigsaw_free_msh_t
from jigsawpy.cjigsaw.lib_jigsaw cimport jigsaw
from jigsawpy.cjigsaw.jigsaw_jig_t cimport jigsaw_jig_t
from jigsawpy.cjigsaw.jigsaw_msh_t cimport jigsaw_msh_t, \
                                           jigsaw_VERT2_t, \
                                           jigsaw_EDGE2_t
from jigsawpy.cjigsaw.jigsaw_const cimport JIGSAW_EUCLIDEAN_MESH, \
                                           JIGSAW_HFUN_RELATIVE

cpdef int main(verbosity=+1):

    cdef int _retv = -1

    # -------------------------------- setup JIGSAW types
    cdef jigsaw_jig_t _jjig
    jigsaw_init_jig_t(&_jjig)

    cdef jigsaw_msh_t _geom
    jigsaw_init_msh_t(&_geom)

    cdef jigsaw_msh_t _init
    jigsaw_init_msh_t(&_init)

    cdef jigsaw_msh_t _mesh
    jigsaw_init_msh_t(&_mesh)

    # --------------------------------------------------------
    #  * JIGSAW's "mesh" is a piecewise linear complex:
    # --------------------------------------------------------
    #  *
    #  *                 e:2
    #  *      v:3 o---------------o v:2
    #  *          |               |
    #  *          |               |
    #  *          |               |
    #  *      e:3 |               | e:1
    #  *          |               |
    #  *          |               |
    #  *          |               |
    #  *      v:0 o---------------o v:1
    #  *                 e:0
    #  *
    # --------------------------------------------------------

    cdef jigsaw_VERT2_t _vert2[4] # setup geom
    for i, (_ppos, _itag) in enumerate([[(0., 0.), +0],
                                        [(1., 0.), +0],
                                        [(1., 1.), +0],
                                        [(0., 1.), +0]]):
        _vert2[i]._ppos = _ppos
        _vert2[i]._itag = _itag

    cdef jigsaw_EDGE2_t _edge2[4]
    for i, (_node, _itag) in enumerate([[(+0, +1), +0],
                                        [(+1, +2), +0],
                                        [(+2, +3), +0],
                                        [(+3, +0), +0]]):
        _edge2[i]._node = _node
        _edge2[i]._itag = _itag

    _geom._flags = JIGSAW_EUCLIDEAN_MESH

    # populate _geom with pointers to jigsaw objects.
    _geom._vert2._data = &_vert2[0]
    _geom._vert2._size = +4

    _geom._edge2._data = &_edge2[0]
    _geom._edge2._size = +4

    # -------------------------------- form init. config.

    cdef jigsaw_VERT2_t _point[4]
    for i, (_ppos, _itag) in enumerate([[(0., 0.), +0],
                                        [(0., .5), +0],
                                        [(0., 1.), +0],
                                        [(.5, .5), +0]]):
        _point[i]._ppos = _ppos
        _point[i]._itag = _itag

    cdef jigsaw_EDGE2_t _edges[3]
    for i, (_node, _itag) in enumerate([[(+0, +1), -1] ,      #  -1 => "un-refinable"
                                        [(+1, +2), -1] ,
                                        [(+2, +3), -1]]):
        _edges[i]._node = _node
        _edges[i]._itag = _itag

    _init._flags = JIGSAW_EUCLIDEAN_MESH

    _init._vert2._data = &_point[0]
    _init._vert2._size = +4

    _init._edge2._data = &_edges[0]
    _init._edge2._size = +3

    # -------------------------------- build JIGSAW tria.

    _jjig._verbosity = verbosity

    _jjig._hfun_hmax = 0.33

    _jjig._hfun_scal = JIGSAW_HFUN_RELATIVE

    _jjig._mesh_dims = +2
    _jjig._geom_feat = +1
    _jjig._mesh_top1 = +1
    _jjig._optm_iter = +0

    _retv = jigsaw (&_jjig,   # the config. opts
                    &_geom,   # geom. data
                    &_init,   # init. data
                    NULL,     # empty hfun. data
                    &_mesh )

    # -------------------------------- print JIGSAW tria. */
    print("\n VERT2: \n\n")
    for _ipos in range(_mesh._vert2._size):
        _x = _mesh._vert2._data[_ipos]._ppos[0]
        _y = _mesh._vert2._data[_ipos]._ppos[1]
        print("%1.4f, %1.4f\n" % (_x, _y))

    print("\n TRIA3: \n\n")
    for _ipos in range(_mesh._tria3._size):
        node0 = _mesh._tria3._data[_ipos]._node[0]
        node1 = _mesh._tria3._data[_ipos]._node[1]
        node2 = _mesh._tria3._data[_ipos]._node[2]
        print("%d, %d, %d\n" % (node0, node1, node2))

    jigsaw_free_msh_t(&_mesh)

    print("JIGSAW returned code : %d \n" % _retv)

    return _retv
