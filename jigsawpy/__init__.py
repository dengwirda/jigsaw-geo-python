"""
------------------------------------------------------------
 *
 *   ,o, ,o,       /                                
 *    `   `  e88~88e  d88~\   /~~~8e Y88b    e    /
 *   888 888 88   88 C888         88b Y88b  d8b  / 
 *   888 888 "8b_d8"  Y88b   e88~-888  Y888/Y88b/  
 *   888 888  /        888D C88   888   Y8/  Y8/   
 *   88P 888 Cb      \_88P   "8b_-888    Y    Y     
 * \_8"       Y8""8D                                
 *
------------------------------------------------------------
 * JIGSAW: Interface to the JIGSAW meshing library.
------------------------------------------------------------
 *
 * Last updated: 15 June, 2019
 *
 * Copyright 2019 --
 * Darren Engwirda
 * darren.engwirda@columbia.edu
 * https://github.com/dengwirda
 *
------------------------------------------------------------
 *
 * This program may be freely redistributed under the 
 * condition that the copyright notices (including this 
 * entire header) are not removed, and no compensation 
 * is received through use of the software.  Private, 
 * research, and institutional use is free.  You may 
 * distribute modified versions of this code UNDER THE 
 * CONDITION THAT THIS CODE AND ANY MODIFICATIONS MADE 
 * TO IT IN THE SAME FILE REMAIN UNDER COPYRIGHT OF THE 
 * ORIGINAL AUTHOR, BOTH SOURCE AND OBJECT CODE ARE 
 * MADE FREELY AVAILABLE WITHOUT CHARGE, AND CLEAR 
 * NOTICE IS GIVEN OF THE MODIFICATIONS.  Distribution 
 * of this code as part of a commercial system is 
 * permissible ONLY BY DIRECT ARRANGEMENT WITH THE 
 * AUTHOR.  (If you are not directly supplying this 
 * code to a customer, and you are instead telling them 
 * how they can obtain it for free, then you are not 
 * required to make any arrangement with me.) 
 *
 * Disclaimer:  Neither I nor: Columbia University, The
 * Massachusetts Institute of Technology, The 
 * University of Sydney, nor The National Aeronautics
 * and Space Administration warrant this code in any 
 * way whatsoever.  This code is provided "as-is" to be 
 * used at your own risk.
 *
------------------------------------------------------------
 """

from jigsawpy.msh_t import jigsaw_msh_t
from jigsawpy.jig_t import jigsaw_jig_t
from jigsawpy.def_t import jigsaw_def_t

from jigsawpy.loadmsh import loadmsh
from jigsawpy.savemsh import savemsh
from jigsawpy.loadjig import loadjig
from jigsawpy.savejig import savejig

from jigsawpy.certify import certify

from jigsawpy  import jigsaw, libsaw

class cmd :
#--------------------------------- expose cmd-line interface
    def jigsaw(opts,mesh=None) :
        
        return jigsaw.jigsaw(opts,mesh)

    def tripod(opts,tria=None) :
        
        return jigsaw.tripod(opts,tria)

class lib :
#--------------------------------- expose API-lib. interface
    def jigsaw(opts,geom,mesh,
               init=None,
               hfun=None) :
        
        return libsaw.jigsaw(
            opts,geom,mesh,init,hfun)

    def tripod(opts,init,tria,
               geom=None) :
        
        return libsaw.tripod(
            opts,init,tria,geom     )



