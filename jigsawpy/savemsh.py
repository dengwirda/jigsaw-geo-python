
import numpy as np
from  pathlib import Path
from .msh_t   import jigsaw_msh_t
from .certify import certify

def saveradii(mesh,file):
    """
    SAVERADII: save the RADII data structure to file.
    
    """
    if   (mesh.radii.size == +3):
        file.write("RADII="\
            f"{mesh.radii[0]:.16E};" \
            f"{mesh.radii[1]:.16E};" \
            f"{mesh.radii[2]:.16E}\n"\
            )

    elif (mesh.radii.size == +1):
        file.write("RADII="\
            f"{mesh.radii[0]:.16E};" \
            f"{mesh.radii[0]:.16E};" \
            f"{mesh.radii[0]:.16E}\n"\
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
            f"{xpts[ipos,0]:.16E};"  \
            f"{xpts[ipos,1]:.16E};"  \
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
            f"{xpts[ipos,0]:.16E};"  \
            f"{xpts[ipos,1]:.16E};"  \
            f"{xpts[ipos,2]:.16E};"  \
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

    #-- do things here!

    return


def savevalue(mesh,file):
    """
    SAVEVALUE: save the VALUE data structure to file.
    
    """
    npos = np.size(mesh.value,0)
    nval = np.size(mesh.value,1)

    file.write ( "VALUE=" + \
        str(npos) + ";" + str(nval) + "\n")

    #-- do things here!

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
        file.write("# " + name + \
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
    

    
