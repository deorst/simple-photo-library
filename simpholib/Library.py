""" class Library """

# for the Library.read_all() and Library.make_new_dir() methods 
from os.path import splitext
from Photo import Photo                                                                     
from shutil import copyfile, rmtree
import sys

import os


class Library(object):

    def __init__(self, source_path, destination_path, libraryset=None):
        self.src_path = source_path.rstrip('/')
        self.dst_path = destination_path.rstrip('/')
        self.libraryset = libraryset
        if self.src_path == self.dst_path:
            self.delete_old = True
        else:
            self.delete_old = False
        self.folders_to_delete = set()
        
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

        sys.stdout.write('Reading files...')

        # traverse directory structure 
        for dummy_dirpath, dummy_dirname, dummy_filename in os.walk(self.src_path):
            # dummy_filename - is a list of names of files in a directory dummy_dirname.
            if dummy_filename:
                for dummy_name in dummy_filename:
                    self.libraryset[uid] = Photo(dummy_dirpath, dummy_name, uid)
                    self.libraryset[uid].get_datetime_from_file()

                    ext = splitext(dummy_name)[1]
                    if ext not in ['.jpg', '.jpeg', '.JPG', '.JPEG',
                                   '.png', '.PNG', '.gif', '.GIF',
                                   '.m4v', '.mov', '.MOV', '.mp4']:
                        self.libraryset[uid].unrecognized = True
                    uid += 1

            if not dummy_dirname:
                if not dummy_dirpath == self.src_path:
                    self.folders_to_delete.add(dummy_dirpath)
            else:
                for dirname in dummy_dirname:
                    self.folders_to_delete.add('{path}/{dirname}'.format(path=dummy_dirpath, dirname=dirname))

        sys.stdout.flush()
        sys.stdout.write('\tDone!\n')

    def make_new_dir(self):
        """
        Create new directories for sorted photos in a dst_dir.
        """

        sys.stdout.write('Create directories...')
        
        # create 'dst_dir/albums' folder just in case.
        # It's a root for a library.
        if 'albums' not in os.listdir(self.dst_path):
            os.mkdir(self.dst_path + '/' + 'albums/')
            
        for dummy_photo in self.libraryset.values():
            year = dummy_photo.get_datetime()[:4]
            month = dummy_photo.get_datetime()[5:7]
            day = dummy_photo.get_datetime()[8:10]

            if dummy_photo.unrecognized:
                if 'unrecognized' not in os.listdir('{path}/'.format(path=self.dst_path)):
                    os.mkdir('{path}/unrecognized'.format(path=self.dst_path))

            else:
                if year not in os.listdir('{path}/albums/'.format(path=self.dst_path)):
                    os.mkdir('{path}/albums/{year}'.format(path=self.dst_path, year=year))

                if month not in os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year=year)):
                    os.mkdir('{path}/albums/{year}/{month}'.format(path=self.dst_path, year=year, month=month))

                if day not in os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path, year=year, month=month)):
                    os.mkdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path, year=year, month=month, day=day))

        sys.stdout.write('\tDone!\n')

    def copy_src_to_dst(self):
        """ copy all photos from src_dir to dst_dir """

        sys.stdout.write('Moving files...\n')

        len_libraryset = float(len(self.libraryset))

        # copy all photos to dst_dir/albums/YYYY/MM/DD based on file's modified date
        for number, dummy_photo in enumerate(self.libraryset.values()):
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
                        name='{year}-{month}-{day}_{number}{ext}'.format(
                            year=year,
                            month=month,
                            day=day,
                            number=number,
                            ext=splitext(name)[1]
                        ),
                    )
                )

            # Delete old files.
            if self.delete_old:
                os.remove('{old_dir}/{name}'.format(old_dir=old_dir, name=name))

            self.update_progress((number+1) / len_libraryset)

            if self.delete_old:
                if not old_dir == self.src_path:
                    self.folders_to_delete.add(old_dir)

    def delete_old_folders(self):
        if self.delete_old:
            if self.src_path in self.folders_to_delete:
                raise Exception
            else:
                for fol in self.folders_to_delete:
                    rmtree(fol)

    @staticmethod
    def update_progress(progress):

        bar_length = 40
        status = ""
        if isinstance(progress, int):
            progress = float(progress)
        if not isinstance(progress, float):
            progress = 0
            status = "ERROR: progress var must be float\r\n"
        if progress < 0:
            progress = 0
            status = "Halt...\r\n"
        if progress >= 1:
            progress = 1
            status = "Done!\r\n"
        block = int(round(bar_length * progress))
        text = "\rProgress: [{0}] {1}% {2}".format("#" * block + "-" * (bar_length - block), int(progress * 100), status)
        sys.stdout.write(text)
        sys.stdout.flush()
