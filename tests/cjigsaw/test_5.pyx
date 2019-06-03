#cython: language_level=3
"""
An example that uses TRIPOD to build a "restricted" DT.
"""
from jigsawpy.cjigsaw.lib_jigsaw cimport jigsaw_init_jig_t
from jigsawpy.cjigsaw.lib_jigsaw cimport jigsaw_init_msh_t
from jigsawpy.cjigsaw.lib_jigsaw cimport jigsaw_free_msh_t
from jigsawpy.cjigsaw.lib_jigsaw cimport tripod
from jigsawpy.cjigsaw.jigsaw_jig_t cimport jigsaw_jig_t
from jigsawpy.cjigsaw.jigsaw_msh_t cimport jigsaw_msh_t, \
                                           jigsaw_VERT2_t, \
                                           jigsaw_EDGE2_t
from jigsawpy.cjigsaw.jigsaw_const cimport JIGSAW_EUCLIDEAN_MESH

cpdef int main(verbosity=+1):
    
    cdef int _retv = 0

    # -------------------------------- setup JIGSAW types   
    cdef jigsaw_jig_t _jjig
    jigsaw_init_jig_t(&_jjig) ;        

    cdef jigsaw_msh_t _geom ;
    jigsaw_init_msh_t(&_geom) ;        

    cdef jigsaw_msh_t _init ;
    jigsaw_init_msh_t(&_init) ;        

    cdef jigsaw_msh_t _tria ;        
    jigsaw_init_msh_t(&_tria) ;
    
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

    _geom._flags = JIGSAW_EUCLIDEAN_MESH;
    
    # populate _geom with pointers to jigsaw objects.
    _geom._vert2._data = &_vert2[0]
    _geom._vert2._size = +4
    
    _geom._edge2._data = &_edge2[0]
    _geom._edge2._size = +4

    # -------------------------------- pts to triangulate

    cdef jigsaw_VERT2_t _point[9]
    for i, (_ppos, _itag) in enumerate([[(0., 0.), +0],
                                        [(1., 0.), +0],
                                        [(1., 1.), +0],
                                        [(0., 1.), +0],
                                        [(.5, .0), +0],
                                        [(1., .5), +0],
                                        [(.5, 1.), +0],
                                        [(.0, .5), +0],
                                        [(.3, .3), +0]]):
        _vert2[i]._ppos = _ppos
        _vert2[i]._itag = _itag
        
    _init._flags = JIGSAW_EUCLIDEAN_MESH
    
    _init._vert2._data = &_point[0]
    _init._vert2._size = +9
        
    # -------------------------------- build TRIPOD r-DT.
        
    _jjig._verbosity = verbosity
        
    _jjig._mesh_dims = +2
        
    _retv = tripod (&_jjig,   # the config. opts
                    &_init,   # init. data            
                    &_geom,   # geom. data
                    &_tria)

    # -------------------------------- print TRIPOD r-DT.
    print("\n VERT2: \n\n")
    for _ipos in range(_tria._vert2._size):
        print("%1.4f, %1.4f\n" % (
                _tria._vert2._data[_ipos]._ppos[0],
                _tria._vert2._data[_ipos]._ppos[0]))


    print("\n TRIA3: \n\n") ;
    for _ipos in range(_tria._tria3._size):
        print("%d, %d, %d\n" % (
            _tria._tria3._data[_ipos]._node[0],
            _tria._tria3._data[_ipos]._node[1],
            _tria._tria3._data[_ipos]._node[2]))

    jigsaw_free_msh_t(&_tria)
    
    print("TRIPOD returned code : %d \n" % _retv)

    return _retv