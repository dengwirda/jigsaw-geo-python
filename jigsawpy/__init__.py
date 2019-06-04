from jigsawpy.Jigsaw import Jigsaw
from jigsawpy.JigsawConf import JigsawConf

__all__ = ["Jigsaw",
           "JigsawConf"]

try:
    import colored_traceback
    colored_traceback.add_hook(always=True)
except ModuleNotFoundError:
    pass
