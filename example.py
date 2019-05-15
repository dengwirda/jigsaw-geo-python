
import matplotlib.pyplot as plt
import matplotlib.tri as tri

from jigsaw import *

def example():

    mesh = jigsaw_msh_t()
    opts = jigsaw_jig_t()

    opts.geom_file = str( \
    Path("jigsaw") / Path("geo") / Path("lake.msh") )
    opts.jcfg_file = str( \
    Path("jigsaw") / Path("out") / Path("lake.jig") )
    opts.mesh_file = str( \
    Path("jigsaw") / Path("out") / Path("lake.msh") )

    opts.hfun_hmax = 0.03
    opts.mesh_dims = +2
    opts.optm_iter = +0

    jigsaw(opts,mesh)

    fig = plt.figure
    plt.triplot(tri.Triangulation( \
        mesh.point.coord[:,0], \
        mesh.point.coord[:,1], \
        mesh.tria3.index[:,:]),linewidth=.50)
    plt.axis('equal')
    plt.show()
    
    return



