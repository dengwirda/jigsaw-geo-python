
import ctypes as ct
import numpy as np
import os
import inspect

from pathlib import Path

from jigsawpy.def_t import indx_t, real_t

from jigsawpy.msh_l import libsaw_VERT2_t, libsaw_VERT3_t, \
    libsaw_EDGE2_t, libsaw_TRIA3_t, \
    libsaw_QUAD4_t, libsaw_TRIA4_t, \
    libsaw_HEXA8_t, libsaw_WEDG6_t, \
    libsaw_PYRA5_t, libsaw_BOUND_t

from jigsawpy.msh_l import libsaw_msh_t
from jigsawpy.jig_l import libsaw_jig_t

from jigsawpy.certify import certify

from jigsawpy.def_t import jigsaw_def_t
from jigsawpy.msh_t import jigsaw_msh_t

# ---------------------------- Try to find/load JIGSAW's API.

jlibname = Path()

if (jlibname == Path()):
    # ---------------------------- set-up path for "local" binary

    #   stackoverflow.com/questions/2632199/
    #       how-do-i-get-the-
    #           path-of-the-current-executed-file-in-python
    filename = \
        inspect.getsourcefile(lambda: None)

    filepath = \
        (Path(filename).resolve()).parent

    if (os.name == "nt"):
        jlibname = \
            filepath / "_lib" / "jigsaw.dll"

    elif (os.name == "posix"):
        jlibname = \
            filepath / "_lib" / "libjigsaw.so"

    else:
        jlibname = Path()

    if (not jlibname.is_file()):
        jlibname = Path()

if (jlibname == Path()):
    # ---------------------------- search machine path for binary
    if (os.name == "nt"):
        jlibname = Path("jigsaw.dll")

    elif (os.name == "posix"):
        jlibname = Path("libjigsaw.so")

    else:
        jlibname = Path()

if (jlibname != Path()):
    # ---------------------------- load jigsaw library via ctypes
    jlib = ct.cdll.LoadLibrary(str(jlibname))

   #print( jlibname )

else:
    raise Exception("JIGSAW's lib not found")


