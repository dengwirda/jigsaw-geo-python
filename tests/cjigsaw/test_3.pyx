#cython: language_level=3
"""
Use JIGSAW to mesh a simple geometry with user-defined
mesh-spacing data defined on a "grid".
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
                                           JIGSAW_EUCLIDEAN_GRID, \
                                           JIGSAW_HFUN_ABSOLUTE

cpdef int main(verbosity=+1):
    
    cdef int _retv = -1
    
    # -------------------------------- setup JIGSAW types
    cdef jigsaw_jig_t _jjig
    jigsaw_init_jig_t(&_jjig)

    cdef jigsaw_msh_t _geom
    jigsaw_init_msh_t(&_geom)    

    cdef jigsaw_msh_t _hfun      
    jigsaw_init_msh_t(&_hfun)

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


    # --------------------------------------------------------
    #  * JIGSAW's "grid" uses a column-major numbering:
    # --------------------------------------------------------
    #  *
    #  *                 v:5         
    #  *      v:2 o-------o-------o v:8
    #  *          |       |       |
    #  *          |       |       |
    #  *          |      v:4      |
    #  *      v:1 o-------o-------o v:7
    #  *          |       |       |
    #  *          |       |       |
    #  *          |       |       |
    #  *      v:0 o-------o-------o v:6
    #  *                 v:3
    #  *
    # --------------------------------------------------------

     
    cdef double _hfun_xgrid[3]
    _hfun_xgrid[:] = [0., .5, 1.]
    
    cdef double _hfun_ygrid[3]
    _hfun_ygrid[:] = [0., .5, 1.]
     
    cdef double _hfun_value[9]
    _hfun_value[:] = [.3, .2, .3, .2, .1, .2, .3, .2, .3]
            
    _hfun._flags = JIGSAW_EUCLIDEAN_GRID
    _hfun._xgrid._data = &_hfun_xgrid[0]
    _hfun._xgrid._size = +3

    _hfun._ygrid._data = &_hfun_ygrid[0]
    _hfun._ygrid._size = +3

    _hfun._value._data = &_hfun_value[0]
    _hfun._value._size = +9

    # -------------------------------- build JIGSAW tria. */
        
    _jjig._verbosity = verbosity
    _jjig._hfun_scal = JIGSAW_HFUN_ABSOLUTE
    _jjig._hfun_hmax = 1.
    _jjig._hfun_hmin = 0.
    _jjig._mesh_dims = +2
    _retv = jigsaw (&_jjig,    # the config. opts
                    &_geom,    # geom. data
                    NULL,      # empty init. data 
                    &_hfun,    # hfun. data
                    &_mesh)

    #-------------------------------- print JIGSAW tria. */

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