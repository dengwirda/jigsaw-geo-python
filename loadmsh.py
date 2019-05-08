    
from msh_t import *
    
def loadpoint(mesh,file,ltag):
    """
    LOADPOINT: load POINT data segment from file.
    
    """
    lnum = int(ltag[1])
    
    d  = mesh.ndims
    mesh.point.coord.resize(lnum,d)
    mesh.point.IDtag.resize(lnum,1)
    
    if   (d == +2):
        loadvert2(mesh,file)    
    elif (d == +3):
        loadvert3(mesh,file)
    
    return
    
    
def loadvert2(mesh,file):
    """
    LOADVERT2: load 2-dim. vertex pos. from file.
    
    """
    lnum = np.size(mesh.point.coord,0)
    next = +0
    
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        mesh.point.coord[next,0] = float(dtag[0])
        mesh.point.coord[next,1] = float(dtag[1])
        
        mesh.point.IDtag[next,0] = int  (dtag[2])

        lnum -= +1
        next += +1
        
    return
    

def loadvert3(mesh,file):
    """
    LOADVERT3: load 3-dim. vertex pos. from file.
    
    """
    lnum = np.size(mesh.point.coord,0)
    next = +0
    
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        mesh.point.coord[next,0] = float(dtag[0])
        mesh.point.coord[next,1] = float(dtag[1])
        mesh.point.coord[next,2] = float(dtag[3])
        
        mesh.point.IDtag[next,0] = int  (dtag[2])

        lnum -= +1
        next += +1
        
    return


def loadedge2(mesh,file,ltag):
    """
    LOADEDGE2: load EDGE2 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.edge2.index.resize(lnum,2)
    mesh.edge2.IDtag.resize(lnum,1)
    
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        mesh.edge2.index[next,0] = int  (dtag[0])
        mesh.edge2.index[next,1] = int  (dtag[1])
        
        mesh.edge2.IDtag[next,0] = int  (dtag[2])

        lnum -= +1
        next += +1
        
    return
        
        
def loadtria3(mesh,file,ltag):
    """
    LOADTRIA3: load TRIA3 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.tria3.index.resize(lnum,3)
    mesh.tria3.IDtag.resize(lnum,1)
    
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        mesh.tria3.index[next,0] = int  (dtag[0])
        mesh.tria3.index[next,1] = int  (dtag[1])
        mesh.tria3.index[next,2] = int  (dtag[2])
        
        mesh.tria3.IDtag[next,0] = int  (dtag[3])

        lnum -= +1
        next += +1
        
    return
        
        
def loadquad4(mesh,file,ltag):
    """
    LOADUAD4: load QUAD4 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.quad4.index.resize(lnum,4)
    mesh.quad4.IDtag.resize(lnum,1)
    
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        mesh.quad4.index[next,0] = int  (dtag[0])
        mesh.quad4.index[next,1] = int  (dtag[1])
        mesh.quad4.index[next,2] = int  (dtag[2])
        mesh.quad4.index[next,3] = int  (dtag[3])
        
        mesh.quad4.IDtag[next,0] = int  (dtag[4])

        lnum -= +1
        next += +1
        
    return
        
        
def loadtria4(mesh,file,ltag):
    """
    LOADTRIA4: load TRIA4 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.tria4.index.resize(lnum,4)
    mesh.tria4.IDtag.resize(lnum,1)
    
    while (lnum >= +1):
        data = file.readline()
        dtag = data.split(";")
        
        mesh.tria4.index[next,0] = int  (dtag[0])
        mesh.tria4.index[next,1] = int  (dtag[1])
        mesh.tria4.index[next,2] = int  (dtag[2])
        mesh.tria4.index[next,3] = int  (dtag[3])
        
        mesh.tria4.IDtag[next,0] = int  (dtag[4])

        lnum -= +1
        next += +1
        
    return
    
    
def loadhexa8(mesh,file,ltag):
    """
    LOADHEXA8: load HEXA8 data segment from file.
    
    """
    lnum = int(ltag[1])
    next = +0
    
    mesh.hexa8.index.resize(lnum,8)
    mesh.hexa8.IDtag.resize(lnum,1)
    
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
        
        mesh.hexa8.IDtag[next,0] = int  (dtag[8])

        lnum -= +1
        next += +1
        
    return
        
        
def loadlines(mesh,file,line):
    """
    LOADLINES: load next non-null line from file.
    
    """
    
    #-- skip any 'comment' lines
    if (line[0] != '#'):
    
    #-- split about '=' charact.
        ltag = line.split("=")
        l1st = ltag[0].upper()
        
        if   (l1st == "MSHID"):
        
    #-- parse MSHID data section
            data = ltag[1].split(";")

            mesh.mshID = \
                data[1].upper()
            
        elif (l1st == "NDIMS"):
        
    #-- parse NDIMS data section
            mesh.ndims = int(ltag[1])
            
        elif (l1st == "POINT"):
    
    #-- parse POINT data section
            loadpoint(mesh,file,ltag)
                
        elif (l1st == "EDGE2"):
        
    #-- parse EDGE2 data section
            loadedge2(mesh,file,ltag)
                
        elif (l1st == "TRIA3"):
   
    #-- parse TRIA3 data section
            loadtria3(mesh,file,ltag)
                
        elif (l1st == "QUAD4"):
   
    #-- parse QUAD4 data section
            loadquad4(mesh,file,ltag)
                
        elif (l1st == "TRIA4"):
   
    #-- parse TRIA4 data section
            loadtria4(mesh,file,ltag)
                
        elif (l1st == "HEXA8"):
   
    #-- parse HEXA8 data section
            loadhexa8(mesh,file,ltag)
                
    return



def loadmsh(name,mesh):
    """
    LOADMSH: load an MSH obj. from file.
    
    """
 
    with open(name,"r") as file:
        while (True):
        
        #-- get the next line from file    
            line = file.readline ()
            
            if (len(line) != +0):

        #-- parse next non-null section            
                loadlines(
                    mesh,file,line)                    
            
            else:
        #-- reached end-of-file: done!!      
                break

    return



