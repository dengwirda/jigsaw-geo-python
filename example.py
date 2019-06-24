#!/usr/bin/env python

import jigsawpy

from tests.case_1_ import case_1_
from tests.case_2_ import case_2_
from tests.case_3_ import case_3_
from tests.case_4_ import case_4_
from tests.case_5_ import case_5_

import os
import argparse
import matplotlib.pyplot as plt


def example(IDnumber=1,savefigs=False):

#--------------- don't disp. to screen, write to png backend

    if savefigs: plt.switch_backend ("Agg")

#--------------- delegate to the individual example cases...

    filepath = os.path.join(
        os.path.abspath(
        os.path.dirname(__file__)),"files")

    if   (IDnumber == +1):
        case_1_(filepath,savefigs)

    elif (IDnumber == +2):
        case_2_(filepath,savefigs)

    elif (IDnumber == +3):
        case_3_(filepath,savefigs)

    elif (IDnumber == +4):
        case_4_(filepath,savefigs)

    elif (IDnumber == +5):
        case_5_(filepath,savefigs)

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("--IDnumber", dest="IDnumber", type=int,
                        required=True, help="Run example with this ID (1-5).")

    parser.add_argument("--savefigs", dest="savefigs", action="store_true",
                        help="Set this flag to save figures to file rather"
                             "than loading graphics.")

    args = parser.parse_args()

    example(IDnumber=args.IDnumber,
            savefigs=args.savefigs)



