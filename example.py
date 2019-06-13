#!/usr/bin/env python

from timeit import default_timer as timer
from pathlib import Path

import jigsawpy

import matplotlib.pyplot as plt
import matplotlib.tri as tri

import argparse


def example(savefigs=False):

    if savefigs:
        # don't display to the screen, write to the png backend
        plt.switch_backend('Agg')

    opts = jigsawpy.jigsaw_jig_t()

    opts.geom_file = \
        str(Path()/"jigsaw"/"geo"/"lake.msh")
    opts.jcfg_file = \
        str(Path()/"jigsaw"/"out"/"lake.jig")
    opts.mesh_file = \
        str(Path()/"jigsaw"/"out"/"lake.msh")

#---------------------------------- call JIGSAW via cmd-line

    mesh = jigsawpy.jigsaw_msh_t()
    geom = jigsawpy.jigsaw_msh_t()

    opts.hfun_hmax = 0.03
    opts.mesh_dims = +2
    opts.optm_iter = +0

    ttic = timer()
    jigsawpy.cmd.jigsaw(opts,mesh)
    ttoc = timer()
    print("cmd: "+ str(ttoc-ttic))

    fig = plt.figure(1)
    plt.triplot(tri.Triangulation( \
        mesh.vert2["coord"][:, 0], \
        mesh.vert2["coord"][:, 1], \
        mesh.tria3["index"]),linewidth=0.500)
    plt.axis('equal')

#---------------------------------- call JIGSAW via API-lib.

    mesh = jigsawpy.jigsaw_msh_t()
    geom = jigsawpy.jigsaw_msh_t()

    jigsawpy.loadmsh(opts.geom_file,geom)

    opts.hfun_hmax = 0.03
    opts.mesh_dims = +2
    opts.optm_iter = +0

    ttic = timer()
    jigsawpy.lib.jigsaw(opts,geom,mesh)
    ttoc = timer()
    print("lib: "+ str(ttoc-ttic))

    fig = plt.figure(2)
    plt.triplot(tri.Triangulation( \
        mesh.vert2["coord"][:, 0], \
        mesh.vert2["coord"][:, 1], \
        mesh.tria3["index"]),linewidth=0.500)
    plt.axis('equal')

    if savefigs:
        plt.figure(1)
        plt.savefig('example_cmd.png')
        plt.figure(2)
        plt.savefig('example_api.png')
    else:
        plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("--savefigs", dest="savefigs", action='store_true',
                        help="Set this flag to write out figures rather than"
                             "showing them.")
    args = parser.parse_args()

    example(savefigs=args.savefigs)
