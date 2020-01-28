
import os
import numpy as np
from scipy import interpolate

import jigsawpy


def case_4_(src_path, dst_path):

# DEMO-4: generate a multi-resolution mesh, via local refin-
# ement along coastlines and shallow ridges. Global grid
# resolution is 150KM, background resolution is 67KM and the
# min. adaptive resolution is 33KM.

    opts = jigsawpy.jigsaw_jig_t()

    topo = jigsawpy.jigsaw_msh_t()

    geom = jigsawpy.jigsaw_msh_t()
    mesh = jigsawpy.jigsaw_msh_t()
    hmat = jigsawpy.jigsaw_msh_t()

#------------------------------------ setup files for JIGSAW

    opts.geom_file = \
        os.path.join(src_path, "eSPH.msh")

    opts.jcfg_file = \
        os.path.join(dst_path, "eSPH.jig")

    opts.mesh_file = \
        os.path.join(dst_path, "mesh.msh")

    opts.hfun_file = \
        os.path.join(dst_path, "spac.msh")

#------------------------------------ define JIGSAW geometry

    geom.mshID = "ellipsoid-mesh"
    geom.radii = np.full(
        3, 6.371E+003, dtype=geom.REALS_t)

    jigsawpy.savemsh(opts.geom_file, geom)

#------------------------------------ define spacing pattern

    jigsawpy.loadmsh(os.path.join(
        src_path, "topo.msh"), topo)

    hmat.mshID = "ellipsoid-grid"
    hmat.radii = geom.radii

    hmat.xgrid = topo.xgrid * np.pi / 180.
    hmat.ygrid = topo.ygrid * np.pi / 180.

    hfn0 = +150.                        # global spacing
    hfn2 = +33.                         # adapt. spacing
    hfn3 = +67.                         # arctic spacing

    hmat.value = np.sqrt(
        np.maximum(-topo.value, 0.0))

    hmat.value = \
        np.maximum(hmat.value, hfn2)
    hmat.value = \
        np.minimum(hmat.value, hfn3)

    mask = hmat.ygrid < 40. * np.pi / 180.

    hmat.value[mask] = hfn0

#------------------------------------ set HFUN grad.-limiter

    hmat.slope = np.full(               # |dH/dx| limits
        topo.value.shape,
        +0.050, dtype=hmat.REALS_t)

    jigsawpy.savemsh(opts.hfun_file, hmat)

    jigsawpy.cmd.marche(opts, hmat)

#------------------------------------ make mesh using JIGSAW

    opts.hfun_scal = "absolute"
    opts.hfun_hmax = float("inf")       # null HFUN limits
    opts.hfun_hmin = float(+0.00)

    opts.mesh_dims = +2                 # 2-dim. simplexes

    opts.optm_qlim = +9.5E-01           # tighter opt. tol
    opts.optm_iter = +32
    opts.optm_qtol = +1.0E-05

    jigsawpy.cmd.tetris(opts, 3, mesh)

    scr2 = jigsawpy.triscr2(            # "quality" metric
        mesh.point["coord"],
        mesh.tria3["index"])

#------------------------------------ save mesh for Paraview

    apos = jigsawpy.R3toS2(
        geom.radii, mesh.point["coord"][:])

    apos = apos * 180. / np.pi

    zfun = interpolate.RectBivariateSpline(
        topo.ygrid, topo.xgrid, topo.value)

    mesh.value = zfun(
        apos[:, 1], apos[:, 0], grid=False)

    cell = mesh.tria3["index"]

    zmsk = \
        mesh.value[cell[:, 0]] + \
        mesh.value[cell[:, 1]] + \
        mesh.value[cell[:, 2]]
    zmsk = zmsk / +3.0

    mesh.tria3 = mesh.tria3[zmsk < +0.]

    print("Saving to ../cache/case_4a.vtk")

    jigsawpy.savevtk(os.path.join(
        dst_path, "case_4a.vtk"), mesh)

    print("Saving to ../cache/case_4b.vtk")

    jigsawpy.savevtk(os.path.join(
        dst_path, "case_4b.vtk"), hmat)

    return
