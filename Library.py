""" Library class """
# The objective of that file is to create a Library class.
# An instance of the Library should have the properties listed below:
# ..., current_uid (this value will be assigned to the instances of the Photo class
# one by one with Photo.get_uid() method), ...

import os           # for the Library.read_all() method (os.walk() used there)
import Photo as photo

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
        data = [['dirpath', 'dirname', 'filename']]
        for dirpath, dirname, filename in os.walk(source_path):
            data.append([str(dirpath), str(dirname), str(filename)])
        return data
                
# test phase

library = Library()

for dummy_item in library.read_all('/Users/dstadnik/Pictures/iPhoto Library.migratedphotolibrary/Masters'):
    print dummy_item
        