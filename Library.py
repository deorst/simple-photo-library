""" class Library """

# for the Library.read_all() and Library.make_new_dir() methods 
from os import listdir, mkdir, walk
from os.path import splitext
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

                    ext = splitext(dummy_name)[1]
                    if ext not in ['.jpg', '.jpeg', '.JPG', '.JPEG',
                                   '.png', '.PNG', '.gif', '.GIF',
                                   '.m4v', '.MOV', '.mp4']:
                        self.libraryset[uid].unrecognized = True
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
            year = dummy_photo.get_datetime()[:4]
            month = dummy_photo.get_datetime()[5:7]
            day = dummy_photo.get_datetime()[8:10]

            if dummy_photo.unrecognized:
                if 'unrecognized' not in listdir('{path}/'.format(path=self.dst_path)):
                    mkdir('{path}/unrecognized'.format(path=self.dst_path))

            else:
                if year not in listdir('{path}/albums/'.format(path=self.dst_path)):
                    mkdir('{path}/albums/{year}'.format(path=self.dst_path, year=year))

                if month not in listdir('{path}/albums/{year}'.format(path=self.dst_path, year=year)):
                    mkdir('{path}/albums/{year}/{month}'.format(path=self.dst_path, year=year, month=month))

                if day not in listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path, year=year, month=month)):
                    mkdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path, year=year, month=month, day=day))

    def copy_src_to_dst(self):
        """ copy all photos from src_dir to dst_dir """
        # copy all photos to dst_dir/albums/YYYY/MM/DD based on file's modified date
        for dummy_photo in self.libraryset.values():
            year = dummy_photo.get_datetime()[:4]
            month = dummy_photo.get_datetime()[5:7]
            day = dummy_photo.get_datetime()[8:10]
            name = dummy_photo.get_name()
            old_dir = dummy_photo.get_directory()
            new_dir = self.dst_path
            if dummy_photo.unrecognized:
                copyfile(
                    '{old_dir}/{name}'.format(old_dir=old_dir, name=name),
                    '{new_dir}/unrecognized/{name}'.format(
                        new_dir=new_dir,
                        name=name
                    )
                )
            else:
                copyfile(
                    '{old_dir}/{name}'.format(old_dir=old_dir, name=name),
                    '{new_dir}/albums/{year}/{month}/{day}/{name}'.format(
                        new_dir=new_dir,
                        year=year,
                        month=month,
                        day=day,
                        name=name,
                    )
                )