def put_jig_t(jigt, jigl):
    """
    PUT-JIG_t: Assign data from python-to-ctypes objects.

    """
    if (jigt is None):
        return

    # --------------------------------- assign MISC user-opt.
    if (isinstance(jigt.verbosity, int)):
        jigl.verbosity = indx_t(jigt.verbosity)
    elif (jigt.verbosity is not None):
        raise Exception("VERBOSITY type")

    # --------------------------------- assign GEOM user-opt.
    if (isinstance(jigt.geom_seed, int)):
        jigl.geom_seed = indx_t(jigt.geom_seed)
    elif (jigt.geom_seed is not None):
        raise Exception("GEOM-SEED type")

    if (isinstance(jigt.geom_feat, bool)):
        jigl.geom_feat = indx_t(jigt.geom_feat)
    elif (jigt.geom_feat is not None):
        raise Exception("GEOM-FEAT type")

    if (isinstance(jigt.geom_eta1, float)):
        jigl.geom_eta1 = real_t(jigt.geom_eta1)
    elif (jigt.geom_eta1 is not None):
        raise Exception("GEOM-ETA1 type")

    if (isinstance(jigt.geom_eta2, float)):
        jigl.geom_eta2 = real_t(jigt.geom_eta2)
    elif (jigt.geom_eta2 is not None):
        raise Exception("GEOM-ETA2 type")

    # --------------------------------- assign INIT user-opt.
    if (isinstance(jigt.init_near, float)):
        jigl.init_near = real_t(jigt.init_near)
    elif (jigt.init_near is not None):
        raise Exception("INIT-NEAR type")

    # --------------------------------- assign HFUN user-opt.
    if (isinstance(jigt.hfun_scal, str)):
        if (jigt.hfun_scal.lower() == "absolute"):
            jigl.hfun_scal = \
                jigsaw_def_t.JIGSAW_HFUN_ABSOLUTE

        if (jigt.hfun_scal.lower() == "relative"):
            jigl.hfun_scal = \
                jigsaw_def_t.JIGSAW_HFUN_RELATIVE

    elif (jigt.hfun_scal is not None):
        raise Exception("HFUN-SCAL type")

    if (isinstance(jigt.hfun_hmax, float)):
        jigl.hfun_hmax = real_t(jigt.hfun_hmax)
    elif (jigt.hfun_hmax is not None):
        raise Exception("HFUN-HMAX type")

    if (isinstance(jigt.hfun_hmin, float)):
        jigl.hfun_hmin = real_t(jigt.hfun_hmin)
    elif (jigt.hfun_hmin is not None):
        raise Exception("HFUN-HMIN type")

    # --------------------------------- assign MESH user-opt.
    if (isinstance(jigt.bnds_kern, str)):
        if (jigt.bnds_kern.lower() == "triacell"):
            jigl.bnds_kern = \
                jigsaw_def_t.JIGSAW_BNDS_TRIACELL

        if (jigt.bnds_kern.lower() == "dualcell"):
            jigl.bnds_kern = \
                jigsaw_def_t.JIGSAW_BNDS_DUALCELL

    elif (jigt.bnds_kern is not None):
        raise Exception("BNDS-KERN type")

    if (isinstance(jigt.mesh_dims, int)):
        jigl.mesh_dims = indx_t(jigt.mesh_dims)
    elif (jigt.mesh_dims is not None):
        raise Exception("MESH-DIMS type")

    if (isinstance(jigt.mesh_kern, str)):
        if (jigt.mesh_kern.lower() == "delfront"):
            jigl.mesh_kern = \
                jigsaw_def_t.JIGSAW_KERN_DELFRONT

        if (jigt.mesh_kern.lower() == "delaunay"):
            jigl.mesh_kern = \
                jigsaw_def_t.JIGSAW_KERN_DELAUNAY

    elif (jigt.mesh_kern is not None):
        raise Exception("MESH-KERN type")

    if (isinstance(jigt.mesh_iter, int)):
        jigl.mesh_iter = indx_t(jigt.mesh_iter)
    elif (jigt.mesh_iter is not None):
        raise Exception("MESH-ITER type")

    if (isinstance(jigt.mesh_top1, bool)):
        jigl.mesh_top1 = indx_t(jigt.mesh_top1)
    elif (jigt.mesh_top1 is not None):
        raise Exception("MESH-TOP1 type")

    if (isinstance(jigt.mesh_top2, bool)):
        jigl.mesh_top2 = indx_t(jigt.mesh_top2)
    elif (jigt.mesh_top2 is not None):
        raise Exception("MESH-TOP2 type")

    if (isinstance(jigt.mesh_rad2, float)):
        jigl.mesh_rad2 = real_t(jigt.mesh_rad2)
    elif (jigt.mesh_rad2 is not None):
        raise Exception("MESH-RAD2 type")

    if (isinstance(jigt.mesh_rad3, float)):
        jigl.mesh_rad3 = real_t(jigt.mesh_rad3)
    elif (jigt.mesh_rad3 is not None):
        raise Exception("MESH-RAD3 type")

    if (isinstance(jigt.mesh_siz1, float)):
        jigl.mesh_siz1 = real_t(jigt.mesh_siz1)
    elif (jigt.mesh_siz1 is not None):
        raise Exception("MESH-SIZ1 type")

    if (isinstance(jigt.mesh_siz2, float)):
        jigl.mesh_siz2 = real_t(jigt.mesh_siz2)
    elif (jigt.mesh_siz2 is not None):
        raise Exception("MESH-SIZ2 type")

    if (isinstance(jigt.mesh_siz3, float)):
        jigl.mesh_siz3 = real_t(jigt.mesh_siz3)
    elif (jigt.mesh_siz3 is not None):
        raise Exception("MESH-SIZ3 type")

    if (isinstance(jigt.mesh_off2, float)):
        jigl.mesh_off2 = real_t(jigt.mesh_off2)
    elif (jigt.mesh_off2 is not None):
        raise Exception("MESH-OFF2 type")

    if (isinstance(jigt.mesh_off3, float)):
        jigl.mesh_off3 = real_t(jigt.mesh_off3)
    elif (jigt.mesh_off3 is not None):
        raise Exception("MESH-OFF3 type")

    if (isinstance(jigt.mesh_snk2, float)):
        jigl.mesh_snk2 = real_t(jigt.mesh_snk2)
    elif (jigt.mesh_snk2 is not None):
        raise Exception("MESH-SNK2 type")

    if (isinstance(jigt.mesh_snk3, float)):
        jigl.mesh_snk3 = real_t(jigt.mesh_snk3)
    elif (jigt.mesh_snk3 is not None):
        raise Exception("MESH-SNK3 type")

    if (isinstance(jigt.mesh_eps1, float)):
        jigl.mesh_eps1 = real_t(jigt.mesh_eps1)
    elif (jigt.mesh_eps1 is not None):
        raise Exception("MESH-EPS1 type")

    if (isinstance(jigt.mesh_eps2, float)):
        jigl.mesh_eps2 = real_t(jigt.mesh_eps2)
    elif (jigt.mesh_eps2 is not None):
        raise Exception("MESH-EPS2 type")

    if (isinstance(jigt.mesh_vol3, float)):
        jigl.mesh_vol3 = real_t(jigt.mesh_vol3)
    elif (jigt.mesh_vol3 is not None):
        raise Exception("MESH-VOL3 type")

    # --------------------------------- assign OPTM user-opt.
    if (isinstance(jigt.optm_iter, int)):
        jigl.optm_iter = indx_t(jigt.optm_iter)
    elif (jigt.optm_iter is not None):
        raise Exception("OPTM-ITER type")

    if (isinstance(jigt.optm_qtol, float)):
        jigl.optm_qtol = real_t(jigt.optm_qtol)
    elif (jigt.optm_qtol is not None):
        raise Exception("OPTM-QTOL type")

    if (isinstance(jigt.optm_qlim, float)):
        jigl.optm_qlim = real_t(jigt.optm_qlim)
    elif (jigt.optm_qlim is not None):
        raise Exception("OPTM-QLIM type")

    if (isinstance(jigt.optm_tria, bool)):
        jigl.optm_tria = indx_t(jigt.optm_tria)
    elif (jigt.optm_tria is not None):
        raise Exception("OPTM-TRIA type")

    if (isinstance(jigt.optm_dual, bool)):
        jigl.optm_dual = indx_t(jigt.optm_dual)
    elif (jigt.optm_dual is not None):
        raise Exception("OPTM-DUAL type")

    if (isinstance(jigt.optm_zip_, bool)):
        jigl.optm_zip_ = indx_t(jigt.optm_zip_)
    elif (jigt.optm_zip_ is not None):
        raise Exception("OPTM-ZIP_ type")

    if (isinstance(jigt.optm_div_, bool)):
        jigl.optm_div_ = indx_t(jigt.optm_div_)
    elif (jigt.optm_div_ is not None):
        raise Exception("OPTM-DIV_ type")

    return


