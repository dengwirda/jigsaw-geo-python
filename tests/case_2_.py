
"""
* DEMO-2 --- generate meshes for a lake superior geometry,
*   demonstrating the use of "restricted"-Delaunay meshes to
*   resample complex boundary definitions at user-defined
*   resolution.
*
* These examples call to JIGSAW via its api.-lib. interface.
*
"""

from pathlib import Path
import numpy as np

import jigsawpy

import matplotlib.pyplot as plt
import matplotlib.tri as tri
from matplotlib.collections import LineCollection


def case_2_(filepath, savefigs=False):

    # ------------------------------------ define JIGSAW geometry

    geom_file = \
        str(Path(filepath) / "lake.msh")

    geom = jigsawpy.jigsaw_msh_t()

    jigsawpy.loadmsh(geom_file, geom)

# ------------------------------------ the lo-resolution case

    print("Call libJIGSAW: case 2a.")

    opts = jigsawpy.jigsaw_jig_t()
    mesh = jigsawpy.jigsaw_msh_t()

    opts.hfun_hmax = 0.060
    opts.mesh_dims = +2
    opts.mesh_rad2 = +1.20

    jigsawpy.lib.jigsaw(opts, geom, mesh)

    fig = plt.figure(1)
    axi = fig.add_subplot(1, 1, 1)
    axi.triplot(tri.Triangulation(
        mesh.vert2["coord"][:, 0],
        mesh.vert2["coord"][:, 1],
        mesh.tria3["index"]), linewidth=0.500)

    vert = geom.vert2["coord"]
    edge = geom.edge2["index"]
    eONE = vert[edge[:, 0], :]
    eTWO = vert[edge[:, 1], :]
    line = LineCollection(
        np.stack((eONE, eTWO), axis=1), color="k")
    axi.add_collection(line)
    plt.axis("equal")

# ------------------------------------ the hi-resolution case

    print("Call libJIGSAW: case 2b.")

    opts = jigsawpy.jigsaw_jig_t()
    mesh = jigsawpy.jigsaw_msh_t()

    opts.hfun_hmax = 0.010
    opts.mesh_dims = +2
    opts.mesh_rad2 = +1.20

    jigsawpy.lib.jigsaw(opts, geom, mesh)

    fig = plt.figure(2)
    axi = fig.add_subplot(1, 1, 1)
    axi.triplot(tri.Triangulation(
        mesh.vert2["coord"][:, 0],
        mesh.vert2["coord"][:, 1],
        mesh.tria3["index"]), linewidth=0.500)

    vert = geom.vert2["coord"]
    edge = geom.edge2["index"]
    eONE = vert[edge[:, 0], :]
    eTWO = vert[edge[:, 1], :]
    line = LineCollection(
        np.stack((eONE, eTWO), axis=1), color="k")
    axi.add_collection(line)
    plt.axis("equal")

    if savefigs:
        plt.figure(1)
        plt.savefig("case_2a.png")
        plt.figure(2)
        plt.savefig("case_2b.png")
    else:
        plt.show()

    return
