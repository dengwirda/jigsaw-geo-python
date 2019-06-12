
import numpy as np
from pathlib import Path
from  .msh_t import jigsaw_msh_t

def loadradii(mesh,file,ltag):
    """
    LOADRADII: load the RADII data segment from file.
    
    """
    rtag = ltag[1].split(";")

    mesh.radii = np.empty( \
        +3,dtype=jigsaw_msh_t.REALS_t)

    if   (len(rtag) == +1):    
        mesh.radii[0] = float(rtag[0])
        mesh.radii[1] = float(rtag[0])
        mesh.radii[2] = float(rtag[0])

    elif (len(rtag) == +3):    
        mesh.radii[0] = float(rtag[0])
        mesh.radii[1] = float(rtag[1])
        mesh.radii[2] = float(rtag[2])

    return


def loadpoint(mesh,file,ltag):
    """
    LOADPOINT: load the POINT data segment from file.
    
    """
    if   (mesh.ndims == +2):
        loadvert2(mesh,file,ltag)
    
    elif (mesh.ndims == +3):
        loadvert3(mesh,file,ltag)

    else:
        raise Exception("Unsupported dimension!")
    
    return
    
    
def loadvert2(mesh,file,ltag):
    """
    LOADVERT2: load the 2-dim. vertex pos. from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.vert2 = np.empty( \
        lnum,dtype=jigsaw_msh_t.VERT2_t)

    vpts = mesh.vert2["coord"]
    itag = mesh.vert2["IDtag"]

    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
       
        vpts[next,0] = float(dtag[0])
        vpts[next,1] = float(dtag[1])
        
        itag[next]   = int  (dtag[2])

        lnum -= +1
        next += +1
    
    return
    

def loadvert3(mesh,file,ltag):
    """
    LOADVERT3: load the 3-dim. vertex pos. from file.

    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.vert3 = np.empty( \
        lnum,dtype=jigsaw_msh_t.VERT3_t)

    vpts = mesh.vert3["coord"]
    itag = mesh.vert3["IDtag"]

    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        vpts[next,0] = float(dtag[0])
        vpts[next,1] = float(dtag[1])
        vpts[next,2] = float(dtag[2])
        
        itag[next]   = int  (dtag[3])

        lnum -= +1
        next += +1
        
    return


def loadpower(mesh,file,ltag):
    """
    LOADPOWER: load the POWER data segment from file.
    
    """
    ptag = ltag[ 1].split(";")

    lnum = int(ptag[0])
    pnum = int(ptag[1])
    next = +0
    
    mesh.power = np.empty( \
       [lnum,pnum],dtype=jigsaw_msh_t.REALS_t)

    vpwr = mesh.power[:,:]
   
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        for dpos in range(len(dtag)):
            vpwr[next,dpos]= float(dtag[dpos])
        
        lnum -= +1
        next += +1
        
    return


def loadvalue(mesh,file,ltag):
    """
    LOADVALUE: load the VALUE data segment from file.
    
    """
    vtag = ltag[ 1].split(";")

    lnum = int(vtag[0])
    vnum = int(vtag[1])
    next = +0
    
    mesh.value = np.empty( \
       [lnum,vnum],dtype=jigsaw_msh_t.REALS_t)    

    vals = mesh.value[:,:]

    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        for dpos in range(len(dtag)):
            vals[next,dpos]= float(dtag[dpos])
        
        lnum -= +1
        next += +1
        
    return


def loadedge2(mesh,file,ltag):
    """
    LOADEDGE2: load the EDGE2 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = 0    

    mesh.edge2 = np.empty( \
        lnum,dtype=jigsaw_msh_t.EDGE2_t)

    cell = mesh.edge2["index"]
    itag = mesh.edge2["IDtag"]

    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        cell[next,0] = int  (dtag[0])
        cell[next,1] = int  (dtag[1])
        
        itag[next]   = int  (dtag[2])

        lnum -= +1
        next += +1
        
    return
        
        
def loadtria3(mesh,file,ltag):
    """
    LOADTRIA3: load the TRIA3 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.tria3 = np.empty( \
        lnum,dtype=jigsaw_msh_t.TRIA3_t)

    cell = mesh.tria3["index"]
    itag = mesh.tria3["IDtag"]

    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        cell[next,0] = int  (dtag[0])
        cell[next,1] = int  (dtag[1])
        cell[next,2] = int  (dtag[2])
        
        itag[next]   = int  (dtag[3])

        lnum -= +1
        next += +1
        
    return
        
        
def loadquad4(mesh,file,ltag):
    """
    LOADUAD4: load the QUAD4 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.quad4 = np.empty( \
        lnum,dtype=jigsaw_msh_t.QUAD4_t)

    cell = mesh.quad4["index"]
    itag = mesh.quad4["IDtag"]

    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        cell[next,0] = int  (dtag[0])
        cell[next,1] = int  (dtag[1])
        cell[next,2] = int  (dtag[2])
        cell[next,3] = int  (dtag[3])
        
        itag[next]   = int  (dtag[4])

        lnum -= +1
        next += +1
        
    return
        
        
def loadtria4(mesh,file,ltag):
    """
    LOADTRIA4: load the TRIA4 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.tria4 = np.empty( \
        lnum,dtype=jigsaw_msh_t.TRIA4_t)

    cell = mesh.tria4["index"]
    itag = mesh.tria4["IDtag"]

    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        cell[next,0] = int  (dtag[0])
        cell[next,1] = int  (dtag[1])
        cell[next,2] = int  (dtag[2])
        cell[next,3] = int  (dtag[3])
        
        itag[next]   = int  (dtag[4])

        lnum -= +1
        next += +1
        
    return
    
    
