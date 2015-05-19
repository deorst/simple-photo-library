# The objective of that file is to create a Photo class.
# An instance of the Photo should have the properties listed below:
# An uid(not name), name, path, datetime.
# uid will be randomly generated, name, path will be original.
# datetime will be extracted from EXIF or from MODIFIED date and time data.

class Photo:
    def __init__(self, directory, name):
        self.directory = directory
        self.name = name
        self.datetime = None            # an instance of Photo will get datetime and uid
        self.uid = None                 # later. So they're 'None' for now.
