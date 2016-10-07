"""
Utility class for working with each individual Photo 
"""

from os.path import getmtime
from time import strftime, gmtime


class Photo(object):

    def __init__(self, directory, name, uid):
        self.directory = directory
        self.name = name
        self.uid = uid
        self.unrecognized = False
        self.datetime = None

    def __str__(self):
        out = ''
        if self.uid:
            out += str(self.uid) + '\t'
        else:
            out += 'NO UID\t'
            
        if self.datetime:
            out += str(self.datetime) + '\t'
        else:
            out += 'NO DATE/TIME\t'
            
        out += str(self.directory) + '/\t'
        out += str(self.name)
        return out  
                
    def get_datetime_from_file(self):
        """ get MODIFIED date and time """
        self.datetime = strftime('%Y:%m:%d %H:%M:%S', gmtime(getmtime(self.directory + '/' + self.name)))
        return self.datetime
        
    def get_datetime(self):
        return self.datetime
        
    def get_name(self):
        return self.name
        
    def get_directory(self):
        return self.directory