def put_ptr_t(data, kind):

    # --------------------------------- helper to assign ptrs
    return np.asfortranarray(
        data).ctypes.data_as(ct.POINTER(kind))


def put_msh_t(msht, mshl):
    """
    PUT-MSH_t: Assign ptrs from python-to-ctypes objects.

    """
    if (msht is None):
        return

    certify(msht)

    if (msht.mshID is not None):
        # --------------------------------- assign mshID variable
        if (msht.mshID.lower() ==
                "euclidean-mesh"):
            mshl.flags = \
                jigsaw_def_t. \
                JIGSAW_EUCLIDEAN_MESH

        if (msht.mshID.lower() ==
                "euclidean-grid"):
            mshl.flags = \
                jigsaw_def_t. \
                JIGSAW_EUCLIDEAN_GRID

        if (msht.mshID.lower() ==
                "ellipsoid-mesh"):
            mshl.flags = \
                jigsaw_def_t. \
                JIGSAW_ELLIPSOID_MESH

        if (msht.mshID.lower() ==
                "ellipsoid-grid"):
            mshl.flags = \
                jigsaw_def_t. \
                JIGSAW_ELLIPSOID_GRID

    if (msht.radii is not None and
            msht.radii.size != +0):
        # --------------------------------- assign ptrs for RADII
        mshl.radii.size = msht.radii.size
        mshl.radii.data = \
            put_ptr_t(msht.radii, real_t)

    if (msht.vert2 is not None and
            msht.vert2.size != +0):
        # --------------------------------- assign ptrs for VERT2
        mshl.vert2.size = msht.vert2.size
        mshl.vert2.data = \
            put_ptr_t(
                msht.vert2, libsaw_VERT2_t)

    if (msht.vert3 is not None and
            msht.vert3.size != +0):
        # --------------------------------- assign ptrs for VERT3
        mshl.vert3.size = msht.vert3.size
        mshl.vert3.data = \
            put_ptr_t(
                msht.vert3, libsaw_VERT3_t)

    if (msht.power is not None and
            msht.power.size != +0):
        # --------------------------------- assign ptrs for POWER
        mshl.power.size = msht.power.size
        mshl.power.data = \
            put_ptr_t(msht.power, real_t)

    if (msht.edge2 is not None and
            msht.edge2.size != +0):
        # --------------------------------- assign ptrs for EDGE2
        mshl.edge2.size = msht.edge2.size
        mshl.edge2.data = \
            put_ptr_t(
                msht.edge2, libsaw_EDGE2_t)

    if (msht.tria3 is not None and
            msht.tria3.size != +0):
        # --------------------------------- assign ptrs for TRIA3
        mshl.tria3.size = msht.tria3.size
        mshl.tria3.data = \
            put_ptr_t(
                msht.tria3, libsaw_TRIA3_t)

    if (msht.quad4 is not None and
            msht.quad4.size != +0):
        # --------------------------------- assign ptrs for QUAD4
        mshl.quad4.size = msht.quad4.size
        mshl.quad4.data = \
            put_ptr_t(
                msht.quad4, libsaw_QUAD4_t)

    if (msht.tria4 is not None and
            msht.tria4.size != +0):
        # --------------------------------- assign ptrs for TRIA4
        mshl.tria4.size = msht.tria4.size
        mshl.tria4.data = \
            put_ptr_t(
                msht.tria4, libsaw_TRIA4_t)

    if (msht.hexa8 is not None and
            msht.hexa8.size != +0):
        # --------------------------------- assign ptrs for HEXA8
        mshl.hexa8.size = msht.hexa8.size
        mshl.hexa8.data = \
            put_ptr_t(
                msht.hexa8, libsaw_HEXA8_t)

    if (msht.wedg6 is not None and
            msht.wedg6.size != +0):
        # --------------------------------- assign ptrs for WEDG6
        mshl.wedg6.size = msht.wedg6.size
        mshl.wedg6.data = \
            put_ptr_t(
                msht.wedg6, libsaw_WEDG6_t)

    if (msht.pyra5 is not None and
            msht.pyra5.size != +0):
        # --------------------------------- assign ptrs for PYRA5
        mshl.pyra5.size = msht.pyra5.size
        mshl.pyra5.data = \
            put_ptr_t(
                msht.pyra5, libsaw_PYRA5_t)

    if (msht.bound is not None and
            msht.bound.size != +0):
        # --------------------------------- assign ptrs for BOUND
        mshl.bound.size = msht.bound.size
        mshl.bound.data = \
            put_ptr_t(
                msht.bound, libsaw_BOUND_t)

    if (msht.xgrid is not None and
            msht.xgrid.size != +0):
        # --------------------------------- assign ptrs for XGRID
        mshl.xgrid.size = msht.xgrid.size
        mshl.xgrid.data = \
            put_ptr_t(msht.xgrid, real_t)

    if (msht.ygrid is not None and
            msht.ygrid.size != +0):
        # --------------------------------- assign ptrs for YGRID
        mshl.ygrid.size = msht.ygrid.size
        mshl.ygrid.data = \
            put_ptr_t(msht.ygrid, real_t)

    if (msht.zgrid is not None and
            msht.zgrid.size != +0):
        # --------------------------------- assign ptrs for ZGRID
        mshl.zgrid.size = msht.zgrid.size
        mshl.zgrid.data = \
            put_ptr_t(msht.zgrid, real_t)

    if (msht.value is not None and
            msht.value.size != +0):
        # --------------------------------- assign ptrs for VALUE
        mshl.value.size = msht.value.size
        mshl.value.data = \
            put_ptr_t(msht.value, real_t)

    return


