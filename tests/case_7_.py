
import os
import time
import numpy as np

import jigsawpy


def case_7_(src_path, dst_path):

# DEMO-7: generate a multi-part mesh of the (contiguous) USA
# using state boundaries to partition the mesh. A local
# stereographic projection is employed. The domain is meshed
# using uniform resolution.

    opts = jigsawpy.jigsaw_jig_t()

    geom = jigsawpy.jigsaw_msh_t()
    mesh = jigsawpy.jigsaw_msh_t()

    proj = jigsawpy.jigsaw_prj_t()

#------------------------------------ setup files for JIGSAW

    opts.geom_file = \
        os.path.join(dst_path, "geom.msh")

    opts.jcfg_file = \
        os.path.join(dst_path, "us48.jig")

    opts.mesh_file = \
        os.path.join(dst_path, "mesh.msh")

#------------------------------------ define JIGSAW geometry

    jigsawpy.loadmsh(os.path.join(
        src_path, "us48.msh"), geom)

    xmin = np.min(
        geom.point["coord"][:, 0])
    ymin = np.min(
        geom.point["coord"][:, 1])
    xmax = np.max(
        geom.point["coord"][:, 0])
    ymax = np.max(
        geom.point["coord"][:, 1])

    geom.point["coord"][:, :] *= np.pi / 180.

    proj.prjID = 'stereographic'
    proj.radii = +6.371E+003
    proj.xbase = \
        +0.500 * (xmin + xmax) * np.pi / 180.
    proj.ybase = \
        +0.500 * (ymin + ymax) * np.pi / 180.

    jigsawpy.project(geom, proj, "fwd")

    jigsawpy.savemsh(opts.geom_file, geom)

#------------------------------------ make mesh using JIGSAW

    opts.hfun_hmax = .005

    opts.mesh_dims = +2                 # 2-dim. simplexes
    opts.mesh_eps1 = +1 / 6.

    ttic = time.time()

    jigsawpy.cmd.jigsaw(opts, mesh)

    ttoc = time.time()

    print("CPUSEC =", (ttoc - ttic))

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

#------------------------------------ save mesh for Paraview

    print("Saving to ../cache/case_7a.vtk")

    jigsawpy.savevtk(os.path.join(
        dst_path, "case_7a.vtk"), mesh)

    return
