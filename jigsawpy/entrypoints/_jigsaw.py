import colored_traceback; colored_traceback.add_hook(always=True)  # noqa:E702


def main():
    from jigsawpy.geom._MeshBoundaries import _MeshBoundaries
    print(_MeshBoundaries)