def get_msh_t(msht, mshl):
    """
    GET-MSH_t: Copy buffer from python-to-ctypes objects.

    """
    if (mshl.flags ==
            jigsaw_def_t.
            JIGSAW_EUCLIDEAN_MESH):

        msht.mshID = "euclidean-mesh"

    if (mshl.flags ==
            jigsaw_def_t.
            JIGSAW_EUCLIDEAN_GRID):

        msht.mshID = "euclidean-grid"

    if (mshl.flags ==
            jigsaw_def_t.
            JIGSAW_ELLIPSOID_MESH):

        msht.mshID = "ellipsoid-mesh"

    if (mshl.flags ==
            jigsaw_def_t.
            JIGSAW_ELLIPSOID_GRID):

        msht.mshID = "ellipsoid-grid"

    if (mshl.radii.size >= +1):
        # --------------------------------- copy buffer for RADII
        nsrc = mshl.radii.size
        asrc = mshl.radii.data

        msht.radii = np.empty(nsrc,
                              dtype=jigsaw_msh_t.REALS_t)

        adst = msht.radii.ctypes.data
        ct.memmove(adst, asrc,
                   nsrc * ct.sizeof(real_t))

        jlib.jigsaw_free_reals(
            ct.byref(mshl.radii))

    if (mshl.vert2.size >= +1):
        # --------------------------------- copy buffer for VERT2
        nsrc = mshl.vert2.size
        asrc = mshl.vert2.data

        msht.vert2 = np.empty(nsrc,
                              dtype=jigsaw_msh_t.VERT2_t)

        adst = msht.vert2.ctypes.data
        ct.memmove(adst, asrc,
                   nsrc * ct.sizeof(libsaw_VERT2_t)
                   )

        jlib.jigsaw_free_vert2(
            ct.byref(mshl.vert2))

    if (mshl.vert3.size >= +1):
        # --------------------------------- copy buffer for VERT3
        nsrc = mshl.vert3.size
        asrc = mshl.vert3.data

        msht.vert3 = np.empty(nsrc,
                              dtype=jigsaw_msh_t.VERT3_t)

        adst = msht.vert3.ctypes.data
        ct.memmove(adst, asrc,
                   nsrc * ct.sizeof(libsaw_VERT3_t)
                   )

        jlib.jigsaw_free_vert3(
            ct.byref(mshl.vert3))

    if (mshl.power.size >= +1):
        # --------------------------------- copy buffer for POWER
        nsrc = mshl.power.size
        asrc = mshl.power.data

        msht.power = np.empty(nsrc,
                              dtype=jigsaw_msh_t.REALS_t)

        adst = msht.power.ctypes.data
        ct.memmove(adst, asrc,
                   nsrc * ct.sizeof(real_t))

        jlib.jigsaw_free_reals(
            ct.byref(mshl.power))

    if (mshl.edge2.size >= +1):
        # --------------------------------- copy buffer for EDGE2
        nsrc = mshl.edge2.size
        asrc = mshl.edge2.data

        msht.edge2 = np.empty(nsrc,
                              dtype=jigsaw_msh_t.EDGE2_t)

        adst = msht.edge2.ctypes.data
        ct.memmove(adst, asrc,
                   nsrc * ct.sizeof(libsaw_EDGE2_t)
                   )

        jlib.jigsaw_free_edge2(
            ct.byref(mshl.edge2))

    if (mshl.tria3.size >= +1):
        # --------------------------------- copy buffer for TRIA3
        nsrc = mshl.tria3.size
        asrc = mshl.tria3.data

        msht.tria3 = np.empty(nsrc,
                              dtype=jigsaw_msh_t.TRIA3_t)

        adst = msht.tria3.ctypes.data
        ct.memmove(adst, asrc,
                   nsrc * ct.sizeof(libsaw_TRIA3_t)
                   )

        jlib.jigsaw_free_tria3(
            ct.byref(mshl.tria3))

    if (mshl.quad4.size >= +1):
        # --------------------------------- copy buffer for QUAD4
        nsrc = mshl.quad4.size
        asrc = mshl.quad4.data

        msht.quad4 = np.empty(nsrc,
                              dtype=jigsaw_msh_t.QUAD4_t)

        adst = msht.quad4.ctypes.data
        ct.memmove(adst, asrc,
                   nsrc * ct.sizeof(libsaw_QUAD4_t)
                   )

        jlib.jigsaw_free_quad4(
            ct.byref(mshl.quad4))

    if (mshl.tria4.size >= +1):
        # --------------------------------- copy buffer for TRIA4
        nsrc = mshl.tria4.size
        asrc = mshl.tria4.data

        msht.tria4 = np.empty(nsrc,
                              dtype=jigsaw_msh_t.TRIA4_t)

        adst = msht.tria4.ctypes.data
        ct.memmove(adst, asrc,
                   nsrc * ct.sizeof(libsaw_TRIA4_t)
                   )

        jlib.jigsaw_free_tria4(
            ct.byref(mshl.tria4))

    if (mshl.hexa8.size >= +1):
        # --------------------------------- copy buffer for HEXA8
        nsrc = mshl.hexa8.size
        asrc = mshl.hexa8.data

        msht.hexa8 = np.empty(nsrc,
                              dtype=jigsaw_msh_t.HEXA8_t)

        adst = msht.hexa8.ctypes.data
        ct.memmove(adst, asrc,
                   nsrc * ct.sizeof(libsaw_HEXA8_t)
                   )

        jlib.jigsaw_free_hexa8(
            ct.byref(mshl.hexa8))

    if (mshl.wedg6.size >= +1):
        # --------------------------------- copy buffer for WEDG6
        nsrc = mshl.wedg6.size
        asrc = mshl.wedg6.data

        msht.wedg6 = np.empty(nsrc,
                              dtype=jigsaw_msh_t.WEDG6_t)

        adst = msht.wedg6.ctypes.data
        ct.memmove(adst, asrc,
                   nsrc * ct.sizeof(libsaw_WEDG6_t)
                   )

        jlib.jigsaw_free_wedg6(
            ct.byref(mshl.wedg6))

    if (mshl.pyra5.size >= +1):
        # --------------------------------- copy buffer for PYRA5
        nsrc = mshl.pyra5.size
        asrc = mshl.pyra5.data

        msht.pyra5 = np.empty(nsrc,
                              dtype=jigsaw_msh_t.PYRA5_t)

        adst = msht.pyra5.ctypes.data
        ct.memmove(adst, asrc,
                   nsrc * ct.sizeof(libsaw_PYRA5_t)
                   )

        jlib.jigsaw_free_pyra5(
            ct.byref(mshl.pyra5))

    if (mshl.xgrid.size >= +1):
        # --------------------------------- copy buffer for XGRID
        nsrc = mshl.xgrid.size
        asrc = mshl.xgrid.data

        msht.xgrid = np.empty(nsrc,
                              dtype=jigsaw_msh_t.REALS_t)

        adst = msht.xgrid.ctypes.data
        ct.memmove(adst, asrc,
                   nsrc * ct.sizeof(real_t))

        jlib.jigsaw_free_reals(
            ct.byref(mshl.xgrid))

    if (mshl.ygrid.size >= +1):
        # --------------------------------- copy buffer for YGRID
        nsrc = mshl.ygrid.size
        asrc = mshl.ygrid.data

        msht.ygrid = np.empty(nsrc,
                              dtype=jigsaw_msh_t.REALS_t)

        adst = msht.ygrid.ctypes.data
        ct.memmove(adst, asrc,
                   nsrc * ct.sizeof(real_t))

        jlib.jigsaw_free_reals(
            ct.byref(mshl.ygrid))

    if (mshl.zgrid.size >= +1):
        # --------------------------------- copy buffer for ZGRID
        nsrc = mshl.zgrid.size
        asrc = mshl.zgrid.data

        msht.zgrid = np.empty(nsrc,
                              dtype=jigsaw_msh_t.REALS_t)

        adst = msht.zgrid.ctypes.data
        ct.memmove(adst, asrc,
                   nsrc * ct.sizeof(real_t))

        jlib.jigsaw_free_reals(
            ct.byref(mshl.zgrid))

    if (mshl.value.size >= +1):
        # --------------------------------- copy buffer for VALUE
        nsrc = mshl.value.size
        asrc = mshl.value.data

        msht.value = np.empty(nsrc,
                              dtype=jigsaw_msh_t.REALS_t)

        adst = msht.value.ctypes.data
        ct.memmove(adst, asrc,
                   nsrc * ct.sizeof(real_t))

        jlib.jigsaw_free_reals(
            ct.byref(mshl.value))

    return


