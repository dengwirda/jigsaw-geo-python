
import numpy as np
from .msh_t import jigsaw_msh_t

def certifyradii(data,stag):

    if (data.size != +3):
        raise Exception("Invalid "+stag+" size.")
    
    if (data.ndim != +1):
        raise Exception("Invalid "+stag+" size.")

    if (data.dtype != jigsaw_msh_t.REALS_t):
        raise Exception("Invalid "+stag+" type.")

    if (not np.isfinite(data).all()):
        raise Exception("Invalid "+stag+" data.")

    if (np.any(data <= 0.)):
        raise Exception("Invalid "+stag+" data.")

    return


def certifypoint(data,stag,KIND):

    if (data.ndim != +1):
        raise Exception("Invalid "+stag+" size.")

    if (data.dtype != KIND):
        raise Exception("Invalid "+stag+" type.")

    if (not np.isfinite(data["coord"]).all()):
        raise Exception("Invalid "+stag+" data.")

    if (not np.isfinite(data["IDtag"]).all()):
        raise Exception("Invalid "+stag+" data.")

    return


def certifyvalue(vals,stag,nval):

    if (vals.ndim != +2):
        raise Exception("Invalid "+stag+" size.")

    if (vals.dtype != jigsaw_msh_t.REALS_t):
        raise Exception("Invalid "+stag+" type.")

    if (not np.isfinite(data).all()):
        raise Exception("Invalid "+stag+" data.")

    return


def certifycells(cell,stag,KIND):

    if (cell.ndim != +1):
        raise Exception("Invalid "+stag+" size.")

    if (cell.dtype != KIND):
        raise Exception("Invalid "+stag+" type.")

    if (not np.isfinite(cell["index"]).all()):
        raise Exception("Invalid "+stag+" data.")

    if (np.any(cell["index"] < +0)):
        raise Exception("Invalid "+stag+" data.")

    if (not np.isfinite(cell["IDtag"]).all()):
        raise Exception("Invalid "+stag+" data.")

    return


def certifyindex(data,stag,KIND):

    if (data.ndim != +1):
        raise Exception("Invalid "+stag+" size.")

    if (cell.dtype != KIND):
        raise Exception("Invalid "+stag+" type.")

    if (not np.isfinite(cell["IDtag"]).all()):
        raise Exception("Invalid "+stag+" data.")

    if (not np.isfinite(cell["index"]).all()):
        raise Exception("Invalid "+stag+" data.")

    if (not np.isfinite(cell["cells"]).all()):
        raise Exception("Invalid "+stag+" data.")

    if (np.any(data < +0)):
        raise Exception("Invalid "+stag+" data.")

    return


