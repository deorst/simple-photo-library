from unittest import TestCase
import time
import datetime
import os
import glob
from shutil import rmtree


class FunctionalityTest(TestCase):
    """
    Test Suite:

    ----Single File----
    1.1. Single file.
    1.2. Single file and an empty folder.
    1.3. Single file in a folder.
    1.4. Single file in a folder and an empty folder.
    1.5. Single file in a folder in a folder.

    ----Two Files----
    2.1. Two files with different modification time.
    2.2. Two files with same modification time.
    2.3. Two files with different modification time and a folder.
    2.4. Two files with same modification time and a folder.
    2.5. Two files in a folder.
    2.6. Two files in a folder in a folder.
    2.7. A file and a file in a folder.
    2.8. A file in a folder and a file in a folder in a folder.
    2.9. A file and a file in a folder in a folder.
    """

    def __init__(self, *args, **kwargs):
        self.dst_path = 'simpholib/tests/files_for_tests/dst'
        super(FunctionalityTest, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        # Create dirs for testing.
        os.mkdir('simpholib/tests/files_for_tests')
        os.mkdir('simpholib/tests/files_for_tests/src')
        os.mkdir('simpholib/tests/files_for_tests/dst')

        # Install library.
        os.system('pip install simpholib')
        super(FunctionalityTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        # Remove dirs for testing.
        rmtree('simpholib/tests/files_for_tests')
        super(FunctionalityTest, cls).tearDownClass()

    def setUp(self):
        # Check that ./files_for_tests is empty.
        self.assertFalse(glob.glob('{path}/*'.format(path=self.dst_path)))
        super(FunctionalityTest, self).setUp()

    def tearDown(self):
        # Clean up dst_path.
        for child in os.listdir('{path}'.format(path=self.dst_path)):
            if os.path.isdir('{path}/{child}'.format(path=self.dst_path, child=child)):
                rmtree('{path}/{child}'.format(path=self.dst_path, child=child))
            else:
                os.remove('{path}/{child}'.format(path=self.dst_path, child=child))
        super(FunctionalityTest, self).tearDown()

#    ----Single File----

    def test_single_file(self):
        """
        1.1. Single file.
            1.1.1. Create an image file.
            1.1.2. Check that image file is created.
            1.1.3. Set 'modified time' for that image file.
            1.1.4. Run 'simpholib'.
            1.1.5. Check new folder structure.
        """

        # 1.1.1. Create an image file.
        picture = open('{path}/1.jpg'.format(path=self.dst_path), 'w')
        picture.close()

        # 1.1.2. Check that image file is created.
        self.assertItemsEqual(os.listdir(self.dst_path), ['1.jpg'])

        # 1.1.3. Set 'modified time' for that image file.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 1.1.4. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 1.1.5. Check new folder structure.
        self.assertItemsEqual(os.listdir(self.dst_path), ['albums'])

        self.assertItemsEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012'])

        self.assertItemsEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])

        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                              year='2012',
                                                                              month='06')), ['14'])

        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
                                                                                    year='2012',
                                                                                    month='06',
                                                                                    day='14')), ['2012-06-14_0.jpg'])

    def test_single_file_and_an_empty_folder(self):
        """
        1.2. Single file and an empty folder.
            1.2.1. Create an image file.
            1.2.2. Create an empty folder.
            1.2.3. Check that image file and folder are created.
            1.2.4. Set 'modified time' for that image file.
            1.2.5. Run 'simpholib'.
            1.2.6. Check new folder structure.
        """
        # 1.2.1. Create an image file.
        picture = open('{path}/1.jpg'.format(path=self.dst_path), 'w')
        picture.close()

        # 1.2.2. Create an empty folder.
        os.mkdir('{path}/empty_folder'.format(path=self.dst_path))

        # 1.2.3. Check that image file and folder are created.
        self.assertItemsEqual(os.listdir(self.dst_path), ['1.jpg', 'empty_folder'])

        # 1.2.4. Set 'modified time' for that image file.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 1.2.5. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 1.2.6. Check new folder structure.
        self.assertItemsEqual(os.listdir(self.dst_path), ['albums'])
        self.assertItemsEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
                                                                                year='2012',
                                                                                month='06',
                                                                                day='14')), ['2012-06-14_0.jpg'])

    def test_single_file_in_a_folder(self):
        """
        1.3. Single file in a folder.
            1.3.1. Create an empty folder.
            1.3.2. Create an image file in a folder.
            1.3.3. Check that image file is created.
            1.3.4. Set 'modified time' for that image file.
            1.3.5. Run 'simpholib'.
            1.3.6. Check new folder structure.
        """

        # 1.3.1. Create an empty folder.
        os.mkdir('{path}/folder'.format(path=self.dst_path))

        # 1.3.2. Create an image file in a folder.
        picture = open('{path}/folder/1.jpg'.format(path=self.dst_path), 'w')
        picture.close()

        # 1.3.3. Check that image file is created.
        self.assertItemsEqual(os.listdir(self.dst_path), ['folder'])
        self.assertItemsEqual(os.listdir('{path}/folder'.format(path=self.dst_path)), ['1.jpg'])

        # 1.3.4. Set 'modified time' for that image file.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/folder/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 1.3.5. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 1.3.6. Check new folder structure.
        self.assertItemsEqual(os.listdir(self.dst_path), ['albums'])
        self.assertItemsEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
                                                                                year='2012',
                                                                                month='06',
                                                                                day='14')), ['2012-06-14_0.jpg'])

    def test_single_file_in_a_folder_and_an_empty_folder(self):
        """
        1.4. Single file in a folder and an empty folder.
            1.4.1. Create 2 empty folders.
            1.4.2. Check that folders are created.
            1.4.3. Create an image file in one of the folders.
            1.4.4. Check that image file is created.
            1.4.5. Set 'modified time' for that image file.
            1.4.6. Run 'simpholib'.
            1.4.7. Check new folder structure.
        """

        # 1.4.1. Create 2 empty folders.
        os.mkdir('{path}/folder_with_file'.format(path=self.dst_path))
        os.mkdir('{path}/empty_folder'.format(path=self.dst_path))

        # 1.4.2. Check that folders are created.
        self.assertItemsEqual(os.listdir(self.dst_path), ['empty_folder', 'folder_with_file'])

        # 1.4.3. Create an image file in one of the folders.
        picture = open('{path}/folder_with_file/1.jpg'.format(path=self.dst_path), 'w')
        picture.close()

        # 1.4.4. Check that image file is created.
        self.assertItemsEqual(os.listdir('{path}/folder_with_file'.format(path=self.dst_path)), ['1.jpg'])

        # 1.4.5. Set 'modified time' for that image file.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/folder_with_file/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 1.4.6. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 1.4.7. Check new folder structure.
        self.assertItemsEqual(os.listdir(self.dst_path), ['albums'])
        self.assertItemsEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
                                                                                year='2012',
                                                                                month='06',
                                                                                day='14')), ['2012-06-14_0.jpg'])

    def test_single_file_in_a_folder_in_a_folder(self):
        """
        1.5. Single file in a folder in a folder.
            1.5.1. Create an empty folder in a folder.
            1.5.2. Check that folders are created.
            1.5.3. Create an image file in a folder.
            1.5.4. Check that image file is created.
            1.5.5. Set 'modified time' for that image file.
            1.5.6. Run 'simpholib'.
            1.5.7. Check new folder structure.
        """

        # 1.5.1. Create an empty folder in a folder.
        os.mkdir('{path}/folder_1/'.format(path=self.dst_path))
        os.mkdir('{path}/folder_1/folder_2/'.format(path=self.dst_path))

        # 1.5.2. Check that folders are created.
        self.assertItemsEqual(os.listdir('{path}/'.format(path=self.dst_path)), ['folder_1'])
        self.assertItemsEqual(os.listdir('{path}/folder_1/'.format(path=self.dst_path)), ['folder_2'])

        # 1.5.3. Create an image file in a folder.
        picture = open('{path}/folder_1/folder_2/1.jpg'.format(path=self.dst_path), 'w')
        picture.close()

        # 1.5.4. Check that image file is created.
        self.assertItemsEqual(os.listdir('{path}/folder_1/folder_2/'.format(path=self.dst_path)), ['1.jpg'])

        # 1.5.5. Set 'modified time' for that image file.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/folder_1/folder_2/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 1.5.6. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 1.5.7. Check new folder structure.
        self.assertItemsEqual(os.listdir(self.dst_path), ['albums'])
        self.assertItemsEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
                                                                                year='2012',
                                                                                month='06',
                                                                                day='14')), ['2012-06-14_0.jpg'])

