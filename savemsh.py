
from msh_t import *
import os.path

def savepoint(mesh,file):
    """
    SAVEPOINT: save POINT data struct. to a file.
    
    """
    npos = \
        np.size(mesh.point.coord,0)
    ndim = \
        np.size(mesh.point.coord,1)

    file.write ( "POINT=" + str(npos)+"\n")

    if   (ndim == +2):

        for ipos in range(npos):
            file.write( \
        f"{mesh.point.coord[ipos,0]:.16E};" \
        f"{mesh.point.coord[ipos,1]:.16E};" \
        f"{mesh.point.IDtag[ipos,0]}\n" \
            )

    elif (ndim == +3):

        for ipos in range(npos):
            file.write( \
        f"{mesh.point.coord[ipos,0]:.16E};" \
        f"{mesh.point.coord[ipos,1]:.16E};" \
        f"{mesh.point.coord[ipos,2]:.16E};" \
        f"{mesh.point.IDtag[ipos,0]}\n" \
            )

    return


def savepower(mesh,file):
    """
    SAVEPOWER: save POWER data struct. to a file.
    
    """
    npos = np.size(mesh.power,0)
    npwr = np.size(mesh.power,1)

    file.write ( "POWER=" + \
        str(npos) + ";" + str(npwr) + "\n")

    #-- do things here!

    return


def savevalue(mesh,file):
    """
    SAVEVALUE: save VALUE data struct. to a file.
    
    """
    npos = np.size(mesh.value,0)
    nval = np.size(mesh.value,1)

    file.write ( "VALUE=" + \
        str(npos) + ";" + str(nval) + "\n")

    #-- do things here!

    return


def saveedge2(mesh,file):
    """
    SAVEEDGE2: save EDGE2 data struct. to a file.
    
    """
    npos = \
        np.size(mesh.edge2.index,0)
    nidx = \
        np.size(mesh.edge2.index,1)

    file.write ( "EDGE2=" + str(npos)+"\n")

    if   (nidx == +2):

        for ipos in range(npos):
            file.write( \
        f"{mesh.edge2.index[ipos,0]};" \
        f"{mesh.edge2.index[ipos,1]};" \
        f"{mesh.edge2.IDtag[ipos,0]}\n"\
            )

    return


def savetria3(mesh,file):
    """
    SAVETRIA3: save TRIA3 data struct. to a file.
    
    """
    npos = \
        np.size(mesh.tria3.index,0)
    nidx = \
        np.size(mesh.tria3.index,1)

    file.write ( "TRIA3=" + str(npos)+"\n")

    if   (nidx == +3):

        for ipos in range(npos):
            file.write( \
        f"{mesh.tria3.index[ipos,0]};" \
        f"{mesh.tria3.index[ipos,1]};" \
        f"{mesh.tria3.index[ipos,2]};" \
        f"{mesh.tria3.IDtag[ipos,0]}\n"\
            )

    return


def savequad4(mesh,file):
    """
    SAVEQUAD4: save QUAD4 data struct. to a file.
    
    """
    npos = \
        np.size(mesh.quad4.index,0)
    nidx = \
        np.size(mesh.quad4.index,1)

    file.write ( "QUAD4=" + str(npos)+"\n")

    if   (nidx == +4):

        for ipos in range(npos):
            file.write( \
        f"{mesh.quad4.index[ipos,0]};" \
        f"{mesh.quad4.index[ipos,1]};" \
        f"{mesh.quad4.index[ipos,2]};" \
        f"{mesh.quad4.index[ipos,3]};" \
        f"{mesh.quad4.IDtag[ipos,0]}\n"\
            )

    return


def savetria4(mesh,file):
    """
    SAVETRIA4: save TRIA4 data struct. to a file.
    
    """
    npos = \
        np.size(mesh.tria4.index,0)
    nidx = \
        np.size(mesh.tria4.index,1)

    file.write ( "TRIA4=" + str(npos)+"\n")

    if   (nidx == +4):

        for ipos in range(npos):
            file.write( \
        f"{mesh.tria4.index[ipos,0]};" \
        f"{mesh.tria4.index[ipos,1]};" \
        f"{mesh.tria4.index[ipos,2]};" \
        f"{mesh.tria4.index[ipos,3]};" \
        f"{mesh.tria4.IDtag[ipos,0]}\n"\
            )

    return


def savehexa8(mesh,file):
    """
    SAVEHEXA8: save HEXA8 data struct. to a file.
    
    """
    npos = \
        np.size(mesh.hexa8.index,0)
    nidx = \
        np.size(mesh.hexa8.index,1)

    file.write ( "HEXA8=" + str(npos)+"\n")

    if   (nidx == +8):

        for ipos in range(npos):
            file.write( \
        f"{mesh.hexa8.index[ipos,0]};" \
        f"{mesh.hexa8.index[ipos,1]};" \
        f"{mesh.hexa8.index[ipos,2]};" \
        f"{mesh.hexa8.index[ipos,3]};" \
        f"{mesh.hexa8.index[ipos,4]};" \
        f"{mesh.hexa8.index[ipos,5]};" \
        f"{mesh.hexa8.index[ipos,6]};" \
        f"{mesh.hexa8.index[ipos,7]};" \
        f"{mesh.hexa8.IDtag[ipos,0]}\n"\
            )

    return


