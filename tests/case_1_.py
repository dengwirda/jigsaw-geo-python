
import os
import numpy as np
from scipy import interpolate

import jigsawpy


def case_1_(src_path, dst_path):

# DEMO-1: generate a uniform resolution (150KM) global grid.

    opts = jigsawpy.jigsaw_jig_t()

    topo = jigsawpy.jigsaw_msh_t()

    geom = jigsawpy.jigsaw_msh_t()
    mesh = jigsawpy.jigsaw_msh_t()

#------------------------------------ setup files for JIGSAW

    opts.geom_file = \
        os.path.join(src_path, "eSPH.msh")

    opts.jcfg_file = \
        os.path.join(dst_path, "eSPH.jig")

    opts.mesh_file = \
        os.path.join(dst_path, "mesh.msh")

#------------------------------------ define JIGSAW geometry

    geom.mshID = "ellipsoid-mesh"
    geom.radii = np.full(
        3, 6.371E+003, dtype=geom.REALS_t)

    jigsawpy.savemsh(opts.geom_file, geom)

#------------------------------------ make mesh using JIGSAW

    opts.hfun_scal = "absolute"
    opts.hfun_hmax = +150.              # uniform at 150km

    opts.mesh_dims = +2                 # 2-dim. simplexes

    opts.optm_qlim = +9.5E-01           # tighter opt. tol
    opts.optm_iter = +32
    opts.optm_qtol = +1.0E-05

    jigsawpy.cmd.tetris(opts, 3, mesh)

    scr2 = jigsawpy.triscr2(            # "quality" metric
        mesh.point["coord"],
        mesh.tria3["index"])

#------------------------------------ save mesh for Paraview

    jigsawpy.loadmsh(os.path.join(
        src_path, "topo.msh"), topo)

#------------------------------------ a very rough land mask

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

    print("Saving to ../cache/case_1a.vtk")

    jigsawpy.savevtk(os.path.join(
        dst_path, "case_1a.vtk"), mesh)

    return
