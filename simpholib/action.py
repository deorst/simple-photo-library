#!../../bin/python

"""
Main script control the flow of the execution of whole program
"""

from Library import Library
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

    library.delete_old_folders()

    # used for logging purposes
    stop = default_timer()

    print 'Execution time: ', stop - start, ' sec'