#   ----Two Files----

    def test_two_files_with_different_mod_time(self):
        """
        2.1. Two image files with different modification time.
            2.1.1. Create two image files.
            2.1.2. Check that folders and files are created.
            2.1.3. Set different 'modified time' for image files.
            2.1.4. Run 'simpholib'.
            2.1.5. Check new folder structure.
        """

        # 2.1.1. Create two image files.
        picture_1 = open('{path}/1.jpg'.format(path=self.dst_path), 'w')
        picture_1.close()

        picture_2 = open('{path}/2.jpg'.format(path=self.dst_path), 'w')
        picture_2.close()

        # 2.1.2. Check that files are created.
        self.assertItemsEqual(os.listdir('{path}/'.format(path=self.dst_path)), ['1.jpg', '2.jpg'])

        # 2.1.3. Set different 'modified time' for image files.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        modified_time = time.mktime(datetime.datetime(2013, 07, 06, 12, 00).timetuple())
        os.utime('{path}/2.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 2.1.4. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 2.1.5. Check new folder structure.
        self.assertItemsEqual(os.listdir(self.dst_path), ['albums'])
        self.assertItemsEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012', '2013'])

        # Check folder structure for first picture file.
        self.assertItemsEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
                                                                                year='2012',
                                                                                month='06',
                                                                                day='14')), ['2012-06-14_0.jpg'])

        # Check folder structure for second picture file.
        self.assertItemsEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2013')), ['07'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2013',
                                                                          month='07')), ['06'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
                                                                                year='2013',
                                                                                month='07',
                                                                                day='06')), ['2013-07-06_1.jpg'])

    def test_two_files_with_same_mod_time(self):
        """
        2.2. Two image files with same modification time.
            2.2.1. Create two image files.
            2.2.2. Check that folders and files are created.
            2.2.3. Set same 'modified time' for image files.
            2.2.4. Run 'simpholib'.
            2.2.5. Check new folder structure.
        """

        # 2.2.2. Create two image files.
        picture_1 = open('{path}/1.jpg'.format(path=self.dst_path), 'w')
        picture_1.close()

        picture_2 = open('{path}/2.jpg'.format(path=self.dst_path), 'w')
        picture_2.close()

        # 2.2.3. Check that folders and files are created.
        self.assertItemsEqual(os.listdir('{path}/'.format(path=self.dst_path)), ['1.jpg', '2.jpg'])

        # 2.2.4. Set different 'modified time' for image files.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))
        os.utime('{path}/2.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 2.2.5. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 2.2.6. Check new folder structure.
        self.assertItemsEqual(os.listdir(self.dst_path), ['albums'])
        self.assertItemsEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012'])

        # Check folder structure for first picture file.
        self.assertItemsEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
                                                                                year='2012',
                                                                                month='06',
                                                                                day='14')), ['2012-06-14_0.jpg',
                                                                                             '2012-06-14_1.jpg'])

    def test_two_files_with_different_mod_time_and_empty_folders(self):
        """
        2.3. Two image files with different modification time.
            2.3.1. Create empty folders - just to mess up a little bit.
            2.3.2. Create two image files.
            2.3.3. Check that folders and files are created.
            2.3.4. Set different 'modified time' for image files.
            2.3.5. Run 'simpholib'.
            2.3.6. Check new folder structure.
        """

        # 2.3.1. Create empty folders - just to mess up a little bit.
        os.mkdir('{path}/folder_1/'.format(path=self.dst_path))
        os.mkdir('{path}/folder_1/folder_2/'.format(path=self.dst_path))

        # 2.3.2. Create two image files.
        picture_1 = open('{path}/1.jpg'.format(path=self.dst_path), 'w')
        picture_1.close()

        picture_2 = open('{path}/2.jpg'.format(path=self.dst_path), 'w')
        picture_2.close()

        # 2.3.3. Check that folders and files are created.
        self.assertItemsEqual(os.listdir('{path}/'.format(path=self.dst_path)), ['1.jpg', '2.jpg', 'folder_1'])
        self.assertItemsEqual(os.listdir('{path}/folder_1/'.format(path=self.dst_path)), ['folder_2'])

        # 2.3.4. Set different 'modified time' for image files.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        modified_time = time.mktime(datetime.datetime(2013, 07, 06, 12, 00).timetuple())
        os.utime('{path}/2.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 2.3.5. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 2.3.6. Check new folder structure.
        self.assertItemsEqual(os.listdir(self.dst_path), ['albums'])
        self.assertItemsEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012', '2013'])

        # Check folder structure for first picture file.
        self.assertItemsEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
                                                                                year='2012',
                                                                                month='06',
                                                                                day='14')), ['2012-06-14_0.jpg'])

        # Check folder structure for second picture file.
        self.assertItemsEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2013')), ['07'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2013',
                                                                          month='07')), ['06'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
                                                                                year='2013',
                                                                                month='07',
                                                                                day='06')), ['2013-07-06_1.jpg'])

    def test_two_files_with_same_mod_time_and_empty_folders(self):
        """
        2.4. Two image files with same modification time.
            2.4.1. Create empty folders - just to mess up a little bit.
            2.4.2. Create two image files.
            2.4.3. Check that folders and files are created.
            2.4.4. Set same 'modified time' for image files.
            2.4.5. Run 'simpholib'.
            2.4.6. Check new folder structure.
        """

        # 2.4.1. Create empty folders - just to mess up a little bit.
        os.mkdir('{path}/folder_1/'.format(path=self.dst_path))
        os.mkdir('{path}/folder_1/folder_2/'.format(path=self.dst_path))

        # 2.4.2. Create two image files.
        picture_1 = open('{path}/1.jpg'.format(path=self.dst_path), 'w')
        picture_1.close()

        picture_2 = open('{path}/2.jpg'.format(path=self.dst_path), 'w')
        picture_2.close()

        # 2.4.3. Check that folders and files are created.
        self.assertItemsEqual(os.listdir('{path}/'.format(path=self.dst_path)), ['1.jpg', '2.jpg', 'folder_1'])
        self.assertItemsEqual(os.listdir('{path}/folder_1/'.format(path=self.dst_path)), ['folder_2'])

        # 2.4.4. Set different 'modified time' for image files.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))
        os.utime('{path}/2.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 2.4.5. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 2.4.6. Check new folder structure.
        self.assertItemsEqual(os.listdir(self.dst_path), ['albums'])
        self.assertItemsEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012'])

        # Check folder structure for first picture file.
        self.assertItemsEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
                                                                                year='2012',
                                                                                month='06',
                                                                                day='14')), ['2012-06-14_0.jpg',
                                                                                             '2012-06-14_1.jpg'])

    def test_two_files_in_a_folder(self):
        """
        2.5. Two files in a folder.
            2.5.1. Create an empty folder.
            2.5.2. Create an image file in a folder.
            2.5.3. Check that image file is created.
            2.5.4. Set 'modified time' for that image file.
            2.5.5. Run 'simpholib'.
            2.5.6. Check new folder structure.
        """

        # 2.5.1. Create an empty folder.
        os.mkdir('{path}/folder'.format(path=self.dst_path))

        # 2.5.2. Create two image files in a folder.
        picture = open('{path}/folder/1.jpg'.format(path=self.dst_path), 'w')
        picture.close()

        picture = open('{path}/folder/2.jpg'.format(path=self.dst_path), 'w')
        picture.close()

        # 2.5.3. Check that image files and folder are created.
        self.assertItemsEqual(os.listdir(self.dst_path), ['folder'])
        self.assertItemsEqual(os.listdir('{path}/folder'.format(path=self.dst_path)), ['1.jpg', '2.jpg'])

        # 2.5.4. Set 'modified time' for image files.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/folder/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))
        os.utime('{path}/folder/2.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 2.5.5. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 2.5.6. Check new folder structure.
        self.assertItemsEqual(os.listdir(self.dst_path), ['albums'])
        self.assertItemsEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
                                                                                year='2012',
                                                                                month='06',
                                                                                day='14')), ['2012-06-14_0.jpg',
                                                                                             '2012-06-14_1.jpg'])

    def test_two_files_in_a_folder_in_a_folder(self):
        """
        2.6. Single file in a folder in a folder.
            2.6.1. Create an empty folder in a folder.
            2.6.2. Check that folders are created.
            2.6.3. Create an image file in a folder.
            2.6.4. Check that image file is created.
            2.6.5. Set 'modified time' for that image file.
            2.6.6. Run 'simpholib'.
            2.6.7. Check new folder structure.
        """

        # 2.6.1. Create an empty folder in a folder.
        os.mkdir('{path}/folder_1/'.format(path=self.dst_path))
        os.mkdir('{path}/folder_1/folder_2/'.format(path=self.dst_path))

        # 2.6.2. Check that folders are created.
        self.assertItemsEqual(os.listdir('{path}/'.format(path=self.dst_path)), ['folder_1'])
        self.assertItemsEqual(os.listdir('{path}/folder_1/'.format(path=self.dst_path)), ['folder_2'])

        # 2.6.3. Create an two image files in a folder.
        picture = open('{path}/folder_1/folder_2/1.jpg'.format(path=self.dst_path), 'w')
        picture.close()

        picture = open('{path}/folder_1/folder_2/2.jpg'.format(path=self.dst_path), 'w')
        picture.close()

        # 2.6.4. Check that image file is created.
        self.assertItemsEqual(os.listdir('{path}/folder_1/folder_2/'.format(path=self.dst_path)), ['1.jpg', '2.jpg'])

        # 2.6.5. Set 'modified time' for that image file.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/folder_1/folder_2/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))
        os.utime('{path}/folder_1/folder_2/2.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 2.6.6. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 1.5.7. Check new folder structure.
        self.assertItemsEqual(os.listdir(self.dst_path), ['albums'])
        self.assertItemsEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
                                                                                year='2012',
                                                                                month='06',
                                                                                day='14')), ['2012-06-14_0.jpg',
                                                                                             '2012-06-14_1.jpg'])

    def test_a_file_and_a_file_in_a_folder(self):
        """
        2.7. A file and a file in a folder.
            2.7.1. Create an empty folder.
            2.7.2. Check that folder is created.
            2.7.3. Create an image file and and image file in a folder.
            2.7.4. Check that image files are created.
            2.7.5. Set 'modified time' for image file.
            2.7.6. Run 'simpholib'.
            2.7.7. Check new folder structure.
        """

        # 2.7.1. Create an empty folder.
        os.mkdir('{path}/folder'.format(path=self.dst_path))

        # 2.7.2. Check that folder is created.
        self.assertItemsEqual(os.listdir(self.dst_path), ['folder'])

        # 2.7.3. Create two image files in a folder.
        picture = open('{path}/1.jpg'.format(path=self.dst_path), 'w')
        picture.close()

        picture = open('{path}/folder/2.jpg'.format(path=self.dst_path), 'w')
        picture.close()

        # 2.7.4. Check that image files and folder are created.
        self.assertItemsEqual(os.listdir('{path}/'.format(path=self.dst_path)), ['1.jpg', 'folder'])
        self.assertItemsEqual(os.listdir('{path}/folder'.format(path=self.dst_path)), ['2.jpg'])

        # 2.7.5. Set 'modified time' for image files.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))
        os.utime('{path}/folder/2.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 2.7.6. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 2.7.7. Check new folder structure.
        self.assertItemsEqual(os.listdir(self.dst_path), ['albums'])
        self.assertItemsEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
                                                                                year='2012',
                                                                                month='06',
                                                                                day='14')), ['2012-06-14_0.jpg',
                                                                                             '2012-06-14_1.jpg'])

    def test_a_file_in_a_foler_and_a_file_in_a_folder_in_a_folder(self):
        """
        2.8. A file in a folder and a file in a folder in a folder.
            2.8.1. Create an empty folder in a folder.
            2.8.2. Check that folder is created.
            2.8.3. Create an image file and and image file in a folder.
            2.8.4. Check that image files are created.
            2.8.5. Set 'modified time' for image file.
            2.8.6. Run 'simpholib'.
            2.8.7. Check new folder structure.
        """

        # 2.8.1. Create an empty folder.
        os.mkdir('{path}/folder_1'.format(path=self.dst_path))
        os.mkdir('{path}/folder_1/folder_2'.format(path=self.dst_path))

        # 2.8.2. Check that folder is created.
        self.assertItemsEqual(os.listdir(self.dst_path), ['folder_1'])
        self.assertItemsEqual(os.listdir('{path}/folder_1'.format(path=self.dst_path)), ['folder_2'])

        # 2.8.3. Create an image file in a folder and another in a folder in a folder.
        picture = open('{path}/folder_1/1.jpg'.format(path=self.dst_path), 'w')
        picture.close()

        picture = open('{path}/folder_1/folder_2/2.jpg'.format(path=self.dst_path), 'w')
        picture.close()

        # 2.8.4. Check that image files and folder are created.
        self.assertItemsEqual(os.listdir('{path}/folder_1'.format(path=self.dst_path)), ['1.jpg', 'folder_2'])
        self.assertItemsEqual(os.listdir('{path}/folder_1/folder_2'.format(path=self.dst_path)), ['2.jpg'])

        # 2.8.5. Set 'modified time' for image files.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/folder_1/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))
        os.utime('{path}/folder_1/folder_2/2.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 2.8.6. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 2.8.7. Check new folder structure.
        self.assertItemsEqual(os.listdir(self.dst_path), ['albums'])
        self.assertItemsEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
                                                                                year='2012',
                                                                                month='06',
                                                                                day='14')), ['2012-06-14_0.jpg',
                                                                                             '2012-06-14_1.jpg'])

    def test_a_file_and_a_file_in_a_folder_in_a_folder(self):
        """
        2.9. A file and a file in a folder in a folder.
            2.9.1. Create an empty folder in a folder.
            2.9.2. Check that folder is created.
            2.9.3. Create an image file and and image file in a folder.
            2.9.4. Check that image files are created.
            2.9.5. Set 'modified time' for image file.
            2.9.6. Run 'simpholib'.
            2.9.7. Check new folder structure.
        """

        # 2.9.1. Create an empty folder.
        os.mkdir('{path}/folder_1'.format(path=self.dst_path))
        os.mkdir('{path}/folder_1/folder_2'.format(path=self.dst_path))

        # 2.9.2. Check that folder is created.
        self.assertItemsEqual(os.listdir(self.dst_path), ['folder_1'])
        self.assertItemsEqual(os.listdir('{path}/folder_1'.format(path=self.dst_path)), ['folder_2'])

        # 2.9.3. Create an image file in a folder and another in a folder in a folder.
        picture = open('{path}/1.jpg'.format(path=self.dst_path), 'w')
        picture.close()

        picture = open('{path}/folder_1/folder_2/2.jpg'.format(path=self.dst_path), 'w')
        picture.close()

        # 2.9.4. Check that image files and folder are created.
        self.assertItemsEqual(os.listdir('{path}/'.format(path=self.dst_path)), ['1.jpg', 'folder_1'])
        self.assertItemsEqual(os.listdir('{path}/folder_1/folder_2'.format(path=self.dst_path)), ['2.jpg'])

        # 2.9.5. Set 'modified time' for image files.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))
        os.utime('{path}/folder_1/folder_2/2.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 2.9.6. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 2.9.7. Check new folder structure.
        self.assertItemsEqual(os.listdir(self.dst_path), ['albums'])
        self.assertItemsEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertItemsEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
                                                                                year='2012',
                                                                                month='06',
                                                                                day='14')), ['2012-06-14_0.jpg',
                                                                                             '2012-06-14_1.jpg'])