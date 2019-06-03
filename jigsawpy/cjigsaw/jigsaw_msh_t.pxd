#cython: language_level=3
cdef extern from '../../lib/jigsaw/inc/lib_jigsaw.h':
    ctypedef int indx_t
    ctypedef double  real_t

cdef extern from '../../lib/jigsaw/inc/jigsaw_msh_t.h':
    
    ctypedef struct jigsaw_VERT2_t:
        real_t                  _ppos[2] # coord.'s
        indx_t                  _itag    # ID tag
        
    ctypedef struct jigsaw_VERT3_t:
        real_t                  _ppos[3] # coord.'s
        indx_t                  _itag     # ID tag
    
    ctypedef struct jigsaw_EDGE2_t:
        indx_t                  _node[2] # indexing
        indx_t                  _itag     # ID tag
    
    ctypedef struct jigsaw_TRIA3_t:
        indx_t                  _node[3] # indexing
        indx_t                  _itag     # ID tag
        
    ctypedef struct jigsaw_QUAD4_t:
        indx_t                  _node[4] # indexing
        indx_t                  _itag     # ID tag
        
    ctypedef struct jigsaw_TRIA4_t:
        indx_t                  _node[4] # indexing
        indx_t                  _itag     # ID tag
        
    ctypedef struct jigsaw_HEXA8_t:
        indx_t                  _node[8] # indexing
        indx_t                  _itag     # ID tag
        
    ctypedef struct jigsaw_WEDG6_t:
        indx_t                  _node[6] # indexing
        indx_t                  _itag     # ID tag
        
    ctypedef struct jigsaw_PYRA5_t:
        indx_t                  _node[5] # indexing
        indx_t                  _itag     # ID tag
        
    ctypedef struct jigsaw_BOUND_t:
        indx_t                  _itag     # ID tag
        indx_t                  _indx     # MSH num.
        indx_t                  _kind     # MSH obj.


    #------------------------------------------- array types    
    
    ctypedef struct jigsaw_VERT2_array_t:
        size_t                             _size
        jigsaw_VERT2_t                    *_data
        
    ctypedef struct jigsaw_VERT3_array_t:
        size_t                             _size
        jigsaw_VERT3_t                    *_data
        
    ctypedef struct jigsaw_EDGE2_array_t:
        size_t                             _size
        jigsaw_EDGE2_t                    *_data
        
    ctypedef struct jigsaw_TRIA3_array_t:
        size_t                             _size
        jigsaw_TRIA3_t                    *_data
        
    ctypedef struct jigsaw_QUAD4_array_t:
        size_t                             _size
        jigsaw_QUAD4_t                    *_data
        
    ctypedef struct jigsaw_TRIA4_array_t:
        size_t                             _size
        jigsaw_TRIA4_t                    *_data
        
    ctypedef struct jigsaw_HEXA8_array_t:
        size_t                             _size
        jigsaw_HEXA8_t                    *_data

    ctypedef struct jigsaw_WEDG6_array_t:
        size_t                             _size
        jigsaw_WEDG6_t                    *_data
        
    ctypedef struct jigsaw_PYRA5_array_t:
        size_t                             _size
        jigsaw_PYRA5_t                    *_data
        
    ctypedef struct jigsaw_BOUND_array_t:
        size_t                             _size
        jigsaw_BOUND_t                    *_data
    
    ctypedef struct jigsaw_INDEX_array_t:
        size_t                             _size
        indx_t                 *_data
        
    ctypedef struct jigsaw_REALS_array_t:
        size_t                             _size
        real_t                 *_data
    
    #------------------------------------------- "msh" class
    ctypedef struct jigsaw_msh_t:   
        indx_t        _flags
        # if (_flags == EUCLIDEAN_MESH)
        jigsaw_VERT2_array_t    _vert2
        jigsaw_VERT3_array_t    _vert3
        jigsaw_REALS_array_t    _power
        jigsaw_EDGE2_array_t    _edge2
        jigsaw_TRIA3_array_t    _tria3
        jigsaw_QUAD4_array_t    _quad4
        jigsaw_TRIA4_array_t    _tria4
        jigsaw_HEXA8_array_t    _hexa8
        jigsaw_WEDG6_array_t    _wedg6
        jigsaw_PYRA5_array_t    _pyra5
        jigsaw_BOUND_array_t    _bound
        # if (_flags == ELLIPSOID_MESH)
        jigsaw_REALS_array_t    _radii
        # if (_flags == EUCLIDEAN_GRID)
        # OR (_flags == ELLIPSOID_GRID)
        jigsaw_REALS_array_t    _xgrid
        jigsaw_REALS_array_t    _ygrid
        jigsaw_REALS_array_t    _zgrid
        # if (_flags == EUCLIDEAN_MESH)
        # OR (_flags == EUCLIDEAN_GRID)
        # OR (_flags == ELLIPSOID_MESH)
        # OR (_flags == ELLIPSOID_GRID)
        jigsaw_REALS_array_t    _value
       
