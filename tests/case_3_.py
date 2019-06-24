
"""
* DEMO-3 -- generate a grid for the Australian region, using
*   scaled ocean-depth as a mesh-spacing indicator.
*
* These examples call to JIGSAW via its cmd.-line interface.
*
"""

from pathlib import Path
import numpy as np

import jigsawpy

import matplotlib.pyplot as plt
import matplotlib.tri as tri
from matplotlib.collections import LineCollection


def case_3_(filepath, savefigs=False):

    opts = jigsawpy.jigsaw_jig_t()

    topo = jigsawpy.jigsaw_msh_t()
    geom = jigsawpy.jigsaw_msh_t()
    hmat = jigsawpy.jigsaw_msh_t()
    mesh = jigsawpy.jigsaw_msh_t()

# ------------------------------------ setup files for JIGSAW

    opts.geom_file = \
        str(Path(filepath) / "aust.msh")  # GEOM file

    opts.jcfg_file = \
        str(Path(filepath) / "aust.jig")  # JCFG file

    opts.mesh_file = \
        str(Path(filepath) / "mesh.msh")  # MESH file

    opts.hfun_file = \
        str(Path(filepath) / "hfun.msh")  # HFUN file

# ------------------------------------ setup TOPO for spacing

    print("Load topo-data: case 3a.")

    geom_file = \
        str(Path(filepath) / "aust.msh")

    topo_file = \
        str(Path(filepath) / "topo.msh")

    jigsawpy.loadmsh(geom_file, geom)
    jigsawpy.loadmsh(topo_file, topo)

    topo.value = topo.value.reshape(
        (topo.xgrid.size, topo.ygrid.size)).T

    xgeo = geom.vert2["coord"][:, 0]
    ygeo = geom.vert2["coord"][:, 1]

    xmin = xgeo.min()
    xmax = xgeo.max()
    ymin = ygeo.min()
    ymax = ygeo.max()

    ipos = np.argwhere(
        np.logical_and(
            topo.xgrid >= xmin, topo.xgrid <= xmax))

    ione = int(ipos[+1] - 1)
    iend = int(ipos[-1] + 2)

    jpos = np.argwhere(
        np.logical_and(
            topo.ygrid >= ymin, topo.ygrid <= ymax))

    jone = int(jpos[+1] - 1)
    jend = int(jpos[-1] + 2)

# ------------------------------------ compute HFUN over TOPO

    hmat.mshID = "euclidean-grid"
    hmat.xgrid = np.array(
        topo.xgrid[ione:iend],
        dtype=jigsawpy.jigsaw_msh_t.REALS_t)
    hmat.ygrid = np.array(
        topo.ygrid[jone:jend],
        dtype=jigsawpy.jigsaw_msh_t.REALS_t)
    hmat.value = np.array(
        topo.value[jone:jend, ione:iend],
        dtype=jigsawpy.jigsaw_msh_t.REALS_t)

    hmat.value = np.sqrt(
        np.maximum(-hmat.value, +0.0))
    hmat.value *= 2.

    hmat.value = \
        np.maximum(hmat.value, +10.)
    hmat.value = \
        np.minimum(hmat.value, +100.)

    hmat.value /= 100.

    jigsawpy.savemsh(opts.hfun_file, hmat)

# ------------------------------------ build mesh via JIGSAW!

    opts.hfun_scal = "absolute"
    opts.hfun_hmax = float("inf")      # null HFUN limits
    opts.hfun_hmin = float(+0.00)

    opts.mesh_dims = +2                 # 2-dim. simplexes

    opts.mesh_eps1 = +1.00

    opts.optm_qlim = +0.80

    jigsawpy.cmd.jigsaw(opts, mesh)

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

    fig = plt.figure(2)
    plt.contourf(
        hmat.xgrid, hmat.ygrid, hmat.value)
    plt.axis("equal")

    if savefigs:
        plt.figure(1)
        plt.savefig("case_3a.png")
        plt.figure(2)
        plt.savefig("case_3b.png")
    else:
        plt.show()

    return
