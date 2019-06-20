
"""
* DEMO-1 --- a simple example demonstrating the construction
*   of PSLG geometry and user-defined mesh-size constraints.
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

def case_1a(savefigs=False):

    opts = jigsawpy.jigsaw_jig_t()

    geom = jigsawpy.jigsaw_msh_t()
    mesh = jigsawpy.jigsaw_msh_t()

#------------------------------------ define JIGSAW geometry
    
    geom.mshID = "euclidean-mesh"
    geom.vert2 = np.array([ # list of xy "node" coordinate
      ((0, 0), 0),          # outer square
      ((9, 0), 0),
      ((9, 9), 0),
      ((0, 9), 0),
      ((4, 4), 0),          # inner square
      ((5, 4), 0),
      ((5, 5), 0),
      ((4, 5), 0)] ,
    dtype=jigsawpy.jigsaw_msh_t.VERT2_t)

    geom.edge2 = np.array([ # list of "edges" between vert
      ((0, 1), 0),          # outer square 
      ((1, 2), 0),
      ((2, 3), 0),
      ((3, 0), 0),
      ((4, 5), 0),          # inner square
      ((5, 6), 0),
      ((6, 7), 0),
      ((7, 4), 0)] ,
    dtype=jigsawpy.jigsaw_msh_t.EDGE2_t)

#------------------------------------ build mesh via JIGSAW! 
  
    print("Call libJIGSAW: case 1a.")

    opts.hfun_hmax = 0.05               # null HFUN limits
   
    opts.mesh_dims = +2                 # 2-dim. simplexes
    
    opts.optm_qlim = +.95  
   
    opts.mesh_top1 = True               # for sharp feat's
    opts.geom_feat = True  
    
    jigsawpy.lib.jigsaw(opts,geom,mesh)  

    fig = plt.figure(1)
    axi = fig.add_subplot(1,1,1)
    axi.triplot(tri.Triangulation( \
        mesh.vert2["coord"][:, 0], \
        mesh.vert2["coord"][:, 1], \
        mesh.tria3["index"]),linewidth=0.500)
    
    vert = geom.vert2["coord"]
    edge = geom.edge2["index"]
    eONE = vert[edge[:, 0], :]
    eTWO = vert[edge[:, 1], :]
    line = LineCollection(
      np.stack((eONE,eTWO),axis=1),color="k") 
    axi.add_collection(line)
    plt.axis("equal")
    
    return


def case_1b(savefigs=False):

    opts = jigsawpy.jigsaw_jig_t()

    geom = jigsawpy.jigsaw_msh_t()
    mesh = jigsawpy.jigsaw_msh_t()

#------------------------------------ define JIGSAW geometry
    
    geom.mshID = "euclidean-mesh"
    geom.vert2 = np.array([ # list of xy "node" coordinate
      ((0, 0), 0),          # outer square
      ((9, 0), 0),
      ((9, 9), 0),
      ((0, 9), 0),
      ((2, 2), 0),          # inner square
      ((7, 2), 0),
      ((7, 7), 0),
      ((2, 7), 0),
      ((3, 3), 0),
      ((6, 6), 0)] ,
    dtype=jigsawpy.jigsaw_msh_t.VERT2_t)

    geom.edge2 = np.array([ # list of "edges" between vert
      ((0, 1), 0),          # outer square 
      ((1, 2), 0),
      ((2, 3), 0),
      ((3, 0), 0),
      ((4, 5), 0),          # inner square
      ((5, 6), 0),
      ((6, 7), 0),
      ((7, 4), 0),
      ((8, 9), 0)] ,
    dtype=jigsawpy.jigsaw_msh_t.EDGE2_t)

    et =  jigsawpy.\
          jigsaw_def_t.JIGSAW_EDGE2_TAG

    geom.bound = np.array([
       (1, 0, et),
       (1, 1, et),
       (1, 2, et),
       (1, 3, et),
       (1, 4, et),
       (1, 5, et),
       (1, 6, et),
       (1, 7, et),
       (2, 4, et),
       (2, 5, et),
       (2, 6, et),
       (2, 7, et)] ,
    dtype=jigsawpy.jigsaw_msh_t.BOUND_t)
    
#------------------------------------ build mesh via JIGSAW! 
  
    print("Call libJIGSAW: case 1b.")

    opts.hfun_hmax = 0.05               # null HFUN limits
    opts.mesh_dims = +2                 # 2-dim. simplexes
    
    opts.optm_qlim = +.95  
   
    opts.mesh_top1 = True               # for sharp feat's
    opts.geom_feat = True  
    
    jigsawpy.lib.jigsaw(opts,geom,mesh)  

    fig = plt.figure(2)
    axi = fig.add_subplot(1,1,1)
    P1= mesh.tria3["IDtag"] == 1        # TRIA in 1st part  
    axi.triplot(tri.Triangulation( \
        mesh.vert2["coord"][:, 0], \
        mesh.vert2["coord"][:, 1], \
    mesh.tria3["index"][P1,:]),linewidth=0.5)
    P2= mesh.tria3["IDtag"] == 2        # TRIA in 2nd part  
    axi.triplot(tri.Triangulation( \
        mesh.vert2["coord"][:, 0], \
        mesh.vert2["coord"][:, 1], \
    mesh.tria3["index"][P2,:]),linewidth=0.5,
        color= "red")

    vert = geom.vert2["coord"]
    edge = geom.edge2["index"]
    eONE = vert[edge[:, 0], :]
    eTWO = vert[edge[:, 1], :]
    line = LineCollection(
      np.stack((eONE,eTWO),axis=1),color="k") 
    axi.add_collection(line)
    plt.axis("equal")

    return


def case_1c(savefigs=False):

    opts = jigsawpy.jigsaw_jig_t()

    geom = jigsawpy.jigsaw_msh_t()
    hmat = jigsawpy.jigsaw_msh_t()
    mesh = jigsawpy.jigsaw_msh_t()

#------------------------------------ define JIGSAW geometry
    
    geom.mshID = "euclidean-mesh"
    geom.vert2 = np.array([ # list of xy "node" coordinate
      ((0, 0), 0),          # outer square
      ((9, 0), 0),
      ((9, 9), 0),
      ((0, 9), 0),
      ((4, 4), 0),          # inner square
      ((5, 4), 0),
      ((5, 5), 0),
      ((4, 5), 0)] ,
    dtype=jigsawpy.jigsaw_msh_t.VERT2_t)

    geom.edge2 = np.array([ # list of "edges" between vert
      ((0, 1), 0),          # outer square 
      ((1, 2), 0),
      ((2, 3), 0),
      ((3, 0), 0),
      ((4, 5), 0),          # inner square
      ((5, 6), 0),
      ((6, 7), 0),
      ((7, 4), 0)] ,
    dtype=jigsawpy.jigsaw_msh_t.EDGE2_t)
   
#------------------------------------ compute HFUN over GEOM    
        
    xgeo = geom.vert2["coord"][:,0]
    ygeo = geom.vert2["coord"][:,1]

    xpos = np.linspace( 
        xgeo.min(),xgeo.max(), 128)
                    
    ypos = np.linspace(
        ygeo.min(),ygeo.max(), 128)

    xmat, ymat = np.meshgrid(xpos, ypos)

    hfun =-.4*np.exp(-.1*(xmat-4.5)**2 \
                     -.1*(ymat-4.5)**2 \
            ) + .6

    hmat.mshID = "euclidean-grid"
    hmat.xgrid = np.array(xpos,
    dtype=jigsawpy.jigsaw_msh_t.REALS_t)
    hmat.ygrid = np.array(ypos,
    dtype=jigsawpy.jigsaw_msh_t.REALS_t)
    hmat.value = np.array(hfun,
    dtype=jigsawpy.jigsaw_msh_t.REALS_t)

#------------------------------------ build mesh via JIGSAW! 
  
    print("Call libJIGSAW: case 1c.")

    opts.hfun_scal = "absolute"
    opts.hfun_hmax = float("inf")       # null HFUN limits
    opts.hfun_hmin = float(+0.00)  
   
    opts.mesh_dims = +2                 # 2-dim. simplexes
    
    opts.optm_qlim = +.95  
   
    opts.mesh_top1 = True               # for sharp feat's
    opts.geom_feat = True  
    
    jigsawpy.lib.jigsaw(opts,geom,mesh,
                        None,hmat)  

    fig = plt.figure(3)
    axi = fig.add_subplot(1,1,1)    
    axi.triplot(tri.Triangulation( \
        mesh.vert2["coord"][:, 0], \
        mesh.vert2["coord"][:, 1], \
        mesh.tria3["index"]),linewidth=0.500)
    
    vert = geom.vert2["coord"]
    edge = geom.edge2["index"]
    eONE = vert[edge[:, 0], :]
    eTWO = vert[edge[:, 1], :]
    line = LineCollection(
      np.stack((eONE,eTWO),axis=1),color="k") 
    axi.add_collection(line)
    plt.axis("equal")

    return


def case_1_(filepath,savefigs=False):

#------------------------------------ build various examples

    case_1a(savefigs)
    case_1b(savefigs)
    case_1c(savefigs)

    if savefigs:
        plt.figure(1)
        plt.savefig("case_1a.png")
        plt.figure(2)
        plt.savefig("case_1b.png")
        plt.figure(3)
        plt.savefig("case_1c.png")
    else: plt.show ()

    return



