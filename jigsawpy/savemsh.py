
import numpy as np
from pathlib import Path
from jigsawpy.msh_t import jigsaw_msh_t
from jigsawpy.certify import certify

def saveradii(mesh,file):
    """
    SAVERADII: save the RADII data structure to file.
    
    """
    if   (mesh.radii.size == +3):
        file.write("RADII="\
            f"{mesh.radii[0]:.18G};" \
            f"{mesh.radii[1]:.18G};" \
            f"{mesh.radii[2]:.18G}\n"\
            )

    elif (mesh.radii.size == +1):
        file.write("RADII="\
            f"{mesh.radii[0]:.18G};" \
            f"{mesh.radii[0]:.18G};" \
            f"{mesh.radii[0]:.18G}\n"\
            )

    return


def savevert2(mesh,file):
    """
    SAVEVERT2: save the POINT data structure to file.
    
    """
    file.write("POINT=" \
        + str(mesh.vert2.size) + "\n")

    xpts = mesh.vert2["coord"]
    itag = mesh.vert2["IDtag"]

    for ipos in range(mesh.vert2.size):
        file.write( \
            f"{xpts[ipos,0]:.18G};"  \
            f"{xpts[ipos,1]:.18G};"  \
            f"{itag[ipos  ]}\n"  \
            )

    return


def savevert3(mesh,file):
    """
    SAVEVERT3: save the POINT data structure to file.
    
    """
    file.write("POINT=" \
        + str(mesh.vert3.size) + "\n")

    xpts = mesh.vert3["coord"]
    itag = mesh.vert3["IDtag"]

    for ipos in range(mesh.vert3.size):
        file.write(
            f"{xpts[ipos,0]:.18G};"  \
            f"{xpts[ipos,1]:.18G};"  \
            f"{xpts[ipos,2]:.18G};"  \
            f"{itag[ipos  ]}\n" \
            )

    return


def savepower(mesh,file):
    """
    SAVEPOWER: save the POWER data structure to file.
    
    """
    npos = np.size(mesh.power,0)
    npwr = np.size(mesh.power,1)

    file.write ( "POWER=" + \
        str(npos) + ";" + str(npwr) + "\n")

    data = mesh.power[:]

    for ipos in range(mesh.power.size):
        fstr = ""
        for ipwr in range(npwr-1):
            fstr = fstr + \
            f"{data[ipos,ipwr]:.18G};"
        fstr = fstr + \
            f"{data[ipos,npwr]:.18G}\n"

        file.write(fstr)

    return


def savevalue(mesh,file):
    """
    SAVEVALUE: save the VALUE data structure to file.
    
    """
    npos = np.size(mesh.value,0)
    nval = np.size(mesh.value,1)

    file.write ( "VALUE=" + \
        str(npos) + ";" + str(nval) + "\n")

    data = mesh.value[:]

    for ipos in range(mesh.value.size):
        fstr = ""
        for ival in range(nval-1):
            fstr = fstr + \
            f"{data[ipos,ival]:.18G};"
        fstr = fstr + \
            f"{data[ipos,nval]:.18G}\n"

        file.write(fstr)

    return


def saveedge2(mesh,file):
    """
    SAVEEDGE2: save the EDGE2 data structure to file.
    
    """
    file.write("EDGE2=" \
        + str(mesh.edge2.size) + "\n")

    cell = mesh.edge2["index"]
    itag = mesh.edge2["IDtag"]

    for ipos in range(mesh.edge2.size):
        file.write( \
            f"{cell[ipos,0]};"  \
            f"{cell[ipos,1]};"  \
            f"{itag[ipos  ]}\n" \
            )

    return


def savetria3(mesh,file):
    """
    SAVETRIA3: save the TRIA3 data structure to file.
    
    """
    file.write("TRIA3=" \
        + str(mesh.tria3.size) + "\n")

    cell = mesh.tria3["index"]
    itag = mesh.tria3["IDtag"]

    for ipos in range(mesh.tria3.size):
        file.write( \
            f"{cell[ipos,0]};"  \
            f"{cell[ipos,1]};"  \
            f"{cell[ipos,2]};"  \
            f"{itag[ipos  ]}\n" \
            )

    return


def savequad4(mesh,file):
    """
    SAVEQUAD4: save the QUAD4 data structure to file.
    
    """
    file.write("QUAD4=" \
        + str(mesh.quad4.size) + "\n")

    cell = mesh.quad4["index"]
    itag = mesh.quad4["IDtag"]

    for ipos in range(mesh.quad4.size):
        file.write( \
            f"{cell[ipos,0]};"  \
            f"{cell[ipos,1]};"  \
            f"{cell[ipos,2]};"  \
            f"{cell[ipos,3]};"  \
            f"{itag[ipos  ]}\n" \
            )

    return


