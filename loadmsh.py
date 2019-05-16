#    
#   LOADMSH load a *.MSH file for JIGSAW.
#
#   LOADMSH(NAME,MESH)
#
#   The following are optionally read from "NAME.MSH". Enti-
#   ties are loaded if they are present in the file:
#
#   .IF. MESH.MSHID == 'EUCLIDEAN-MESH':
#   -----------------------------------
#
#   MESH.POINT.COORD - [NPxND] array of point coordinates, 
#       where ND is the number of spatial dimenions.
#
#   MESH.POINT.IDTAG - [NPx 1] array of vertex "ID-tags",
#       one ID assigned for each vertex in the mesh.
#
#   MESH.POWER       - [NPx 1] array of vertex "weights", 
#       associated with the dual "power" tessellation.
#
#   MESH.EDGE2.INDEX - [N2x 2] array of indexing for EDGE-2 
#       elements, where INDEX[K,:] is an array of 
#       "point-indices" associated with the K-TH edge.
#
#   MESH.EDGE2.IDTAG - [N2x 1] array of EDGE-2 "ID-tags",
#       one ID assigned for each EDGE-2 in the mesh.
#
#   MESH.TRIA3.INDEX - [N3x 3] array of indexing for TRIA-3 
#       elements, where INDEX[K,:] is an array of 
#       "point-indices" associated with the K-TH cell.
#
#   MESH.TRIA3.IDTAG - [N3x 1] array of TRIA-3 "ID-tags",
#       one ID assigned for each TRIA-3 in the mesh.
#
#   MESH.QUAD4.INDEX - [N4x 4] array of indexing for QUAD-4 
#       elements, where INDEX[K,:] is an array of 
#       "point-indices" associated with the K-TH cell.
#
#   MESH.QUAD4.IDTAG - [N4x 1] array of QUAD-4 "ID-tags",
#       one ID assigned for each QUAD-4 in the mesh.
#
#   MESH.TRIA4.INDEX - [N4x 4] array of indexing for TRIA-4 
#       elements, where INDEX[K,:] is an array of 
#       "point-indices" associated with the K-TH cell.
#
#   MESH.TRIA4.IDTAG - [N4x 1] array of TRIA-4 "ID-tags",
#       one ID assigned for each TRIA-4 in the mesh.
#
#   MESH.HEXA8.INDEX - [N8x 8] array of indexing for HEXA-8 
#       elements, where INDEX[K,:] is an array of 
#       "point-indices" associated with the K-TH cell.
#
#   MESH.HEXA8.IDTAG - [N8x 1] array of HEXA-8 "ID-tags",
#       one ID assigned for each HEXA-8 in the mesh.
#
#   MESH.WEDG6.INDEX - [N6x 6] array of indexing for WEDG-6 
#       elements, where INDEX[K,:] is an array of 
#       "point-indices" associated with the K-TH cell.
#
#   MESH.WEDG6.IDTAG - [N6x 1] array of WEDG-6 "ID-tags",
#       one ID assigned for each WEDG-6 in the mesh.
#
#   MESH.PYRA5.INDEX - [N5x 5] array of indexing for PYRA-5 
#       elements, where INDEX[K,:] is an array of 
#       "point-indices" associated with the K-TH cell.
#
#   MESH.PYRA5.IDTAG - [N5x 1] array of PYRA-5 "ID-tags",
#       one ID assigned for each PYRA-5 in the mesh.
#
#   MESH.BOUND.INDEX - [NBx 3] array of "boundary" indexing
#       in the domain, indicating how elements in the 
#       geometry are associated with various enclosed areas
#       /volumes, herein known as "parts". INDEX[:,1] is an 
#       array of "part" ID's, INDEX[:,2] is an array of 
#       element numbering and INDEX[:,3] is an array of 
#       element "tags", describing which element "kind" is 
#       numbered via INDEX[:,2]. 
#       In the default case, where BOUND is not specified, 
#       all elements in the geometry are assumed to define
#       the boundaries of enclosed "parts".
#
#   MESH.VALUE - [NPxNV] array of "values" associated with
#       the vertices of the mesh.
#
#   .IF. MESH.MSHID == 'ELLIPSOID-MESH':
#   -----------------------------------
#
#   MESH.RADII - [ 3x 1] array of principle ellipsoid radii.
#
#   Additionally, entities described in the 'EUCLIDEAN-MESH'
#   specification are optionally loaded.
#
#   .IF. MESH.MSHID == 'EUCLIDEAN-GRID':
#   .OR. MESH.MSHID == 'ELLIPSOID-GRID':
#   -----------------------------------
#
#   MESH.XGRID - [N1x 1] array of "x-axis" grid coordinates. 
#       Values must increase or decrease monotonically.
#
#   MESH.YGRID - [N2x 1] array of "y-axis" grid coordinates. 
#       Values must increase or decrease monotonically.
#
#   MESH.ZGRID - [N3x 1] array of "z-axis" grid coordinates. 
#       Values must increase or decrease monotonically.
#
#   MESH.VALUE - [NMxNV] array of "values" associated with 
#       the vertices of the grid, where NM is the product of
#       the dimensions of the grid. NV values are associated 
#       with each vertex.
#
#   See also JIGSAW, SAVEMSH
#

