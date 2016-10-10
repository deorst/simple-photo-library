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
        self.dst_path = 'simpholib/tests/files_for_test/dst'
        super(FunctionalityTest, self).__init__(*args, **kwargs)

    def setUp(self):
        # Check that ./files_for_test is empty.
        self.assertFalse(glob.glob('{path}/*'.format(path=self.dst_path)))
        super(FunctionalityTest, self).setUp()

    def tearDown(self):
        # Remove all files.
        # for filename in os.listdir(self.dst_path):
        #     os.remove('{path}/{filename}'.format(path=self.dst_path, filename=filename))
        super(FunctionalityTest, self).tearDown()

    def test_single_file(self):
        """
        1.1. Single file.
        """
        picture = open('{path}/1.jpg'.format(path=self.dst_path), 'w')
        picture.close()
        modified_time = time.mktime(datetime.datetime(2012, 06, 14).timetuple())
        os.utime('{path}/1.jpg'.format(path=self.dst_path), (modified_time, modified_time))
        time.sleep(5)
        os.system('simpho ./{dst_path}/'.format(dst_path=self.dst_path))
