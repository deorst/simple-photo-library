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
    2.1. Two files.
    2.2. Two files and an empty folder.
    2.3. Two files in a folder.
    2.4. Two files in a folder in a folder.
    2.5. A file and a file in a folder.
    2.6. A file in a folder and a file in a folder in a folder.
    2.7. A file and a file in a folder in a folder.
    """

    def __init__(self, *args, **kwargs):
        self.dst_path = 'simpholib/tests/files_for_tests/dst'
        super(FunctionalityTest, self).__init__(*args, **kwargs)

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
        self.assertEqual(os.listdir(self.dst_path), ['1.jpg'])

        # 1.1.3. Set 'modified time' for that image file.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 1.1.4. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 1.1.5. Check new folder structure.
        self.assertEqual(os.listdir(self.dst_path), ['albums'])
        self.assertEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012'])
        self.assertEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
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
        self.assertEqual(os.listdir(self.dst_path), ['1.jpg', 'empty_folder'])

        # 1.2.4. Set 'modified time' for that image file.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 1.2.5. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 1.2.6. Check new folder structure.
        self.assertEqual(os.listdir(self.dst_path), ['albums'])
        self.assertEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012'])
        self.assertEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
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
        self.assertEqual(os.listdir(self.dst_path), ['folder'])
        self.assertEqual(os.listdir('{path}/folder'.format(path=self.dst_path)), ['1.jpg'])

        # 1.3.4. Set 'modified time' for that image file.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/folder/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 1.3.5. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 1.3.6. Check new folder structure.
        self.assertEqual(os.listdir(self.dst_path), ['albums'])
        self.assertEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012'])
        self.assertEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
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
        self.assertEqual(os.listdir(self.dst_path), ['empty_folder', 'folder_with_file'])

        # 1.4.3. Create an image file in one of the folders.
        picture = open('{path}/folder_with_file/1.jpg'.format(path=self.dst_path), 'w')
        picture.close()

        # 1.4.4. Check that image file is created.
        self.assertEqual(os.listdir('{path}/folder_with_file'.format(path=self.dst_path)), ['1.jpg'])

        # 1.4.5. Set 'modified time' for that image file.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/folder_with_file/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 1.4.6. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 1.4.7. Check new folder structure.
        self.assertEqual(os.listdir(self.dst_path), ['albums'])
        self.assertEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012'])
        self.assertEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
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
        self.assertEqual(os.listdir('{path}/'.format(path=self.dst_path)), ['folder_1'])
        self.assertEqual(os.listdir('{path}/folder_1/'.format(path=self.dst_path)), ['folder_2'])

        # 1.5.3. Create an image file in a folder.
        picture = open('{path}/folder_1/folder_2/1.jpg'.format(path=self.dst_path), 'w')
        picture.close()

        # 1.5.4. Check that image file is created.
        self.assertEqual(os.listdir('{path}/folder_1/folder_2/'.format(path=self.dst_path)), ['1.jpg'])

        # 1.5.5. Set 'modified time' for that image file.
        modified_time = time.mktime(datetime.datetime(2012, 06, 14, 12, 00).timetuple())
        os.utime('{path}/folder_1/folder_2/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))

        # 1.5.6. Run 'simpholib'.
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))

        # 1.5.7. Check new folder structure.
        self.assertEqual(os.listdir(self.dst_path), ['albums'])
        self.assertEqual(os.listdir('{path}/albums'.format(path=self.dst_path)), ['2012'])
        self.assertEqual(os.listdir('{path}/albums/{year}'.format(path=self.dst_path, year='2012')), ['06'])
        self.assertEqual(os.listdir('{path}/albums/{year}/{month}'.format(path=self.dst_path,
                                                                          year='2012',
                                                                          month='06')), ['14'])
        self.assertEqual(os.listdir('{path}/albums/{year}/{month}/{day}'.format(path=self.dst_path,
                                                                                year='2012',
                                                                                month='06',
                                                                                day='14')), ['2012-06-14_0.jpg'])

