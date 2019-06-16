
"""
* DEMO-4 -- generate a "multi-part" mesh of the (contiguous)
*   USA, using state boundaries to partition the mesh.
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

def case_4_(savefigs=False):

    opts = jigsawpy.jigsaw_jig_t()

    topo = jigsawpy.jigsaw_msh_t()
    geom = jigsawpy.jigsaw_msh_t()
    hmat = jigsawpy.jigsaw_msh_t()
    mesh = jigsawpy.jigsaw_msh_t()

#------------------------------------ setup files for JIGSAW

    opts.geom_file = \
        str(Path()/"files"/"us48.msh")  # GEOM file
        
    opts.jcfg_file = \
        str(Path()/"files"/"us48.jig")  # JCFG file
    
    opts.mesh_file = \
        str(Path()/"files"/"mesh.msh")  # MESH file
    
    opts.hfun_file = \
        str(Path()/"files"/"hfun.msh")  # HFUN file

#------------------------------------ build mesh via JIGSAW!

    jigsawpy.loadmsh(
              opts.geom_file,geom)

    opts.hfun_hmax = .005
    
    opts.mesh_dims = +2                 # 2-dim. simplexes
    opts.mesh_eps1 = +1/6.
    
    opts.optm_qlim = +.90

    jigsawpy.cmd.jigsaw(opts,mesh)

    fig = plt.figure(1)
    axi = fig.add_subplot(1,1,1) 
    ttag = mesh.tria3["IDtag"]   
    for ptag in range(ttag.max()):
        pt = ttag == ptag
        if (pt.any()): \
        axi.triplot(tri.Triangulation( \
        mesh.vert2["coord"][:, 0], \
        mesh.vert2["coord"][:, 1], \
        mesh.tria3["index"][pt,:]) , \
    linewidth=0.500,color=np.random.rand(3,))

    vert = geom.vert2["coord"]
    edge = geom.edge2["index"]
    eONE = vert[edge[:, 0], :]
    eTWO = vert[edge[:, 1], :]
    line = LineCollection(
      np.stack((eONE,eTWO),axis=1),color="k") 
    axi.add_collection(line)
    plt.axis("equal")
    
    if savefigs:
        plt.figure(1)
        plt.savefig("case_4_.png")
    else: plt.show ()

    return