#-----------------------------------------------------------
#   Darren Engwirda
#   github.com/dengwirda/jigsaw-python
#   11-May-2019
#   darren.engwirda@columbia.edu
#-----------------------------------------------------------
#

from pathlib import Path
from msh_t   import *
    
def loadradii(mesh,file,ltag):
    """
    LOADRADII: load RADII data segment from file.
    
    """
    rtag = ltag[1].split(";")

    mesh.radii = \
        np.empty (+3, dtype=np.float64)

    if   (len(rtag) == +1):        
        mesh.radii[0]            = float(rtag[0])
        mesh.radii[1]            = float(rtag[0])
        mesh.radii[2]            = float(rtag[0])

    elif (len(rtag) == +3):        
        mesh.radii[0]            = float(rtag[0])
        mesh.radii[1]            = float(rtag[1])
        mesh.radii[2]            = float(rtag[2])

    return


def loadpoint(mesh,file,ltag):
    """
    LOADPOINT: load POINT data segment from file.
    
    """
    lnum = int(ltag[1])
    
    d  = mesh.ndims

    mesh.point = jigsaw_point_t(lnum,d)
    
    if   (d == +2):
        loadvert2(mesh,file)    
    elif (d == +3):
        loadvert3(mesh,file)
    
    return
    
    
def loadvert2(mesh,file):
    """
    LOADVERT2: load 2-dim. vertex pos. from file.
    
    """
    lnum = np.size(mesh.point.coord, 0)
    next = +0
    
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        mesh.point.coord[next,0] = float(dtag[0])
        mesh.point.coord[next,1] = float(dtag[1])
        
        mesh.point.IDtag[next]   = int  (dtag[2])

        lnum -= +1
        next += +1
        
    return
    

def loadvert3(mesh,file):
    """
    LOADVERT3: load 3-dim. vertex pos. from file.

    """
    lnum = np.size(mesh.point.coord, 0)
    next = +0
    
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        mesh.point.coord[next,0] = float(dtag[0])
        mesh.point.coord[next,1] = float(dtag[1])
        mesh.point.coord[next,2] = float(dtag[3])
        
        mesh.point.IDtag[next]   = int  (dtag[2])

        lnum -= +1
        next += +1
        
    return


def loadpower(mesh,file,ltag):
    """
    LOADPOWER: load POWER data segment from file.
    
    """
    ptag = ltag[ 1].split(";")

    lnum = int(ptag[0])
    pnum = int(ptag[1])
    next = +0
    
    mesh.power = np.empty( \
       [lnum,pnum],dtype=np.float64)
    
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        for dpos in range(len(dtag)):
            mesh.power[next,dpos]= float(dtag[dpos])
        
        lnum -= +1
        next += +1
        
    return


def loadvalue(mesh,file,ltag):
    """
    LOADVALUE: load VALUE data segment from file.
    
    """
    vtag = ltag[ 1].split(";")

    lnum = int(vtag[0])
    vnum = int(vtag[1])
    next = +0
    
    mesh.value = np.empty( \
       [lnum,vnum],dtype=np.float64)
    
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        for dpos in range(len(dtag)):
            mesh.value[next,dpos]= float(dtag[dpos])
        
        lnum -= +1
        next += +1
        
    return


def loadedge2(mesh,file,ltag):
    """
    LOADEDGE2: load EDGE2 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.edge2 = jigsaw_cells_t(lnum,2)

    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        mesh.edge2.index[next,0] = int  (dtag[0])
        mesh.edge2.index[next,1] = int  (dtag[1])
        
        mesh.edge2.IDtag[next]   = int  (dtag[2])

        lnum -= +1
        next += +1
        
    return
        
        
def loadtria3(mesh,file,ltag):
    """
    LOADTRIA3: load TRIA3 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.tria3 = jigsaw_cells_t(lnum,3)
    
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        mesh.tria3.index[next,0] = int  (dtag[0])
        mesh.tria3.index[next,1] = int  (dtag[1])
        mesh.tria3.index[next,2] = int  (dtag[2])
        
        mesh.tria3.IDtag[next]   = int  (dtag[3])

        lnum -= +1
        next += +1
        
    return
        
        
