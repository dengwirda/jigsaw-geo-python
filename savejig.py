#
#   SAVEJIG save a *.JIG file for JIGSAW.
#
#   SAVEJIG(NAME,OPTS)
#   
#   OPTS is a user-defined set of meshing options:
#
#   REQUIRED fields:
#   ---------------
#
#   OPTS.JCFG_FILE - "JCFGNAME.JIG", a string containing the 
#       name of the cofig. file (will be created on output).
#
#   OPTS.MESH_FILE - "MESHNAME.MSH", a string containing the 
#       name of the output file (will be created on output).
#
#   OPTIONAL fields (INIT):
#   ----------------------
#
#   OPTS.INIT_FILE - "INITNAME.MSH", a string containing the 
#       name of the initial distribution file (is required 
#       at input).
#
#   OPTS.INIT_NEAR - {default = 1.E-8} relative "zip" tol.
#       applied when processing initial conditions. In cases
#       where "sharp-feature" detection is active, nodes in 
#       the initial set are zipped to their nearest feature
#       node if the separation length is less than NEAR*SCAL
#       where SCAL is the max. bounding-box dimension.
#
#   OPTIONAL fields (GEOM):
#   ----------------------
#
#   OPTS.GEOM_FILE - "GEOMNAME.MSH", a string containing the 
#       name of the geometry file (is required at input). 
#       See SAVEMSH for additional details regarding the cr-
#       eation of *.MSH files.
#
#   OPTS.GEOM_SEED - {default=8} number of "seed" vertices 
#       used to initialise mesh generation.
#
#   OPTS.GEOM_FEAT - {default=false} attempt to auto-detect 
#       "sharp-features" in the input geometry. Features can 
#       lie adjacent to 1-dim. entities, (i.e. geometry 
#       "edges") and/or 2-dim. entities, (i.e. geometry 
#       "faces") based on both geometrical and/or topologic-
#       al constraints. Geometrically, features are located 
#       between any neighbouring entities that subtend 
#       angles less than GEOM_ETAX degrees, where "X" is the 
#       (topological) dimension of the feature. Topological-
#       ly, features are located at the apex of any non-man-
#       ifold connections.
#
#   OPTS.GEOM_ETA1 - {default=45deg} 1-dim. feature-angle, 
#       features are located between any neighbouring 
#       "edges" that subtend angles less than ETA1 deg.
#
#   OPTS.GEOM_ETA2 - {default=45deg} 2-dim. feature angle, 
#       features are located between any neighbouring 
#       "faces" that subtend angles less than ETA2 deg.
#
#   OPTIONAL fields (HFUN):
#   ----------------------
#
#   OPTS.HFUN_FILE - "HFUNNAME.MSH", a string containing the 
#       name of the mesh-size file (is required at input).
#       The mesh-size function is specified as a general pi-
#       ecewise linear function, defined at the vertices of
#       an unstructured triangulation. See SAVEMSH for addi-
#       tional details.
#
#   OPTS.HFUN_SCAL - {default='relative'} scaling type for 
#       mesh-size fuction. HFUN_SCAL='relative' interprets 
#       mesh-size values as percentages of the (mean) length 
#       of the axis-aligned bounding-box (AABB) associated 
#       with the geometry. HFUN_SCAL='absolute' interprets 
#       mesh-size values as absolute measures.
#
#   OPTS.HFUN_HMAX - {default=0.02} max. mesh-size function 
#       value. Interpreted based on SCAL setting.
#
#   OPTS.HFUN_HMIN - {default=0.00} min. mesh-size function 
#       value. Interpreted based on SCAL setting.
#
#   OPTIONAL fields (MESH):
#   ----------------------
#
#   OPTS.MESH_DIMS - {default=3} number of "topological" di-
#       mensions to mesh. DIMS=K meshes K-dimensional featu-
#       res, irrespective of the number of spatial dim.'s of 
#       the problem (i.e. if the geometry is 3-dimensional 
#       and DIMS=2 a surface mesh will be produced).
#
#   OPTS.MESH_KERN - {default='delfront'} meshing kernal,
#       choice of the standard Delaunay-refinement algorithm 
#       (KERN='delaunay') or the Frontal-Delaunay method 
#       (KERN='delfront').
#
#   OPTS.MESH_ITER - {default=+INF} max. number of mesh ref-
#       inement iterations. Set ITER=N to see progress after 
#       N iterations. 
#
#   OPTS.MESH_TOP1 - {default=false} enforce 1-dim. topolog-
#       ical constraints. 1-dim. edges are refined until all 
#       embedded nodes are "locally 1-manifold", i.e. nodes 
#       are either centred at topological "features", or lie 
#       on 1-manifold complexes.
#
#   OPTS.MESH_TOP2 - {default=false} enforce 2-dim. topolog-
#       ical constraints. 2-dim. trias are refined until all 
#       embedded nodes are "locally 2-manifold", i.e. nodes 
#       are either centred at topological "features", or lie 
#       on 2-manifold complexes.
#
#   OPTS.MESH_RAD2 - {default=1.05} max. radius-edge ratio 
#       for 2-tria elements. 2-trias are refined until the 
#       ratio of the element circumradii to min. edge length 
#       is less-than RAD2.
#
#   OPTS.MESH_RAD3 - {default=2.05} max. radius-edge ratio 
#       for 3-tria elements. 3-trias are refined until the 
#       ratio of the element circumradii to min. edge length 
#       is less-than RAD3.
#
#   OPTS.MESH_OFF2 - {default=0.90} radius-edge ratio target
#       for insertion of "shape"-type offcentres for 2-tria
#       elements. When refining an element II, offcentres
#       are positioned to form a new "frontal" element JJ 
#       that satisfies JRAD <= OFF2.
#
#   OPTS.MESH_OFF3 - {default=1.10} radius-edge ratio target
#       for insertion of "shape"-type offcentres for 3-tria
#       elements. When refining an element II, offcentres
#       are positioned to form a new "frontal" element JJ 
#       that satisfies JRAD <= OFF3.
#
#   OPTS.MESH_SNK2 - {default=0.20} inflation tolerance for
#       insertion of "sink" offcentres for 2-tria elements.
#       When refining an element II, "sinks" are positioned
#       at the centre of the largest adj. circumball staisf-
#       ying |JBAL-IBAL| < SNK2 * IRAD, where IRAD is the 
#       radius of the circumball, and [IBAL,JBAL] are the 
#       circumball centres.
#
#   OPTS.MESH_SNK3 - {default=0.33} inflation tolerance for
#       insertion of "sink" offcentres for 3-tria elements.
#       When refining an element II, "sinks" are positioned
#       at the centre of the largest adj. circumball staisf-
#       ying |JBAL-IBAL| < SNK3 * IRAD, where IRAD is the 
#       radius of the circumball, and [IBAL,JBAL] are the 
#       circumball centres.
#
#   OPTS.MESH_EPS1 - {default=0.33} max. surface-discretisa-
#       tion error multiplier for 1-edge elements. 1-edge 
#       elements are refined until the surface-disc. error 
#       is less-than EPS1 * HFUN(X).
#
#   OPTS.MESH_EPS2 - {default=0.33} max. surface-discretisa-
#       tion error multiplier for 2-tria elements. 2-tria 
#       elements are refined until the surface-disc. error 
#       is less-than EPS2 * HFUN(X).
#
#   OPTS.MESH_VOL3 - {default=0.00} min. volume-length ratio 
#       for 3-tria elements. 3-tria elements are refined 
#       until the volume-length ratio exceeds VOL3. Can be 
#       used to supress "sliver" elements.
#
#   OPTIONAL fields (OPTM):
#   ----------------------
#
#   OPTS.OPTM_ITER - {default=16} max. number of mesh optim-
#       isation iterations. Set ITER=N to see progress after 
#       N iterations. 
#
#   OPTS.OPTM_QTOL - {default=1.E-04} tolerance on mesh cost
#       function for convergence. Iteration on a given node
#       is terminated if adjacent element cost-functions are
#       improved by less than QTOL.
#
#   OPTS.OPTM_QLIM - {default=0.9375} threshold on mesh cost
#       function above which gradient-based optimisation is
#       attempted.
#
#   OPTS.OPTM_TRIA - {default= true} allow for optimisation
#       of TRIA grid geometry.
#
#   OPTS.OPTM_DUAL - {default=false} allow for optimisation
#       of DUAL grid geometry.
#
#   OPTS.OPTM_ZIP_ - {default= true} allow for "merge" oper-
#       ations on sub-face topology.
#
#   OPTS.OPTM_DIV_ - {default= true} allow for "split" oper-
#       ations on sub-face topology.
#
#   OPTIONAL fields (MISC):
#   ----------------------
#
#   OPTS.VERBOSITY - {default=0} verbosity of log-file gene-
#       rated by JIGSAW. Set VERBOSITY >= 1 for more output.
#
#   See also JIGSAW, SAVEJIG
#