def savetria4(mesh,file):
    """
    SAVETRIA4: save the TRIA4 data structure to file.
    
    """
    file.write("TRIA4=" \
        + str(mesh.tria4.size) + "\n")

    cell = mesh.tria4["index"]
    itag = mesh.tria4["IDtag"]

    for ipos in range(mesh.tria4.size):
        file.write( \
            f"{cell[ipos,0]};"  \
            f"{cell[ipos,1]};"  \
            f"{cell[ipos,2]};"  \
            f"{cell[ipos,3]};"  \
            f"{itag[ipos  ]}\n" \
            )

    return


def savehexa8(mesh,file):
    """
    SAVEHEXA8: save the HEXA8 data structure to file.
    
    """
    file.write("HEXA8=" \
        + str(mesh.hexa8.size) + "\n")

    cell = mesh.hexa8["index"]
    itag = mesh.hexa8["IDtag"]

    for ipos in range(mesh.hexa8.size):
        file.write( \
            f"{cell[ipos,0]};"  \
            f"{cell[ipos,1]};"  \
            f"{cell[ipos,2]};"  \
            f"{cell[ipos,3]};"  \
            f"{cell[ipos,4]};"  \
            f"{cell[ipos,5]};"  \
            f"{cell[ipos,6]};"  \
            f"{cell[ipos,7]};"  \
            f"{itag[ipos  ]}\n" \
            )

    return


def savewedg6(mesh,file):
    """
    SAVEWEDG6: save the WEDG6 data structure to file.
    
    """
    file.write("WEDG6=" \
        + str(mesh.wedg6.size) + "\n")

    cell = mesh.wedg6["index"]
    itag = mesh.wedg6["IDtag"]

    for ipos in range(mesh.wedg6.size):
        file.write( \
            f"{cell[ipos,0]};"  \
            f"{cell[ipos,1]};"  \
            f"{cell[ipos,2]};"  \
            f"{cell[ipos,3]};"  \
            f"{cell[ipos,4]};"  \
            f"{cell[ipos,5]};"  \
            f"{itag[ipos  ]}\n" \
            )

    return


def savepyra5(mesh,file):
    """
    SAVEPYRA5: save the PYRA5 data structure to file.
    
    """
    file.write("PYRA5=" \
        + str(mesh.pyra5.size) + "\n")

    cell = mesh.pyra5["index"]
    itag = mesh.pyra5["IDtag"]

    for ipos in range(mesh.pyra5.size):
        file.write( \
            f"{cell[ipos,0]};"  \
            f"{cell[ipos,1]};"  \
            f"{cell[ipos,2]};"  \
            f"{cell[ipos,3]};"  \
            f"{cell[ipos,4]};"  \
            f"{itag[ipos  ]}\n" \
            )

    return


def savebound(mesh,file):
    """
    SAVEBOUND: save the BOUND data structure to file.
    
    """
    file.write("BOUND=" \
        + str(mesh.bound.size) + "\n")

    itag = mesh.bound["IDtag"]
    indx = mesh.bound["index"]
    kind = mesh.bound["cells"]

    for ipos in range(mesh.bound.size):
        file.write( \
            f"{itag[ipos  ]};"  \
            f"{indx[ipos  ]};"  \
            f"{kind[ipos  ]}\n" \
            )

    return


def savecoord(data,file,inum):
    """
    SAVECOORD: save the COORD data structure to file.
    
    """
    file.write("COORD=" \
        + str(inum) + ";" + str(data.size) + "\n")

    for ipos in range(data.size):
        file.write(f"{data[ipos]:.18G}\n"
            )

    return


def savendmat(data,file):
    """
    SAVENDMAT: save the VALUE data structure to file.
    
    """
    file.write("VALUE=" \
        + str(np.prod(data.shape)) + ";+1" + "\n")

    for iter in np.nditer(data,order="F"):
        file.write(f"{iter:.18G}\n")

    return


