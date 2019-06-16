
import subprocess
import os,inspect
import shutil

from pathlib import Path

from jigsawpy.jig_t import jigsaw_jig_t
from jigsawpy.msh_t import jigsaw_msh_t

from jigsawpy.loadmsh import loadmsh
from jigsawpy.savejig import savejig

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

    #   stackoverflow.com/questions/2632199/
    #       how-do-i-get-the-
    #       path-of-the-current-executed-file-in-python
        filename = \
            inspect.getsourcefile(lambda:None)

        filepath = Path(os.path.dirname(
            os.path.abspath(filename))).parent
    
        if   (os.name ==    "nt"):
            jexename  = \
                filepath / "c_lib" \
          / "jigsaw" / "bin" / "jigsaw.exe"

        elif (os.name == "posix"):
            jexename  = \
                filepath / "c_lib" \
          / "jigsaw" / "bin" / "jigsaw"

        else:
            jexename  = Path ()

        if (not jexename.is_file()):
            jexename  = Path ()

    if (jexename == Path()):
#---------------------------- search machine path for binary
        jexename = Path(shutil.which("jigsaw"))

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
        
    #   stackoverflow.com/questions/2632199/
    #       how-do-i-get-the-
    #       path-of-the-current-executed-file-in-python
        filename = \
            inspect.getsourcefile(lambda:None)

        filepath = Path(os.path.dirname(
            os.path.abspath(filename))).parent
    
        if   (os.name ==    "nt"):
            jexename  = \
                filepath / "c_lib" \
          / "jigsaw" / "bin" / "tripod.exe"

        elif (os.name == "posix"):
            jexename  = \
                filepath / "c_lib" \
          / "jigsaw" / "bin" / "tripod"

        else:
            jexename  = Path ()

        if (not jexename.is_file()):
            jexename  = Path ()

    if (jexename == Path()):
#---------------------------- search machine path for binary
        jexename = Path(shutil.which("tripod"))

    if (jexename != Path()):
#---------------------------- call JIGSAW and capture output
        subprocess.run( \
            [str(jexename),opts.jcfg_file], check = True)

        if tria is not None: loadmsh(opts.mesh_file,tria)

    else:

        raise Exception("JIGSAW's executable not found!")

    return



