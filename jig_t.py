
class jigsaw_jig_t:
    def __init__(self):
    
    #------------------------------------------ MISC options
        self.verbosity = None
        
        self.jcfg_file = None
        
        self.tria_file = None
        self.bnds_file = None
        
    #------------------------------------------ INIT options
        self.init_file = None
        self.init_near = None
        
    #------------------------------------------ GEOM options
        self.geom_file = None
        
        self.geom_seed = None
        
        self.geom_feat = None
        
        self.geom_phi1 = None
        self.geom_phi2 = None
        
        self.geom_eta1 = None
        self.geom_eta2 = None
        
    #------------------------------------------ HFUN options
        self.hfun_file = None        
        
        self.hfun_scal = None
        
        self.hfun_hmax = None
        self.hfun_hmin = None
        
    #------------------------------------------ MESH options
        self.mesh_file = None
        
        self.mesh_kern = None
        self.bnds_kern = None
        
        self.mesh_iter = None
        
        self.mesh_dims = None
        
        self.mesh_top1 = None
        self.mesh_top2 = None
        
        self.mesh_siz1 = None
        self.mesh_siz2 = None
        self.mesh_siz3 = None
        
        self.mesh_eps1 = None
        self.mesh_eps2 = None
        
        self.mesh_rad2 = None
        self.mesh_rad3 = None
    
        self.mesh_off2 = None
        self.mesh_off3 = None
        
        self.mesh_snk2 = None
        self.mesh_snk3 = None
        
        self.mesh_vol3 = None
        
    #------------------------------------------ OPTM options
        self.optm_iter = None        
        
        self.optm_qtol = None
        self.optm_qlim = None
        
        self.optm_zip_ = None
        self.optm_div_ = None
        self.optm_tria = None
        self.optm_dual = None