def loadhexa8(mesh,file,ltag):
    """
    LOADHEXA8: load the HEXA8 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.hexa8 = np.empty( \
        lnum,dtype=jigsaw_msh_t.HEXA8_t)

    cell = mesh.hexa8["index"]
    itag = mesh.hexa8["IDtag"]

    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        cell[next,0] = int  (dtag[0])
        cell[next,1] = int  (dtag[1])
        cell[next,2] = int  (dtag[2])
        cell[next,3] = int  (dtag[3])
        cell[next,4] = int  (dtag[4])
        cell[next,5] = int  (dtag[5])
        cell[next,6] = int  (dtag[6])
        cell[next,7] = int  (dtag[7])
        
        itag[next]   = int  (dtag[8])

        lnum -= +1
        next += +1
        
    return


def loadpyra5(mesh,file,ltag):
    """
    LOADPYRA5: load the PYRA5 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.pyra5 = np.empty( \
        lnum,dtype=jigsaw_msh_t.PYRA5_t)

    cell = mesh.pyra5["index"]
    itag = mesh.pyra5["IDtag"]

    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        cell[next,0] = int  (dtag[0])
        cell[next,1] = int  (dtag[1])
        cell[next,2] = int  (dtag[2])
        cell[next,3] = int  (dtag[3])
        cell[next,4] = int  (dtag[4])
        
        itag[next]   = int  (dtag[5])

        lnum -= +1
        next += +1
        
    return


def loadwedg6(mesh,file,ltag):
    """
    LOADWEDG6: load the WEDG6 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.wedg6 = np.empty( \
        lnum,dtype=jigsaw_msh_t.WEDG6_t)

    cell = mesh.wedg6["index"]
    itag = mesh.wedg6["IDtag"]

    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        cell[next,0] = int  (dtag[0])
        cell[next,1] = int  (dtag[1])
        cell[next,2] = int  (dtag[2])
        cell[next,3] = int  (dtag[3])
        cell[next,4] = int  (dtag[4])
        cell[next,5] = int  (dtag[5])
        
        itag[next]   = int  (dtag[6])

        lnum -= +1
        next += +1
        
    return


def loadbound(mesh,file,ltag):
    """
    LOADBOUND: load the BOUND data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.bound = np.empty( \
        lnum,dtype=jigsaw_msh_t.BOUND_t)

    itag = mesh.bound["IDtag"]
    indx = mesh.bound["index"]
    kind = mesh.bound["cells"]

    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
    
        itag[next]   = int  (dtag[0])
        indx[next]   = int  (dtag[1])
        kind[next]   = int  (dtag[2])

        lnum -= +1
        next += +1
        
    return


def loadcoord(mesh,file,ltag):
    """
    LOADCOORD: load the COORD data segment from file.
    
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
    LOADXGRID: load the XGRID data segment from file.
    
    """
    idim = int(ctag[0])
    lnum = int(ctag[1])
    next = +0
    
    mesh.xgrid = np.empty( \
        lnum,dtype=jigsaw_msh_t.REALS_t)
    

    xpts = mesh.xgrid[:]

    while (lnum >= +1):
        xpts[next] = float(file.readline())
    
        lnum -= +1
        next += +1

    return


def loadygrid(mesh,file,ctag):
    """
    LOADYGRID: load the YGRID data segment from file.
    
    """
    idim = int(ctag[0])
    lnum = int(ctag[1])
    next = +0
    
    mesh.ygrid = np.empty( \
        lnum,dtype=jigsaw_msh_t.REALS_t)
    
    ypts = mesh.ygrid[:]

    while (lnum >= +1):
        ypts[next] = float(file.readline())
    
        lnum -= +1
        next += +1

    return


def loadzgrid(mesh,file,ctag):
    """
    LOADZGRID: load the ZGRID data segment from file.
    
    """
    idim = int(ctag[0])
    lnum = int(ctag[1])
    next = +0
    
    mesh.zgrid = np.empty( \
        lnum,dtype=jigsaw_msh_t.REALS_t)

    zpts = mesh.zgrid[:]

    while (lnum >= +1):
        zpts[next] = float(file.readline())
    
        lnum -= +1
        next += +1

    return
        
        
def loadlines(mesh,file,line):
    """
    LOADLINES: load the next non-null line from file.
    
    """
    
    #------------------------------ skip any 'comment' lines
   
    if (line[0] != '#'):
    
    #------------------------------ split about '=' charact.
        ltag = line.split("=")
        kind = ltag[0].upper()
        
        if   (kind == "MSHID"):
        
    #----------------------------------- parse MSHID struct.
            data = ltag[1].split(";")

            if (len(data) > 1):
                mesh.mshID = \
            data[1].strip().lower()
            
        elif (kind == "NDIMS"):
        
    #----------------------------------- parse NDIMS struct.
            mesh.ndims = int(ltag[1])
        
        elif (kind == "RADII"):
    
    #----------------------------------- parse RADII struct.
            loadradii(mesh,file,ltag)
    
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
    LOADMSH: load a JIGSAW MSH obj. from file.

    LOADMSH(NAME,MESH)

    MESH is JIGSAW's primary mesh/grid/geom class. See MSH_t
    for details.

    Data in MESH is loaded on-demand -- any objects included
    in the file will be read.
    
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



