#cython: language_level=3
from cpython.mem cimport PyMem_Malloc, \
                         PyMem_Free
from cpython.pycapsule cimport PyCapsule_New, \
                               PyCapsule_GetPointer
from jigsawpy.cjigsaw.jigsaw_jig_t cimport jigsaw_jig_t
from jigsawpy.cjigsaw.jigsaw_msh_t cimport jigsaw_msh_t
from jigsawpy.cjigsaw.lib_jigsaw cimport jigsaw_init_jig_t, \
                                         jigsaw as _jigsaw
from jigsawpy.Geom cimport Geom as _Geom
# from jigsawpy.Hfun cimport Hfun as _Hfun

cdef class Jigsaw:

    def __cinit__(self):
        cdef jigsaw_jig_t *_jcfg = <jigsaw_jig_t *> PyMem_Malloc(sizeof(jigsaw_jig_t))
        jigsaw_init_jig_t(_jcfg)
        self.__jcfg = _jcfg

    def __init__(self, Geom, Hfun=None, Mesh=None, verbosity=0):
        self._Geom = Geom
        self._Hfun = Hfun
        self._Mesh = Mesh
        self._verbosity = verbosity
    
    def jigsaw(self):
        _retv = _jigsaw(self.__jcfg,
                        self.__geom,
                        self.__init,
                        self.__hfun,
                        self.__mesh)

    @property
    def Geom(self):
        return self._Geom

    @property
    def Hfun(self):
        return self._Hfun

    @property
    def Mesh(self):
        return self._Mesh

    @property
    def verbosity(self):
        return self._verbosity

    @property
    def _Geom(self):
        return self.__Geom

    @property
    def _Hfun(self):
        return self.__Hfun


    @property
    def _Mesh(self):
        return self.__Mesh

    @property
    def _verbosity(self):
        return self.__verbosity

    @_Geom.setter
    def _Geom(self, Geom):
        assert isinstance(Geom, _Geom)
        self.__Geom = Geom
        cdef const char *name = "Geom.__geom"
        cdef jigsaw_msh_t *_geom = <jigsaw_msh_t *>PyCapsule_GetPointer(self.Geom._geom, name)
        self.__geom = _geom


    @_Hfun.setter
    def _Hfun(self, Hfun):
        # assert isinstance(Hfun, _Hfun)
        # self.__Hfun = Hfun
        # if Hfun is not None:
        #     self._hfun = self.Hfun.__hfun
        # else:
        #     self._hfun = NULL
        pass
        

    @_Mesh.setter
    def _Mesh(self, Mesh):
        # assert isinstance(Mesh, _Mesh)
        # self.__Mesh = Mesh
        # if Mesh is not None:
        #     self._init = self.Mesh.__mesh
        # else:
        #     self._init = NULL
        pass
        

    @verbosity.setter
    def verbosity(self, int verbosity):
        self._verbosity = verbosity

    @_verbosity.setter
    def _verbosity(self, int verbosity):
        assert verbosity in [0, 1, 2, 3]
        self.__verbosity = verbosity