def jigsaw(opts, geom, mesh,
           init=None,
           hfun=None):
    """
    JIGSAW API-lib. interface to JIGSAW.

    JIGSAW(OPTS,GEOM,MESH,INIT=None,
                          HFUN=None)

    Call the JIGSAW mesh generator using the config. options
    specified in the OPTS structure.

    OPTS is a user-defined set of meshing options. See JIG_t
    for details.

    """

    # --------------------------------- set-up ctypes objects

    ojig = libsaw_jig_t()

    jlib.jigsaw_init_jig_t(ct.byref(ojig))

    put_jig_t(opts, ojig)

    gmsh = libsaw_msh_t()
    mmsh = libsaw_msh_t()
    imsh = libsaw_msh_t()
    hmsh = libsaw_msh_t()

    jlib.jigsaw_init_msh_t(ct.byref(gmsh))
    jlib.jigsaw_init_msh_t(ct.byref(mmsh))
    jlib.jigsaw_init_msh_t(ct.byref(imsh))
    jlib.jigsaw_init_msh_t(ct.byref(hmsh))

    put_msh_t(geom, gmsh)
    put_msh_t(init, imsh)
    put_msh_t(hfun, hmsh)

    iptr = ct.byref(imsh)
    if init is None:
        iptr = 0

    hptr = ct.byref(hmsh)
    if hfun is None:
        hptr = 0

    # --------------------------------- call to JIGSAW's lib.

    retv = jlib.jigsaw(ct.byref(ojig),
                       ct.byref(gmsh),
                       iptr,
                       hptr,
                       ct.byref(mmsh))

    # --------------------------------- copy buffers to MSH_t

    get_msh_t(mesh, mmsh)

    return