#-----------------------------------------------------------
#   Darren Engwirda
#   github.com/dengwirda/jigsaw-python
#   14-May-2019
#   darren.engwirda@columbia.edu
#-----------------------------------------------------------
#

from pathlib import Path
from jig_t   import *

def savechar(file,sval,stag):

    if (isinstance(sval,str)):
        file.write("  " + stag + "=" + sval + "\n")
    else:
        raise Exception("Invalid data: OPTS.",stag)

    return

def saveints(file,ival,stag):

    if (isinstance(ival,int)):
        file.write( \
            "  " + stag + "=" + str(ival) + "\n")
    else:
        raise Exception("Invalid data: OPTS.",stag)

    return
    
def savereal(file,fval,stag):

    if (isinstance(fval,float)):
        file.write( \
            "  " + stag + '=' + str(fval) + "\n")
    else:
        raise Exception("Invalid data: OPTS.",stag)

    return
    
def savebool(file,bval,stag):

    if (isinstance(bval,bool)):
        if (bval == True):
            file.write("  " + stag + "=TRUE \n")
        else:
            file.write("  " + stag + "=FALSE\n")
    else:
        raise Exception("Invalid data: OPTS.",stag)

    return


def savejig(name,opts):
    """
    SAVEJIG: save a JIG config. obj. to file.
    
    """

    if (not isinstance(name,str)):
        raise Exception("Incorrect type: NAME.")
        
    if (not isinstance(opts,jigsaw_jig_t)):
        raise Exception("Incorrect type: OPTS.")

    fext = Path(name).suffix
    
    if (fext.strip() != ".jig"):
        name =   name + ".jig"

    with Path(name).open("w") as file:
        
        file.write("# " + name + \
    " config. file; created by JIGSAW's PYTHON interface \n")
        
    #------------------------------------------ MISC options
        if (opts.verbosity is not None):
            saveints(file,opts.verbosity,"VERBOSITY")
            
        if (opts.tria_file is not None):
            savechar(file,opts.tria_file,"TRIA_FILE")
        if (opts.bnds_file is not None):
            savechar(file,opts.bnds_file,"BNDS_FILE")            

    #------------------------------------------ INIT options
        if (opts.init_file is not None):
            savechar(file,opts.init_file,"INIT_FILE")

        if (opts.init_near is not None):
            savereal(file,opts.init_near,"INIT_NEAR")
            
    #------------------------------------------ GEOM options
        if (opts.geom_file is not None):
            savechar(file,opts.geom_file,"GEOM_FILE")
            
        if (opts.geom_seed is not None):
            saveints(file,opts.geom_seed,"GEOM_SEED")
            
        if (opts.geom_feat is not None):
            savebool(file,opts.geom_feat,"GEOM_FEAT")
        
        if (opts.geom_phi1 is not None):
            savereal(file,opts.geom_phi1,"GEOM_PHI1")
        if (opts.geom_phi2 is not None):
            savereal(file,opts.geom_phi2,"GEOM_PHI2")
            
        if (opts.geom_eta1 is not None):
            savereal(file,opts.geom_eta1,"GEOM_ETA1")
        if (opts.geom_eta2 is not None):
            savereal(file,opts.geom_eta2,"GEOM_ETA2")
            
    #------------------------------------------ HFUN options
        if (opts.hfun_file is not None):
            savechar(file,opts.hfun_file,"HFUN_FILE")
            
        if (opts.hfun_scal is not None):
            savechar(file,opts.hfun_scal,"HFUN_SCAL")
            
        if (opts.hfun_hmax is not None):
            savereal(file,opts.hfun_hmax,"HFUN_HMAX")
        if (opts.hfun_hmin is not None):
            savereal(file,opts.hfun_hmin,"HFUN_HMIN")
            
    #------------------------------------------ MESH options
        if (opts.mesh_file is not None):
            savechar(file,opts.mesh_file,"MESH_FILE")
            
        if (opts.mesh_kern is not None):
            savechar(file,opts.mesh_kern,"MESH_KERN")
        if (opts.bnds_kern is not None):
            savechar(file,opts.bnds_kern,"BNDS_KERN")
            
        if (opts.mesh_iter is not None):
            saveints(file,opts.mesh_iter,"MESH_ITER")
            
        if (opts.mesh_dims is not None):
            saveints(file,opts.mesh_dims,"MESH_DIMS")
            
        if (opts.mesh_top1 is not None):
            savebool(file,opts.mesh_top1,"MESH_TOP1")
        if (opts.mesh_top2 is not None):
            savebool(file,opts.mesh_top2,"MESH_TOP2")
            
        if (opts.mesh_siz1 is not None):
            savereal(file,opts.mesh_siz1,"MESH_SIZ1")
        if (opts.mesh_siz2 is not None):
            savereal(file,opts.mesh_siz2,"MESH_SIZ2")
        if (opts.mesh_siz3 is not None):
            savereal(file,opts.mesh_siz3,"MESH_SIZ3")
            
        if (opts.mesh_eps1 is not None):
            savereal(file,opts.mesh_eps1,"MESH_EPS1")
        if (opts.mesh_eps2 is not None):
            savereal(file,opts.mesh_eps2,"MESH_EPS2")
        
        if (opts.mesh_rad2 is not None):
            savereal(file,opts.mesh_rad2,"MESH_RAD2")
        if (opts.mesh_rad3 is not None):
            savereal(file,opts.mesh_rad3,"MESH_RAD3")
            
        if (opts.mesh_off2 is not None):
            savereal(file,opts.mesh_off2,"MESH_OFF2")
        if (opts.mesh_off3 is not None):
            savereal(file,opts.mesh_off3,"MESH_OFF3")
            
        if (opts.mesh_snk2 is not None):
            savereal(file,opts.mesh_snk2,"MESH_SNK2")
        if (opts.mesh_snk3 is not None):
            savereal(file,opts.mesh_snk3,"MESH_SNK3")
            
        if (opts.mesh_vol3 is not None):
            savereal(file,opts.mesh_vol3,"MESH_VOL3")
            
    #------------------------------------------ OPTM options
        if (opts.optm_iter is not None):
            saveints(file,opts.optm_iter,"OPTM_ITER")
            
        if (opts.optm_qtol is not None):
            savereal(file,opts.optm_qtol,"OPTM_QTOL")
        if (opts.optm_qlim is not None):
            savereal(file,opts.optm_qlim,"OPTM_QLIM")
    
        if (opts.optm_zip_ is not None):
            savebool(file,opts.optm_zip_,"OPTM_ZIP_")
        if (opts.optm_div_ is not None):
            savebool(file,opts.optm_div_,"OPTM_DIV_")
        if (opts.optm_tria is not None):
            savebool(file,opts.optm_tria,"OPTM_TRIA")
        if (opts.optm_dual is not None):
            savebool(file,opts.optm_dual,"OPTM_DUAL")
        
    return



