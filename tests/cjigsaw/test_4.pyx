#cython: language_level=3
"""
An example that uses JIGSAW to mesh "multiply-connected" 
geometry. 
"""
from jigsawpy.cjigsaw.lib_jigsaw cimport jigsaw_init_jig_t
from jigsawpy.cjigsaw.lib_jigsaw cimport jigsaw_init_msh_t
from jigsawpy.cjigsaw.lib_jigsaw cimport jigsaw_free_msh_t
from jigsawpy.cjigsaw.lib_jigsaw cimport jigsaw
from jigsawpy.cjigsaw.jigsaw_jig_t cimport jigsaw_jig_t
from jigsawpy.cjigsaw.jigsaw_msh_t cimport jigsaw_msh_t, \
                                           jigsaw_VERT2_t, \
                                           jigsaw_EDGE2_t, \
                                           jigsaw_BOUND_t
from jigsawpy.cjigsaw.jigsaw_const cimport JIGSAW_EUCLIDEAN_MESH, \
                                           JIGSAW_EDGE2_TAG, \
                                           JIGSAW_HFUN_RELATIVE

cpdef int main(verbosity=+1):
    
    cdef int _retv = 0
    
    # -------------------------------- setup JIGSAW types
    cdef jigsaw_jig_t _jjig
    jigsaw_init_jig_t(&_jjig)

    cdef jigsaw_msh_t _geom
    jigsaw_init_msh_t(&_geom)    

    cdef jigsaw_msh_t _mesh      
    jigsaw_init_msh_t(&_mesh)

    # --------------------------------------------------------
    #  * A domain with "interior" constraints
    # --------------------------------------------------------
    #  *
    #  *                 e:2
    #  *      v:3 o---------------o v:2
    #  *          |               |
    #  *          |      e:6      |
    #  *          |     o---o     |
    #  *      e:3 | e:7 |   | e:5 | e:1
    #  *          |     o---o     |
    #  *          |      e:4      |
    #  *          |               |
    #  *      v:0 o---------------o v:1
    #  *                 e:0
    #  *
    # --------------------------------------------------------


    cdef int _ITAG = JIGSAW_EDGE2_TAG
    
    cdef jigsaw_VERT2_t _vert2[8]
    for i, (_ppos, _itag) in enumerate([[(0., 0.), +0 ],
                                        [(3., 0.), +0 ],
                                        [(3., 3.), +0 ],
                                        [(0., 3.), +0 ],
                                        [(1., 1.), +0 ],
                                        [(2., 1.), +0 ],
                                        [(2., 2.), +0 ],
                                        [(1., 2.), +0 ]]):
        _vert2[i]._ppos = _ppos
        _vert2[i]._itag = _itag

    cdef jigsaw_EDGE2_t _edge2[8]
    for i, (_node, _itag) in enumerate([[(+0, +1), +0],          # outer geom.
                                        [(+1, +2), +0],
                                        [(+2, +3), +0],
                                        [(+3, +0), +0],
                                        [(+4, +5), +0],          # inner geom.
                                        [(+5, +6), +0],
                                        [(+6, +7), +0],
                                        [(+7, +4), +0]]):
        _edge2[i]._node = _node
        _edge2[i]._itag = _itag
 
    cdef jigsaw_BOUND_t _bound[4]
    _bound[:] = [[+0, +0, _ITAG],
                 [+0, +1, _ITAG],
                 [+0, +2, _ITAG],
                 [+0, +3, _ITAG]]
    
    _geom._flags = JIGSAW_EUCLIDEAN_MESH;
    
    _geom._vert2._data = &_vert2[0]
    _geom._vert2._size = +4
    
    _geom._edge2._data = &_edge2[0]
    _geom._edge2._size = +4

    _geom._bound._data = &_bound[0]
    _geom._bound._size = +4

    # -------------------------------- build JIGSAW tria. */
        
    _jjig._verbosity = verbosity
    
    _jjig._hfun_hmax = 0.2
    _jjig._hfun_scal = JIGSAW_HFUN_RELATIVE

    _jjig._mesh_dims = +2
    
    _retv = jigsaw (&_jjig,    # the config. opts
                    &_geom,    # geom. data
                    NULL,      # empty init. data 
                    NULL,      # empty hfun. data
                    &_mesh)
 
    # -------------------------------- print JIGSAW tria. */
    print("\n VERT2: \n\n")
    for _ipos in range(_mesh._vert2._size):
        print("%1.4f, %1.4f\n" % (
                _mesh._vert2._data[_ipos]._ppos[0],
                _mesh._vert2._data[_ipos]._ppos[0]))


    print("\n TRIA3: \n\n") ;
    for _ipos in range(_mesh._tria3._size):
        print("%d, %d, %d\n" % (
            _mesh._tria3._data[_ipos]._node[0],
            _mesh._tria3._data[_ipos]._node[1],
            _mesh._tria3._data[_ipos]._node[2]))

    jigsaw_free_msh_t(&_mesh)
    
    print("JIGSAW returned code : %d \n" % _retv) 
    
    return _retv