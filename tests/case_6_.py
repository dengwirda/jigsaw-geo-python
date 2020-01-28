
import os
import numpy as np

import jigsawpy


def case_6_(src_path, dst_path):

# DEMO-6: generate a multi-part mesh of the (contiguous) USA
# using state boundaries to partition the mesh. A local
# stereographic projection is employed. The domain is meshed
# using uniform resolution.

    opts = jigsawpy.jigsaw_jig_t()

    geom = jigsawpy.jigsaw_msh_t()
    mesh = jigsawpy.jigsaw_msh_t()

    proj = jigsawpy.jigsaw_prj_t()

#------------------------------------ setup files for JIGSAW

    opts.geom_file = \
        os.path.join(src_path, "proj.msh")

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

    jigsawpy.cmd.jigsaw(opts, mesh)

#------------------------------------ save mesh for Paraview

    print("Saving to ../cache/case_6a.vtk")

    jigsawpy.savevtk(os.path.join(
        dst_path, "case_6a.vtk"), mesh)

    return
