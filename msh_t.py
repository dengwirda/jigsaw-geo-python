
import numpy as np

class jigsaw_point_t:
    def __init__(self,npts=0,ndim=0):  
    #------------------------------------------ VERT struct.
        self.coord = \
    np.empty([npts,ndim],dtype=np.float64)
        
        self.IDtag = \
    np.empty([npts],     dtype=  np.int32)
      
class jigsaw_cells_t:
    def __init__(self,ncel=0,nidx=0):
    #------------------------------------------ CELL struct.
        self.index = \
    np.empty([ncel,nidx],dtype=  np.int32)
        self.IDtag = \
    np.empty([ncel],     dtype=  np.int32)

class jigsaw_index_t:
    def __init__(self,nrow=0,nidx=0):
    #------------------------------------------ BNDS struct.
        self.index = \
    np.empty([nrow,nidx],dtype=  np.int32)

class jigsaw_msh_t:
    def __init__(self):
    #------------------------------------------ MESH struct.
        self.mshID = "EUCLIDEAN-MESH"
        self.ndims = +0
    
        self.point = jigsaw_point_t(0,0)
        
        self.power = \
    np.empty([0,0],      dtype=np.float64)
        
        self.radii = \
    np.empty([0],        dtype=np.float64)
        
        self.edge2 = jigsaw_cells_t(0,2)
        self.tria3 = jigsaw_cells_t(0,3)
        self.quad4 = jigsaw_cells_t(0,4)
        self.tria4 = jigsaw_cells_t(0,4)
        self.hexa8 = jigsaw_cells_t(0,8)
        
        self.bound = jigsaw_index_t(0,2) 
        
        self.xgrid = \
    np.empty([0],        dtype=np.float64)
        self.ygrid = \
    np.empty([0],        dtype=np.float64)
        self.zgrid = \
    np.empty([0],        dtype=np.float64)
        
        self.value = \
    np.empty([0,0],      dtype=np.float64)
    


