""" Library class """
# The objective of that file is to create a Library class.
# An instance of the Library should have the properties listed below:
# ..., current_uid (this value will be assigned to the instances of the Photo class
# one by one with Photo.get_uid() method), ...

import os           # for the Library.read_all() method (os.walk() used there)
from Photo import Photo

class Library:
    def __init__(self, source_path):
        self.src_path = source_path
        self.database = None
        
    def __str__(self):
        out = 'uid:\tdate/time:\tdirectory:\tname:\n'
        if self.database:
		    for dummy_item in self.database.values():
			    out += str(dummy_item) + '\n'
        return out
        
    def generate_uid(self):
        """ generate uid for the 'Photo.get_uid()' """
        return self.current_uid
        
    def read_all(self):
        """ read all files in a given directory 'source_path' """
        uid = '00000'                                                    # need to make in '00000'
        self.database = {}
        for dummy_dirpath, dummy_dirname, dummy_filename in os.walk(self.src_path):
            if dummy_filename:
                for dummy_name in dummy_filename:
                    self.database[uid] = Photo(dummy_dirpath, dummy_name)
                    self.database[uid].get_uid(uid)
                    uid = int(uid)
                    uid += 1
                    uid = str(uid)
                    while len(uid) < 5:
                        uid = '0' + uid
        return self.database
        
                
# test phase

library = Library('/Users/dstadnik/Pictures/iPhoto Library.migratedphotolibrary/Masters')
library.read_all()

print library
        