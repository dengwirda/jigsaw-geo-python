#cython: language_level=3
from jigsawpy.cjigsaw.jigsaw_jig_t cimport jigsaw_jig_t
from jigsawpy.cjigsaw.jigsaw_msh_t cimport jigsaw_msh_t

cdef extern from '../../lib/jigsaw/inc/lib_jigsaw.h':

    # --------------------------------------------------------
    #  * generate mesh via JIGSAW.
    # --------------------------------------------------------
    cdef int jigsaw_make_mesh = jigsaw
    cdef int jigsaw(jigsaw_jig_t *_jcfg,
                    jigsaw_msh_t *_geom,
                    jigsaw_msh_t *_init,
                    jigsaw_msh_t *_hfun,
                    jigsaw_msh_t *_mesh)
        
    # --------------------------------------------------------
    #  * compute rDT's via TRIPOD.
    # --------------------------------------------------------
            
    cdef int tripod(jigsaw_jig_t *_jcfg,
                    jigsaw_msh_t *_init,
                    jigsaw_msh_t *_geom,
                    jigsaw_msh_t *_mesh)
        
    # --------------------------------------------------------
    #  * limit |df/dx| via MARCHE.
    # -------------------------------------------------------- 
    cdef int marche(jigsaw_jig_t *_jcfg,
                    jigsaw_msh_t *_ffun)

    # --------------------------------------------------------
    #  * setup objects for JIGSAW.
    # --------------------------------------------------------
    cdef void jigsaw_init_msh_t(jigsaw_msh_t *_mesh)
    cdef void jigsaw_init_jig_t(jigsaw_jig_t *_jjig)
        
    # --------------------------------------------------------
    #  * parse-to-file for JIGSAW.
    # --------------------------------------------------------
    cdef int jigsaw_save_msh_t(char *_file, jigsaw_msh_t *_mesh)
    cdef int jigsaw_save_jig_t(char *_file, jigsaw_jig_t *_jjig)
    cdef int jigsaw_load_msh_t(char *_file, jigsaw_msh_t *_mesh)
    cdef int jigsaw_load_jig_t(char *_file, jigsaw_jig_t *_jjig)

    cdef void jigsaw_free_msh_t(jigsaw_msh_t *_mesh)
