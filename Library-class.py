# The objective of that file is to create a Library class.
# An instance of the Library should have the properties listed below:
# ..., current_uid (this value will assigned to the instances of the Photo class
# one by one with Photo.get_uid() method), ...

class Library:
    def __init__(self, current_uid = 0):
        self.current_uid = current_uid
        
    def __str__(self):
        s = 'current uid:\t' + str(self.current_uid)
        return s
        
    def generate_uid(self):
        """ generate uid for the 'Photo.get_uid()' """
        pass
        
# test phase


        