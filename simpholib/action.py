#!../../bin/python

"""
Main script control the flow of the execution of whole program
"""

from Photo import Photo
from Library import Library
from sys import exit

# for testing purposes
from timeit import default_timer


def main(src_dir, dst_dir=None):

    if not dst_dir:
        dst_dir = src_dir

    # used for logging purposes
    start = default_timer()

    library = Library(src_dir, dst_dir)

    library.read_all()
    library.make_new_dir()
    library.copy_src_to_dst()

    # used for logging purposes
    stop = default_timer()

    print '\rExecution time: ', stop - start, ' sec'