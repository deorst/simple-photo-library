import action
import os
import sys


def main():

    # Helpers.
    def check_path(path):
        if not os.path.exists(path):
            print "Path '%s' doesn't exist!" % path
            sys.exit(0)

    # Checks for user input.
    user_input = sys.argv

    if len(user_input) <= 1:
        print 'At least source directory should be passed.'
        sys.exit(0)
    elif len(user_input) == 2:
        src_dir = user_input[1]
        check_path(src_dir)
        dst_dir=None

    elif len(user_input) == 3:
        src_dir = user_input[1]
        dst_dir = user_input[2]
        for path in [src_dir, dst_dir]:
            check_path(path)

    action.main(src_dir, dst_dir)

