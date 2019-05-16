#
#   Container obj. for JIGSAW mesh data.
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
#   specification may be optionally defined.
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
#   See also JIGSAW, JIG_t
#

#-----------------------------------------------------------
#   Darren Engwirda
#   github.com/dengwirda/jigsaw-python
#   14-May-2019
#   darren.engwirda@columbia.edu
#-----------------------------------------------------------
#

import numpy as np

class jigsaw_point_t:
    def __init__(self,npts=0,ndim=0):  
    #------------------------------------------ VERT struct.
        self.coord = \
    np.empty([npts,ndim],dtype=np.float64)
        
        self.IDtag = \
    np.empty([npts]     ,dtype=  np.int32)
      
class jigsaw_cells_t:
    def __init__(self,ncel=0,nidx=0):
    #------------------------------------------ CELL struct.
        self.index = \
    np.empty([ncel,nidx],dtype=  np.int32)
        
        self.IDtag = \
    np.empty([ncel]     ,dtype=  np.int32)

class jigsaw_index_t:
    def __init__(self,nrow=0,nidx=0):
    #------------------------------------------ INTS struct.
        self.index = \
    np.empty([nrow,nidx],dtype=  np.int32)

class jigsaw_msh_t:
    def __init__(self):
    #------------------------------------------ MESH struct.
        self.mshID = "euclidean-mesh"
        self.ndims = +0
    
        self.radii = \
    np.empty([0],        dtype=np.float64)

        self.point = jigsaw_point_t(0,0)
        
        self.power = \
    np.empty([0,0],      dtype=np.float64)

        self.edge2 = jigsaw_cells_t(0,2)
        self.tria3 = jigsaw_cells_t(0,3)
        self.quad4 = jigsaw_cells_t(0,4)
        self.tria4 = jigsaw_cells_t(0,4)
        self.hexa8 = jigsaw_cells_t(0,8)
        self.pyra5 = jigsaw_cells_t(0,5)
        self.wedg6 = jigsaw_cells_t(0,6)
        
        self.bound = jigsaw_index_t(0,3) 
        
        self.xgrid = \
    np.empty([0],        dtype=np.float64)
        self.ygrid = \
    np.empty([0],        dtype=np.float64)
        self.zgrid = \
    np.empty([0],        dtype=np.float64)
        
        self.value = \
    np.empty([0,0],      dtype=np.float64)



