
"""
* DEMO-5: generate a uniform resolution (200km) global grid.
*
* These examples call to JIGSAW via its cmd.-line interface.
*
"""

from pathlib import Path
import numpy as np

import jigsawpy
 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.tri as tri

def case_5_(savefigs=False):

    opts = jigsawpy.jigsaw_jig_t()

    geom = jigsawpy.jigsaw_msh_t()
    mesh = jigsawpy.jigsaw_msh_t()

#------------------------------------ setup files for JIGSAW

    opts.geom_file = \
        str(Path()/"files"/"aust.msh")  # GEOM file
        
    opts.jcfg_file = \
        str(Path()/"files"/"aust.jig")  # JCFG file
    
    opts.mesh_file = \
        str(Path()/"files"/"mesh.msh")  # MESH file

#------------------------------------ define JIGSAW geometry
    
    geom.mshID = "ellipsoid-mesh"
    geom.radii = np.array(
        [+6371., +6371., +6371.],
    dtype=jigsawpy.jigsaw_msh_t.REALS_t)

    jigsawpy.savemsh(
              opts.geom_file,geom)

#------------------------------------ build mesh via JIGSAW! 
  
    opts.hfun_scal = "absolute"
    opts.hfun_hmax = +200. 
    
    opts.mesh_dims = +2                 # 2-dim. simplexes

    opts.optm_qlim = +.95

    jigsawpy.cmd.jigsaw(opts,mesh)

    fig = plt.figure(1)
    axi = fig.add_subplot(
    111,aspect="equal",projection="3d")
    axi.plot_trisurf(
        mesh.vert3["coord"][:, 0], \
        mesh.vert3["coord"][:, 1], \
        mesh.vert3["coord"][:, 2], \
    triangles=mesh.tria3["index"], \
    edgecolor="black",color="white", \
    linewidth=0.1000,alpha=0.7500)
    
    if savefigs:
        plt.figure(1)
        plt.savefig("case_5_.png")
    else: plt.show ()
    
    return



