
import os
import time
import numpy as np
from scipy import interpolate

import jigsawpy


def case_5_(src_path, dst_path):

# DEMO-5: generate struct. icosahedral and cubedsphere grids

    opts = jigsawpy.jigsaw_jig_t()

    topo = jigsawpy.jigsaw_msh_t()

    geom = jigsawpy.jigsaw_msh_t()
    icos = jigsawpy.jigsaw_msh_t()
    cube = jigsawpy.jigsaw_msh_t()

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
        3, 1.000E+000, dtype=geom.REALS_t)

    jigsawpy.savemsh(opts.geom_file, geom)

#------------------------------------ make mesh using JIGSAW

    opts.hfun_hmax = +1.
    opts.mesh_dims = +2                 # 2-dim. simplexes

    opts.optm_iter = +512
    opts.optm_qtol = +1.0E-06

#   opts.optm_kern = "cvt+dqdx"

    ttic = time.time()

    jigsawpy.cmd.icosahedron(opts, +6, icos)

    ttoc = time.time()

    print("CPUSEC =", (ttoc - ttic))

    ttic = time.time()

    jigsawpy.cmd.cubedsphere(opts, +6, cube)

    ttoc = time.time()

    print("CPUSEC =", (ttoc - ttic))

#------------------------------------ save mesh for Paraview

    jigsawpy.loadmsh(os.path.join(
        src_path, "topo.msh"), topo)

#------------------------------------ a very rough land mask

    zfun = interpolate.RectBivariateSpline(
        topo.ygrid, topo.xgrid, topo.value)

    apos = jigsawpy.R3toS2(
        geom.radii, icos.point["coord"][:])

    apos = apos * 180. / np.pi

    icos.value = zfun(
        apos[:, 1], apos[:, 0], grid=False)

    cell = icos.tria3["index"]

    zmsk = \
        icos.value[cell[:, 0]] + \
        icos.value[cell[:, 1]] + \
        icos.value[cell[:, 2]]
    zmsk = zmsk / +3.0

    icos.tria3 = icos.tria3[zmsk < +0.]

    print("Saving to ../cache/case_5a.vtk")

    jigsawpy.savevtk(os.path.join(
        dst_path, "case_5a.vtk"), icos)

#------------------------------------ a very rough land mask

    apos = jigsawpy.R3toS2(
        geom.radii, cube.point["coord"][:])

    apos = apos * 180. / np.pi

    cube.value = zfun(
        apos[:, 1], apos[:, 0], grid=False)

    cell = cube.quad4["index"]

    zmsk = \
        cube.value[cell[:, 0]] + \
        cube.value[cell[:, 1]] + \
        cube.value[cell[:, 2]] + \
        cube.value[cell[:, 3]]
    zmsk = zmsk / +4.0

    cube.quad4 = cube.quad4[zmsk < +0.]

    print("Saving to ../cache/case_5b.vtk")

    jigsawpy.savevtk(os.path.join(
        dst_path, "case_5b.vtk"), cube)

    return
