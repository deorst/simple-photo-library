""" class Library """

# for the Library.read_all() and Library.make_new_dir() methods 
from os import listdir, mkdir, walk                                                         
from Photo import Photo                                                                     
from shutil import copyfile                                                                 

class Library:
    def __init__(self, source_path, destination_path):
        self.dst_path = destination_path
        self.src_path = source_path

        # will be assigned later in the Library.read_all() method
        self.database = None                                                                
        
    def __str__(self):
        """Return a string containing a nicely printable representation of an object"""

        # header
        out = 'uid:\tdate/time(modified):\tdirectory:\tname:\n'                             
        if self.database:                     
		    for dummy_item in self.database.values():
			    out += str(dummy_item) + '\n'
        return out
        
    def read_all(self):
        """ read all files in a given directory 'source_path' and returns a dictionary database {str(uid): (instance of Library)}"""
        uid = '00000'                                                                       # maximum amount of photos 99999
        self.database = {}

        # traverse directory structure 
        for dummy_dirpath, dummy_dirname, dummy_filename in walk(self.src_path):
            # dummy_filename - is a list of names of files in a directory dummy_dirname.
            if dummy_filename:                                                              
                for dummy_name in dummy_filename:
                    self.database[uid] = Photo(dummy_dirpath, dummy_name, uid)
                    self.database[uid].get_datetime_from_file()
                    uid = int(uid)
                    uid += 1
                    uid = str(uid)
                    while len(uid) < 5:
                        uid = '0' + uid
#        return self.database       there is no need in return as self.database will be used only inside of the instance of Library
        
    def make_new_dir(self):
        """ creates new directories ordered photos in a dst_dir """
        
        # create 'dst_dir/albums' folder just in case. It will contain all other folders
        if 'albums' not in listdir(self.dst_path):
            mkdir(self.dst_path + '/' + 'albums/')
            
        for dummy_photo in self.database.values():
            # create a 'dst_dir/albums/YYYY' folder
            if dummy_photo.get_datetime()[:4] not in listdir(self.dst_path + '/' + 'albums/'):
                mkdir(self.dst_path + '/' + 'albums/' + dummy_photo.get_datetime()[:4])
                
            # create a 'dst_dir/albums/YYYY/MM' folder
            if dummy_photo.get_datetime()[5:7] not in listdir(self.dst_path + '/' + 'albums/' + dummy_photo.get_datetime()[:4]):
                mkdir(self.dst_path + '/' + 'albums/' + dummy_photo.get_datetime()[:4] + '/' + dummy_photo.get_datetime()[5:7])
            
            # create a 'dst_dir/albums/YYYY/MM/DD' folder
            if dummy_photo.get_datetime()[8:10] not in listdir(self.dst_path + '/' + 'albums/' + dummy_photo.get_datetime()[:4] + '/' + dummy_photo.get_datetime()[5:7]):
                mkdir(self.dst_path + '/' + 'albums/' + dummy_photo.get_datetime()[:4] + '/' + dummy_photo.get_datetime()[5:7] + '/' + dummy_photo.get_datetime()[8:10])
            
    def copy_src_to_dst(self):
        """ copy all photos from src_dir to dst_dir """
        # copy all photos to dst_dir/albums/YYYY/MM/DD based on file's modified date
        for dummy_photo in self.database.values():
            copyfile(dummy_photo.get_directory() + '/' + dummy_photo.get_name(), self.dst_path + '/' + 'albums/' + dummy_photo.get_datetime()[:4] + '/' + dummy_photo.get_datetime()[5:7] + '/' + dummy_photo.get_datetime()[8:10] + '/' + dummy_photo.get_name())
                    