def savewedg6(mesh,file):
    """
    SAVEWEDG6: save WEDG6 data struct. to a file.
    
    """
    npos = \
        np.size(mesh.wedg6.index,0)
    nidx = \
        np.size(mesh.wedg6.index,1)

    file.write ( "WEDG6=" + str(npos)+"\n")

    if   (nidx == +6):

        for ipos in range(npos):
            file.write( \
        f"{mesh.wedg6.index[ipos,0]};" \
        f"{mesh.wedg6.index[ipos,1]};" \
        f"{mesh.wedg6.index[ipos,2]};" \
        f"{mesh.wedg6.index[ipos,3]};" \
        f"{mesh.wedg6.index[ipos,4]};" \
        f"{mesh.wedg6.index[ipos,5]};" \
        f"{mesh.wedg6.IDtag[ipos,0]}\n"\
            )

    return


def savepyra5(mesh,file):
    """
    SAVEPYRA5: save PYRA5 data struct. to a file.
    
    """
    npos = \
        np.size(mesh.pyra5.index,0)
    nidx = \
        np.size(mesh.pyra5.index,1)

    file.write ( "PYRA5=" + str(npos)+"\n")

    if   (nidx == +5):

        for ipos in range(npos):
            file.write( \
        f"{mesh.pyra5.index[ipos,0]};" \
        f"{mesh.pyra5.index[ipos,1]};" \
        f"{mesh.pyra5.index[ipos,2]};" \
        f"{mesh.pyra5.index[ipos,3]};" \
        f"{mesh.pyra5.index[ipos,4]};" \
        f"{mesh.pyra5.IDtag[ipos,0]}\n"\
            )

    return


def savebound(mesh,file):
    """
    SAVEBOUND: save BOUND data struct. to a file.
    
    """
    npos = \
        np.size(mesh.bound.index,0)
    nidx = \
        np.size(mesh.bound.index,1)

    file.write ( "BOUND=" + str(npos)+"\n")

    if   (nidx == +3):

        for ipos in range(npos):
            file.write( \
        f"{mesh.bound.index[ipos,0]};" \
        f"{mesh.bound.index[ipos,1]};" \
        f"{mesh.bound.index[ipos,2]}\n"\
            )

    return


def save_mesh_file(mesh,file,nver,kind):

    file.write("MSHID=" + str(nver) + ";" + kind + "\n")

    if (mesh.radii is not None and \
            mesh.radii.size != +0):

    #----------------------------------- write RADII struct.
        fstr = "RADII=" \
             + str(mesh.radii[0])+ ";" \
             + str(mesh.radii[1])+ ";" \
             + str(mesh.radii[2])+"\n"
        
        file.write (fstr)

    if (mesh.point is not None and \
        mesh.point.coord.size != +0):

    #----------------------------------- write POINT struct.
        savepoint(mesh,file)

    if (mesh.power is not None and \
            mesh.power.size != +0):

    #----------------------------------- write POWER struct.
        savepower(mesh,file)

    if (mesh.value is not None and \
            mesh.value.size != +0):

    #----------------------------------- write VALUE struct.
        savevalue(mesh,file)

    if (mesh.edge2 is not None and \
        mesh.edge2.index.size != +0):

    #----------------------------------- write EDGE2 struct.
        saveedge2(mesh,file)

    if (mesh.tria3 is not None and \
        mesh.tria3.index.size != +0):

    #----------------------------------- write TRIA3 struct.
        savetria3(mesh,file)

    if (mesh.quad4 is not None and \
        mesh.quad4.index.size != +0):

    #----------------------------------- write QUAD4 struct.
        savequad4(mesh,file)

    if (mesh.tria4 is not None and \
        mesh.tria4.index.size != +0):

    #----------------------------------- write TRIA4 struct.
        savetria4(mesh,file)

    if (mesh.hexa8 is not None and \
        mesh.hexa8.index.size != +0):

    #----------------------------------- write HEXA8 struct.
        savehexa8(mesh,file)

    if (mesh.wedg6 is not None and \
        mesh.wedg6.index.size != +0):

    #----------------------------------- write WEDG6 struct.
        savewedg6(mesh,file)

    if (mesh.pyra5 is not None and \
        mesh.pyra5.index.size != +0):

    #----------------------------------- write PYRA5 struct.
        savepyra5(mesh,file)

    if (mesh.bound is not None and \
        mesh.bound.index.size != +0):

    #----------------------------------- write BOUND struct.
        savebound(mesh,file)
        

    return


def save_grid_file(mesh,file,nver,kind):

    file.write("MSHID=" + str(nver) + ";" + kind + "\n")

    return


def savemsh(name,mesh):
    """
    SAVEMSH: save a MSH obj. to file.
    
    """

    if (not isinstance(name,str)):
        raise Exception("Incorrect type: NAME.")
        
    if (not isinstance(mesh,jigsaw_msh_t)):
        raise Exception("Incorrect type: MESH.")

    nver =  +3

    fext = os.path.splitext(name)[1]
    
    if (fext.strip() != ".msh"):
        name =   name + ".msh"

    kind = mesh.mshID.lower()

    with open(name,"w") as file:

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
    
    
    
