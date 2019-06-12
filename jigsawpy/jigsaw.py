
import subprocess
import os

from  pathlib import Path

from .jig_t import jigsaw_jig_t
from .msh_t import jigsaw_msh_t

from .loadmsh import loadmsh
from .savejig import savejig

def jigsaw(opts,mesh=None):
    """
    JIGSAW cmd-line interface to JIGSAW.
 
    JIGSAW(OPTS,MESH=None)
 
    Call the JIGSAW mesh generator using the config. options 
    specified in the OPTS structure. 
 
    OPTS is a user-defined set of meshing options. See JIG_t
    for details.
 
    """
    jexename = Path()

    if (not isinstance(opts,jigsaw_jig_t)):
        raise Exception("Incorrect type: OPTS.")

    if ((mesh is not None) and \
        not isinstance(mesh,jigsaw_msh_t)):
        raise Exception("Incorrect type: MESH.")

    savejig(opts.jcfg_file,opts)

    if (jexename == Path()):
#---------------------------- set-up path for "local" binary
        filepath = Path().absolute()

        if   (os.name ==    "nt"):
            jexename  = filepath \
          / "jigsaw" / "bin" / "jigsaw.exe"

        elif (os.name == "posix"):
            jexename  = filepath \
          / "jigsaw" / "bin" / "jigsaw"

        else:
            jexename  = Path ()

        if (not jexename.is_file()):
            jexename  = Path ()

    if (jexename == Path()):
#---------------------------- search machine path for binary        
        if   (os.name ==    "nt"):
            jexename  = Path ( "jigsaw.exe" )

        elif (os.name == "posix"):
            jexename  = Path ( "jigsaw" )

        else:
            jexename  = Path ()


    if (jexename != Path()):
#---------------------------- call JIGSAW and capture output
        subprocess.run( \
            [str(jexename),opts.jcfg_file], check = True)

        if mesh is not None: loadmsh(opts.mesh_file,mesh)

    else:

        raise Exception("JIGSAW's executable not found!")

    return


def tripod(opts,tria=None):
    """
    TRIPOD cmd-line interface to TRIPOD.
 
    TRIPOD(OPTS,TRIA=None)
 
    Call the TRIPOD tessellation util. using the config. opt 
    specified in the OPTS structure. 
 
    OPTS is a user-defined set of meshing options. See JIG_t
    for details.
 
    """
    jexename = Path()

    if (not isinstance(opts,jigsaw_jig_t)):
        raise Exception("Incorrect type: OPTS.")

    if ((tria is not None) and \
        not isinstance(tria,jigsaw_msh_t)):
        raise Exception("Incorrect type: TRIA.")

    savejig(opts.jcfg_file,opts)

    if (jexename == Path()):
#---------------------------- set-up path for "local" binary
        filepath = Path().absolute()

        if   (os.name ==    "nt"):
            jexename  = filepath \
          / "jigsaw" / "bin" / "tripod.exe"

        elif (os.name == "posix"):
            jexename  = filepath \
          / "jigsaw" / "bin" / "tripod"

        else:
            jexename  = Path ()

        if (not jexename.is_file()):
            jexename  = Path ()

    if (jexename == Path()):
#---------------------------- search machine path for binary        
        if   (os.name ==    "nt"):
            jexename  = Path ( "tripod.exe" )

        elif (os.name == "posix"):
            jexename  = Path ( "tripod" )

        else:
            jexename  = Path ()


    if (jexename != Path()):
#---------------------------- call JIGSAW and capture output
        subprocess.run( \
            [str(jexename),opts.jcfg_file], check = True)

        if tria is not None: loadmsh(opts.mesh_file,tria)

    else:

        raise Exception("JIGSAW's executable not found!")

    return