def tripod(opts, init, tria,
           geom=None):
    """
    TRIPOD API-lib. interface to TRIPOD.

    TRIPOD(OPTS,INIT,TRIA,GEOM=None)

    Call the TRIPOD tessellation util. using the config. opt
    specified in the OPTS structure.

    OPTS is a user-defined set of meshing options. See JIG_t
    for details.

    """

    # --------------------------------- set-up ctypes objects

    ojig = libsaw_jig_t()

    jlib.jigsaw_init_jig_t(ct.byref(ojig))

    put_jig_t(opts, ojig)

    imsh = libsaw_msh_t()
    tmsh = libsaw_msh_t()
    gmsh = libsaw_msh_t()

    jlib.jigsaw_init_msh_t(ct.byref(imsh))
    jlib.jigsaw_init_msh_t(ct.byref(tmsh))
    jlib.jigsaw_init_msh_t(ct.byref(gmsh))

    put_msh_t(init, imsh)
    put_msh_t(geom, gmsh)

    gptr = ct.byref(gmsh)
    if geom is None:
        gptr = 0

    # --------------------------------- call to JIGSAW's lib.

    retv = jlib.tripod(ct.byref(ojig),
                       ct.byref(imsh),
                       gptr,
                       ct.byref(tmsh))

    # --------------------------------- copy buffers to MSH_t

    get_msh_t(tria, tmsh)

    return