def loadquad4(mesh,file,ltag):
    """
    LOADUAD4: load QUAD4 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.quad4 = jigsaw_cells_t(lnum,4)
    
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        mesh.quad4.index[next,0] = int  (dtag[0])
        mesh.quad4.index[next,1] = int  (dtag[1])
        mesh.quad4.index[next,2] = int  (dtag[2])
        mesh.quad4.index[next,3] = int  (dtag[3])
        
        mesh.quad4.IDtag[next]   = int  (dtag[4])

        lnum -= +1
        next += +1
        
    return
        
        
def loadtria4(mesh,file,ltag):
    """
    LOADTRIA4: load TRIA4 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.tria4 = jigsaw_cells_t(lnum,4)
    
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        mesh.tria4.index[next,0] = int  (dtag[0])
        mesh.tria4.index[next,1] = int  (dtag[1])
        mesh.tria4.index[next,2] = int  (dtag[2])
        mesh.tria4.index[next,3] = int  (dtag[3])
        
        mesh.tria4.IDtag[next]   = int  (dtag[4])

        lnum -= +1
        next += +1
        
    return
    
    
def loadhexa8(mesh,file,ltag):
    """
    LOADHEXA8: load HEXA8 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.hexa8 = jigsaw_cells_t(lnum,8)
    
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        mesh.hexa8.index[next,0] = int  (dtag[0])
        mesh.hexa8.index[next,1] = int  (dtag[1])
        mesh.hexa8.index[next,2] = int  (dtag[2])
        mesh.hexa8.index[next,3] = int  (dtag[3])
        mesh.hexa8.index[next,4] = int  (dtag[4])
        mesh.hexa8.index[next,5] = int  (dtag[5])
        mesh.hexa8.index[next,6] = int  (dtag[6])
        mesh.hexa8.index[next,7] = int  (dtag[7])
        
        mesh.hexa8.IDtag[next]   = int  (dtag[8])

        lnum -= +1
        next += +1
        
    return


def loadpyra5(mesh,file,ltag):
    """
    LOADPYRA5: load PYRA5 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.pyra5 = jigsaw_cells_t(lnum,5)
    
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        mesh.pyra5.index[next,0] = int  (dtag[0])
        mesh.pyra5.index[next,1] = int  (dtag[1])
        mesh.pyra5.index[next,2] = int  (dtag[2])
        mesh.pyra5.index[next,3] = int  (dtag[3])
        mesh.pyra5.index[next,4] = int  (dtag[4])
        
        mesh.pyra5.IDtag[next]   = int  (dtag[5])

        lnum -= +1
        next += +1
        
    return


def loadwedg6(mesh,file,ltag):
    """
    LOADWEDG6: load WEDG6 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.wedg6 = jigsaw_cells_t(lnum,6)
    
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        mesh.wedg6.index[next,0] = int  (dtag[0])
        mesh.wedg6.index[next,1] = int  (dtag[1])
        mesh.wedg6.index[next,2] = int  (dtag[2])
        mesh.wedg6.index[next,3] = int  (dtag[3])
        mesh.wedg6.index[next,4] = int  (dtag[4])
        mesh.wedg6.index[next,5] = int  (dtag[5])
        
        mesh.wedg6.IDtag[next]   = int  (dtag[6])

        lnum -= +1
        next += +1
        
    return


def loadbound(mesh,file,ltag):
    """
    LOADBOUND: load BOUND data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.bound = jigsaw_index_t(lnum,3)
    
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        mesh.bound.index[next,0] = int  (dtag[0])
        mesh.bound.index[next,1] = int  (dtag[1])
        mesh.bound.index[next,2] = int  (dtag[2])
    
        lnum -= +1
        next += +1

    return


def loadcoord(mesh,file,ltag):
    """
    LOADCOORD: load COORD data segment from file.
    
    """
    ctag = ltag[ 1].split(";")

    if   (int(ctag[0]) == +1):
        loadxgrid(mesh,file,ctag)
    elif (int(ctag[0]) == +2):
        loadygrid(mesh,file,ctag)
    elif (int(ctag[0]) == +3):
        loadzgrid(mesh,file,ctag)

    return


