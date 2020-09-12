
import os
import math
import time
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
        os.path.join(src_path, "geom.msh")

    opts.jcfg_file = \
        os.path.join(dst_path, "opts.jig")

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

#   opts.optm_kern = "cvt+dqdx"

    rbar = np.mean(geom.radii)          # bisect heuristic

    nlev = round(math.log2(
        rbar / math.sin(.4 * math.pi) / opts.hfun_hmax)
    )

    ttic = time.time()

    jigsawpy.cmd.tetris(opts, nlev - 1, mesh)

    ttoc = time.time()

    print("CPUSEC =", (ttoc - ttic))

    print("BISECT =", +nlev)

    cost = jigsawpy.triscr2(            # quality metrics!
        mesh.point["coord"],
        mesh.tria3["index"])

    print("TRISCR =", np.min(cost), np.mean(cost))

    cost = jigsawpy.pwrscr2(
        mesh.point["coord"],
        mesh.power,
        mesh.tria3["index"])

    print("PWRSCR =", np.min(cost), np.mean(cost))

    tbad = jigsawpy.centre2(
        mesh.point["coord"],
        mesh.power,
        mesh.tria3["index"])

    print("OBTUSE =",
          +np.count_nonzero(np.logical_not(tbad)))

    ndeg = jigsawpy.trideg2(
        mesh.point["coord"],
        mesh.tria3["index"])

    print("TOPOL. =",
          +np.count_nonzero(ndeg==+6) / ndeg.size)

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
