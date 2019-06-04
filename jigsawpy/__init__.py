from jigsawpy.Jigsaw import Jigsaw

__all__ = ["Jigsaw"]

try:
    import colored_traceback
    colored_traceback.add_hook(always=True)
except ModuleNotFoundError:
    pass