def certifymesht(mesh):

    if (mesh.radii is not None and \
        mesh.radii.size != +0 ):

        certifyradii(mesh.radii,"MESH.RADII")

    if (mesh.vert2 is not None and \
        mesh.vert2.size != +0 ):

        certifypoint(mesh.vert2,"MESH.VERT2", \
            jigsaw_msh_t.VERT2_t)

    if (mesh.vert3 is not None and \
        mesh.vert3.size != +0 ):

        certifypoint(mesh.vert3,"MESH.VERT3", \
            jigsaw_msh_t.VERT3_t)

    if (mesh.power is not None and \
        mesh.power.size != +0 ):

        certifyvalue(mesh.power,"MESH.POWER")

    if (mesh.value is not None and \
        mesh.value.size != +0 ):

        certifyvalue(mesh.value,"MESH.VALUE")

    if (mesh.edge2 is not None and \
        mesh.edge2.size != +0 ):

        certifycells(mesh.edge2,"MESH.EDGE2", \
            jigsaw_msh_t.EDGE2_t)

    if (mesh.tria3 is not None and \
        mesh.tria3.size != +0 ):

        certifycells(mesh.tria3,"MESH.TRIA3", \
            jigsaw_msh_t.TRIA3_t)

    if (mesh.quad4 is not None and \
        mesh.quad4.size != +0 ):

        certifycells(mesh.quad4,"MESH.QUAD4", \
            jigsaw_msh_t.QUAD4_t)

    if (mesh.tria4 is not None and \
        mesh.tria4.size != +0 ):

        certifycells(mesh.tria4,"MESH.TRIA4", \
            jigsaw_msh_t.TRIA4_t)

    if (mesh.hexa8 is not None and \
        mesh.hexa8.size != +0 ):

        certifycells(mesh.hexa8,"MESH.HEXA8", \
            jigsaw_msh_t.HEXA8_t)

    if (mesh.wedg6 is not None and \
        mesh.wedg6.size != +0 ):

        certifycells(mesh.wedg6,"MESH.WEDG6", \
            jigsaw_msh_t.WEDG6_t)

    if (mesh.pyra5 is not None and \
        mesh.pyra5.size != +0 ):

        certifycells(mesh.pyra5,"MESH.PYRA5", \
            jigsaw_msh_t.PYRA5_t)

    if (mesh.bound is not None and \
        mesh.bound.size != +0 ):

        certifyindex(mesh.bound,"MESH.BOUND", \
            jigsaw_msh_t.BOUND_t)

    return


def certifycoord(data,stag):

    if (data.ndim != +1):
        raise Exception("Invalid "+stag+" size.")

    if (data.dtype != jigsaw_msh_t.REALS_t):
        raise Exception("Invalid "+stag+" type.")

    if (not np.isfinite(data).all()):
        raise Exception("Invalid "+stag+" data.")

    return


def certifyNDmat(data,stag,dims):

    if (data.ndim != len(dims)):
        raise Exception("Invalid "+stag+" size.")

    if (data.size != np.prod(dims)):
        raise Exception("Invalid "+stag+" size.")

    if (data.dtype != jigsaw_msh_t.REALS_t):
        raise Exception("Invalid "+stag+" type.")

    if (not np.isfinite(data).all()):
        raise Exception("Invalid "+stag+" data.")

    return


def certifygridt(mesh):

    dims = []

    if (mesh.radii is not None and \
        mesh.radii.size != +0 ):

        certifyradii(mesh.radii,"MESH.RADII")

    if (mesh.xgrid is not None and \
        mesh.xgrid.size != +0 ):

        dims +=[mesh.xgrid.size]

        certifycoord(mesh.xgrid,"MESH.XGRID")

    if (mesh.ygrid is not None and \
        mesh.ygrid.size != +0 ):

        dims +=[mesh.ygrid.size]

        certifycoord(mesh.ygrid,"MESH.YGRID")

    if (mesh.zgrid is not None and \
        mesh.zgrid.size != +0 ):

        dims +=[mesh.zgrid.size]

        certifycoord(mesh.zgrid,"MESH.ZGRID")

    if (mesh.value is not None and \
        mesh.value.size != +0 ):

        certifyNDmat(mesh.value,"MESH.VALUE", \
                     dims)

    return


def certify(mesh):
    """
    CERTIFY: certify layout for a JIGSAW MSH object.
    
    """

    if (mesh is None): return

    if (not isinstance (mesh,jigsaw_msh_t)):
        raise Exception("Invalid MESH structure.")

    if (not isinstance (mesh.mshID,str)):
        raise Exception("Invalid MESH.MSHID tag.")

    if (mesh.mshID.lower() \
            in ["euclidean-mesh","ellipsoid-mesh"
                    ]   ):
    #---------------------------------- certify MESH struct.
        certifymesht(mesh)
                  
    elif (mesh.mshID.lower() \
            in ["euclidean-grid","ellipsoid-grid"
                    ]   ):
    #---------------------------------- certify GRID struct.
        certifygridt(mesh)

    else:
        raise Exception("Invalid MESH.MSHID tag.")
 
    return



