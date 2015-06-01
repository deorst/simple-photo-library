"""
Main script control the flow of the execution of whole program
"""


from Photo import Photo
from Library import Library
from timeit import default_timer

src_dir = raw_input('Please type in source directory: ')
dst_dir = raw_input('Please type in destination directory: ')

start = default_timer()                             # used for logging purposes
library = Library(src_dir, dst_dir)

library.read_all()
library.make_new_dir()
library.copy_src_to_dst()


stop = default_timer()                              # used for logging purposes

print '\rExecution time: ', stop - start, ' sec'