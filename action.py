"""
Main script control the flow of the execution of whole program
"""


from Photo import Photo
from Library import Library

# for testing purposes
from timeit import default_timer

# get source and destination folder from user
src_dir = raw_input('Please type in source directory: ')
dst_dir = raw_input('Please type in destination directory: ')

# used for logging purposes
start = default_timer()    

library = Library(src_dir, dst_dir)

library.read_all()
library.make_new_dir()
library.copy_src_to_dst()

# used for logging purposes
stop = default_timer()                              

print '\rExecution time: ', stop - start, ' sec'