""" class Library """

# for the Library.read_all() and Library.make_new_dir() methods 
from os import listdir, mkdir, walk                                                         
from Photo import Photo                                                                     
from shutil import copyfile                                                                 


class Library(object):

    def __init__(self, source_path, destination_path, libraryset=None):
        self.src_path = source_path
        self.dst_path = destination_path
        self.libraryset = libraryset
        
    def __str__(self):
        """Return a string containing a nicely printable representation of an object"""

        # header
        out = 'uid:\tdate/time(modified):\tdirectory:\tname:\n'                             
        if self.libraryset:
            for dummy_item in self.libraryset.values():
                out += str(dummy_item) + '\n'
        return out
        
    def read_all(self):
        """
        Read all files in a given directory 'source_path',
        and returns a dictionary 'libraryset' {str(uid): Library.object}
        """
        uid = 0
        self.libraryset = {}

        # traverse directory structure 
        for dummy_dirpath, dummy_dirname, dummy_filename in walk(self.src_path):
            # dummy_filename - is a list of names of files in a directory dummy_dirname.
            if dummy_filename:                                                              
                for dummy_name in dummy_filename:
                    self.libraryset[uid] = Photo(dummy_dirpath, dummy_name, uid)
                    self.libraryset[uid].get_datetime_from_file()
                    uid += 1

    def make_new_dir(self):
        """
        Create new directories for sorted photos in a dst_dir.
        """
        
        # create 'dst_dir/albums' folder just in case.
        # It's a root for a library.
        if 'albums' not in listdir(self.dst_path):
            mkdir(self.dst_path + '/' + 'albums/')
            
        for dummy_photo in self.libraryset.values():
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
        for dummy_photo in self.libraryset.values():
            copyfile(
                dummy_photo.get_directory() + '/' + dummy_photo.get_name(),
                self.dst_path + '/' + 'albums/' +
                dummy_photo.get_datetime()[:4] + '/' +
                dummy_photo.get_datetime()[5:7] + '/' +
                dummy_photo.get_datetime()[8:10] + '/' +
                dummy_photo.get_name()
            )
