""" Photo class """
# The objective of that file is to create a Photo class.
# An instance of the Photo should have the properties listed below:
# An uid(not name), name, path, datetime.
# uid will be randomly generated, name, path will be original.
# datetime will be extracted from MODIFIED date and time data.

import os
import time

class Photo:
    def __init__(self, directory, name):
        self.directory = directory
        self.name = name
        self.datetime = None            # an instance of Photo will get datetime and uid
        self.uid = None                 # later (with method of Photo class). So they're 'None' for now.
        
    def __str__(self):
    
        s = ''
        if self.uid:
            s += str(self.uid) + '\t'
        else:
            s += 'NO UID\t'
            
        if self.datetime:
            s += str(self.datetime) + '\t'
        else:
            s += 'NO DATE/TIME\t'
            
        s +=  str(self.directory) + '/\t'
        s += str(self.name) + '\t'
        return s
        
    def set_uid(self, uid):             
        """ get uid from the 'Library.generate_uid()' """
        self.uid = uid   
                
    def get_datetime_from_file(self):
        self.datetime = time.strftime('%Y:%m:%d %H:%M:%S', time.gmtime(os.path.getmtime(self.directory + '/' + self.name)))
        
    def get_datetime(self):
        return self.datetime
        
    def get_name(self):
        return self.name
        
    def get_directory(self):
        return self.directory
     
        
