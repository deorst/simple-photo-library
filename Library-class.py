# The objective of that file is to create a Library class.
# An instance of the Library should have the properties listed below:
# ..., current_uid (this value will assigned to the instances of the Photo class
# one by one with Photo.get_uid() method), path, name...

import os           # for the Library.read_all() method (os.walk() used there)

class Library:
    def __init__(self, current_uid = 0):
        self.current_uid = current_uid
        
    def __str__(self):
        s = 'current uid:\t' + str(self.current_uid)
        return s
        
    def generate_uid(self):
        """ generate uid for the 'Photo.get_uid()' """
        return self.current_uid
        
    def read_all(self, source_path):
        """ read all files in a given directory 'source_path' """
        data = {}
        for dirpath, dirname, filename in os.walk(source_path):
            s = 'dirpath:\t' + str(dirpath) + ',\t'
            s += 'dirname:\t' + str(dirname) + ',\t'
            s += 'filename:\t' + str(filename)
        return s
                
# test phase

library = Library()

print library.read_all('/Users/dstadnik/python-projects')
        