def loadxgrid(mesh,file,ctag):
    """
    LOADXGRID: load XGRID data segment from file.
    
    """
    idim = int(ctag[0])
    lnum = int(ctag[1])
    next = +0
    
    mesh.xgrid = np.empty (lnum,dtype=np.float64)
    
    while (lnum >= +1):
        mesh.xgrid[next] = float(file.readline())
    
        lnum -= +1
        next += +1

    return


def loadygrid(mesh,file,ctag):
    """
    LOADYGRID: load YGRID data segment from file.
    
    """
    idim = int(ctag[0])
    lnum = int(ctag[1])
    next = +0
    
    mesh.ygrid = np.empty (lnum,dtype=np.float64)
    
    while (lnum >= +1):
        mesh.ygrid[next] = float(file.readline())
    
        lnum -= +1
        next += +1

    return


def loadzgrid(mesh,file,ctag):
    """
    LOADZGRID: load ZGRID data segment from file.
    
    """
    idim = int(ctag[0])
    lnum = int(ctag[1])
    next = +0
    
    mesh.zgrid = np.empty (lnum,dtype=np.float64)
    
    while (lnum >= +1):
        mesh.zgrid[next] = float(file.readline())
    
        lnum -= +1
        next += +1

    return
        
        
def loadlines(mesh,file,line):
    """
    LOADLINES: load next non-null line from file.
    
    """
    
    #------------------------------ skip any 'comment' lines
    
    if (line[0] != '#'):
    
    #------------------------------ split about '=' charact.
        ltag = line.split("=")
        kind = ltag[0].upper()
        
        if   (kind == "MSHID"):
        
    #----------------------------------- parse MSHID struct.
            data = ltag[1].split(";")

            mesh.mshID = \
            data[1].strip().lower()
            
        elif (kind == "NDIMS"):
        
    #----------------------------------- parse NDIMS struct.
            mesh.ndims = int(ltag[1])
        
        elif (kind == "RADII"):
    
    #----------------------------------- parse RADII struct.
            loadardii(mesh,file,ltag)
    
        elif (kind == "POINT"):
    
    #----------------------------------- parse POINT struct.
            loadpoint(mesh,file,ltag)

        elif (kind == "POWER"):
    
    #----------------------------------- parse POWER struct.
            loadpower(mesh,file,ltag)

        elif (kind == "VALUE"):
   
    #----------------------------------- parse VALUE struct.
            loadvalue(mesh,file,ltag)
                
        elif (kind == "EDGE2"):
        
    #----------------------------------- parse EDGE2 struct.
            loadedge2(mesh,file,ltag)
                
        elif (kind == "TRIA3"):
   
    #----------------------------------- parse TRIA3 struct.
            loadtria3(mesh,file,ltag)
                
        elif (kind == "QUAD4"):
   
    #----------------------------------- parse QUAD4 struct.
            loadquad4(mesh,file,ltag)
                
        elif (kind == "TRIA4"):
   
    #----------------------------------- parse TRIA4 struct.
            loadtria4(mesh,file,ltag)
                
        elif (kind == "HEXA8"):
   
    #----------------------------------- parse HEXA8 struct.
            loadhexa8(mesh,file,ltag)

        elif (kind == "PYRA5"):
   
    #----------------------------------- parse PYRA5 struct.
            loadpyra5(mesh,file,ltag)

        elif (kind == "WEDG6"):
   
    #----------------------------------- parse WEDG6 struct.
            loadwedg6(mesh,file,ltag)

        elif (kind == "BOUND"):
   
    #----------------------------------- parse BOUND struct.
            loadbound(mesh,file,ltag)

        elif (kind == "COORD"):
   
    #----------------------------------- parse COORD struct.
            loadcoord(mesh,file,ltag)
        
    return


def loadmsh(name,mesh):
    """
    LOADMSH: load an MSH obj. from file.
    
    """
 
    if (not isinstance(name,str)):
        raise Exception("Incorrect type: NAME.")
        
    if (not isinstance(mesh,jigsaw_msh_t)):
        raise Exception("Incorrect type: MESH.")

    with Path(name).open("r") as file:
        while (True):
        
    #--------------------------- get the next line from file    
            line = file.readline ()
            
            if (len(line) != +0):

    #--------------------------- parse next non-null section
                loadlines(
                    mesh,file,line)                    
            
            else:
    #--------------------------- reached end-of-file: done!!
                break

    return