def save_mesh_file(mesh,file,nver,kind):

    file.write("MSHID=" + str(nver) + ";" + kind + "\n")

    if (mesh.vert2 is not None and \
        mesh.vert2.size != +0):

    #----------------------------------- write NDIMS struct.
        file.write("NDIMS=2\n")

    if (mesh.vert3 is not None and \
        mesh.vert3.size != +0):

    #----------------------------------- write NDIMS struct.
        file.write("NDIMS=3\n")

    if (mesh.radii is not None and \
        mesh.radii.size != +0):

    #----------------------------------- write RADII struct.
        saveradii(mesh,file)
 
    if (mesh.vert2 is not None and \
        mesh.vert2.size != +0):

    #----------------------------------- write VERT2 struct.
        savevert2(mesh,file)

    if (mesh.vert3 is not None and \
        mesh.vert3.size != +0):

    #----------------------------------- write VERT3 struct.
        savevert3(mesh,file)

    if (mesh.power is not None and \
        mesh.power.size != +0):

    #----------------------------------- write POWER struct.
        savepower(mesh,file)

    if (mesh.value is not None and \
        mesh.value.size != +0):

    #----------------------------------- write VALUE struct.
        savevalue(mesh,file)

    if (mesh.edge2 is not None and \
        mesh.edge2.size != +0):

    #----------------------------------- write EDGE2 struct.
        saveedge2(mesh,file)

    if (mesh.tria3 is not None and \
        mesh.tria3.size != +0):

    #----------------------------------- write TRIA3 struct.
        savetria3(mesh,file)

    if (mesh.quad4 is not None and \
        mesh.quad4.size != +0):

    #----------------------------------- write QUAD4 struct.
        savequad4(mesh,file)

    if (mesh.tria4 is not None and \
        mesh.tria4.size != +0):

    #----------------------------------- write TRIA4 struct.
        savetria4(mesh,file)

    if (mesh.hexa8 is not None and \
        mesh.hexa8.size != +0):

    #----------------------------------- write HEXA8 struct.
        savehexa8(mesh,file)

    if (mesh.wedg6 is not None and \
        mesh.wedg6.size != +0):

    #----------------------------------- write WEDG6 struct.
        savewedg6(mesh,file)

    if (mesh.pyra5 is not None and \
        mesh.pyra5.size != +0):

    #----------------------------------- write PYRA5 struct.
        savepyra5(mesh,file)

    if (mesh.bound is not None and \
        mesh.bound.size != +0):

    #----------------------------------- write BOUND struct.
        savebound(mesh,file)
        

    return


def save_grid_file(mesh,file,nver,kind):

    file.write("MSHID=" + str(nver) + ";" + kind + "\n")

    if (mesh.radii is not None and \
        mesh.radii.size != +0):

    #----------------------------------- write RADII struct.
        saveradii(mesh.radii,file)

    #----------------------------------- calc. NDIMS struct.
    ndim =  +0

    if (mesh.xgrid is not None and \
        mesh.xgrid.size != +0):

        ndim += +1

    if (mesh.ygrid is not None and \
        mesh.ygrid.size != +0):

        ndim += +1

    if (mesh.zgrid is not None and \
        mesh.zgrid.size != +0):

        ndim += +1

    if (ndim >= +1):
    #----------------------------------- write NDIMS struct.
        file.write(
        "NDIMS=" + str(ndim) + "\n")


    if (mesh.xgrid is not None and \
        mesh.xgrid.size != +0):

    #----------------------------------- write XGRID struct.
        savecoord(mesh.xgrid,file,1)

    if (mesh.ygrid is not None and \
        mesh.ygrid.size != +0):

    #----------------------------------- write YGRID struct.
        savecoord(mesh.ygrid,file,2)

    if (mesh.zgrid is not None and \
        mesh.zgrid.size != +0):

    #----------------------------------- write ZGRID struct.
        savecoord(mesh.zgrid,file,3)

    if (mesh.value is not None and \
        mesh.value.size != +0):

    #----------------------------------- write VALUE struct.
        savendmat(mesh.value,file)

    return


def savemsh(name,mesh):
    """
    SAVEMSH: save a JIGSAW MSH object to file.

    SAVEMESH(NAME,MESH)

    MESH is JIGSAW's primary mesh/grid/geom class. See MSH_t
    for details.

    Data in MESH is written as-needed -- any objects defined
    will be saved to file.
    
    """

    if (not isinstance(name,str)):
        raise Exception("Incorrect type: NAME.")
        
    if (not isinstance(mesh,jigsaw_msh_t)):
        raise Exception("Incorrect type: MESH.")

    nver =  +3

    certify(mesh)

    fext = Path(name).suffix
    
    if (fext.strip() != ".msh"):
        name =   name + ".msh"

    kind = mesh.mshID.lower()

    with Path(name).open("w") as file:
    #----------------------------------- write JIGSAW object    
        file.write("# " + Path(name).name + \
    "; created by JIGSAW's PYTHON interface \n")
   
        if (kind == "euclidean-mesh"):
            save_mesh_file( \
            mesh,file,nver,"euclidean-mesh")

        if (kind == "euclidean-grid"):
            save_grid_file( \
            mesh,file,nver,"euclidean-grid")

        if (kind == "ellipsoid-mesh"):
            save_mesh_file( \
            mesh,file,nver,"ellipsoid-mesh")

        if (kind == "ellipsoid-grid"):
            save_grid_file( \
            mesh,file,nver,"ellipsoid-grid")

    return
    

    
