
from msh_t import *

def certifyradii(data,stag):

    if (data.size != +3):
        raise Exception("Invalid "+stag+" size.")
    
    if (data.ndim != +1):
        raise Exception("Invalid "+stag+" size.")

    if (data.dtype is not  np.float64 ):
        raise Exception("Invalid "+stag+" data.")

    if (np.any(not np.isfinite(data)) ):
        raise Exception("Invalid "+stag+" data.")

    if (np.any(data <= 0.)):
        raise Exception("Invalid "+stag+" data.")

    return


def certifypoint(data,stag):

    if (np.size(data.coord,0) \
    !=  np.size(data.IDtag,0)):
        raise Exception("Invalid "+stag+" size.")

    if (data.coord.ndim != +2):
        raise Exception("Invalid "+stag+" size.")

    if (data.IDtag.ndim != +1):
        raise Exception("Invalid "+stag+" size.")

    if (np.size(data.coord,1) \
            not in (+2, +3) ):
        raise Exception("Invalid "+stag+" size.")

    if (data.coord.dtype \
            is not  np.float64 ):
        raise Exception("Invalid "+stag+" data.")

    if (data.IDtag.dtype \
            is not  np.  int32 ):
        raise Exception("Invalid "+stag+" data.")

    if (np.any(not np.isfinite( \
            data.coord)) ):
        raise Exception("Invalid "+stag+" data.")

    if (np.any(not np.isfinite( \
            data.IDtag)) ):
        raise Exception("Invalid "+stag+" data.")

    return


def certifyvalue(vals,stag,nval):

    if (vals.ndim != +2):
        raise Exception("Invalid "+stag+" size.")

    if (vals.dtype is not  np.float64 ):
        raise Exception("Invalid "+stag+" data.")

    if (np.any(not np.isfinite(vals)) ):
        raise Exception("Invalid "+stag+" data.")

    return


def certifycells(cell,stag,nidx):

    if (np.size(cell.index,0) \
    !=  np.size(cell.IDtag,0)):
        raise Exception("Invalid "+stag+" size.")

    if (np.size(cell.index,1) != nidx):
        raise Exception("Invalid "+stag+" size.")

    if (cell.index.ndim != +2):
        raise Exception("Invalid "+stag+" size.")

    if (cell.IDtag.ndim != +1):
        raise Exception("Invalid "+stag+" size.")

    if (cell.index.dtype \
            is not  np.  int32 ):
        raise Exception("Invalid "+stag+" data.")

    if (cell.IDtag.dtype \
            is not  np.  int32 ):
        raise Exception("Invalid "+stag+" data.")

    if (np.any(not np.isfinite( \
            cell.index)) ):
        raise Exception("Invalid "+stag+" data.")

    if (np.any(cell.index < +0)):
        raise Exception("Invalid "+stag+" data.")

    if (np.any(not np.isfinite( \
            cell.IDtag)) ):
        raise Exception("Invalid "+stag+" data.")

    return


def certifyindex(data,stag,nidx):

    if (np.size(data.index,1) != nidx):
        raise Exception("Invalid "+stag+" size.")

    if (data.index.dtype \
            is not  np.  int32 ):
        raise Exception("Invalid "+stag+" data.")

    if (np.any(not np.isfinite( \
            data.index)) ):
        raise Exception("Invalid "+stag+" data.")

    if (np.any(data.index < +0)):
        raise Exception("Invalid "+stag+" data.")

    return


def certifymesht(mesh):

    if (mesh.radii is not None and \
        mesh.radii.size != +0 ):

        certifyradii(mesh.radii,"MESH.RADII")

    if (mesh.point is not None and \
       (mesh.point.coord.size != +0 or  \
        mesh.point.IDtag.size != +0)):

        certifypoint(mesh.point,"MESH.POINT")

    if (mesh.power is not None and \
        mesh.power.size != +0 ):

        certifyvalue(mesh.power,"MESH.POWER")

    if (mesh.value is not None and \
        mesh.value.size != +0 ):

        certifyvalue(mesh.value,"MESH.VALUE")

    if (mesh.edge2 is not None and \
       (mesh.edge2.index.size != +0 or  \
        mesh.edge2.IDtag.size != +0)):

        certifycells(mesh.edge2,"MESH.EDGE2",2)

    if (mesh.tria3 is not None and \
       (mesh.tria3.index.size != +0 or  \
        mesh.tria3.IDtag.size != +0)):

        certifycells(mesh.tria3,"MESH.TRIA3",3)

    if (mesh.quad4 is not None and \
       (mesh.quad4.index.size != +0 or  \
        mesh.quad4.IDtag.size != +0)):

        certifycells(mesh.quad4,"MESH.QUAD4",4)

    if (mesh.tria4 is not None and \
       (mesh.tria4.index.size != +0 or  \
        mesh.tria4.IDtag.size != +0)):

        certifycells(mesh.tria4,"MESH.TRIA4",4)

    if (mesh.hexa8 is not None and \
       (mesh.hexa8.index.size != +0 or  \
        mesh.hexa8.IDtag.size != +0)):

        certifycells(mesh.hexa8,"MESH.HEXA8",8)

    if (mesh.wedg6 is not None and \
       (mesh.wedg6.index.size != +0 or  \
        mesh.wedg6.IDtag.size != +0)):

        certifycells(mesh.wedg6,"MESH.WEDG6",6)

    if (mesh.pyra5 is not None and \
       (mesh.pyra5.index.size != +0 or  \
        mesh.pyra5.IDtag.size != +0)):

        certifycells(mesh.pyra5,"MESH.PYRA5",5)

    if (mesh.bound is not None and \
        mesh.bound.index.size != +0 ):

        certifyindex(mesh.bound,"MESH.BOUND",3)

    return


def certifycoord(data,stag):

    if (data.ndim != +1):
        raise Exception("Invalid "+stag+" size.")

    if (data.dtype is not  np.float64 ):
        raise Exception("Invalid "+stag+" data.")

    if (np.any(not np.isfinite(data)) ):
        raise Exception("Invalid "+stag+" data.")

    return


def certifyndmat(data,stag,dims):

    if (data.ndim != len(dims)):
        raise Exception("Invalid "+stag+" size.")

    if (data.size != np.prod(dims)):
        raise Exception("Invalid "+stag+" size.")

    if (data.dtype is not  np.float64 ):
        raise Exception("Invalid "+stag+" data.")

    if (np.any(not np.isfinite(data)) ):
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

        certifyndmat(mesh.value,"MESH.VALUE", \
                     dims)

    return


def certify(mesh):

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



