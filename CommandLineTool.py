#!/urs/bin/env python3

import cmd
import sys
import readline
import rlcompleter
from AprilTagStuff import *
from Database import *
import firebase_admin
from firebase_admin import credentials


class CommandLineTool(cmd.Cmd):
    intro = 'Welcome to Galaxy MilkyWay. Type help or ? to list commands \n'
    prompt = '(Database)'
    file = None

    def do_update(self, arg):
        """Pulls old image from database and compares it to new image"""
        # pull old image
        img = cv2.imread(arg, cv2.IMREAD_GRAYSCALE)
        tags = scan_image(img)

        for tag in tags:
            print("Updating tag {0} location".format(tag))
            # update database

    def do_sync(self, arg):
        """Scan tagged equipment into system **one at a time**"""
        ls = arg.split()
        img = cv2.imread(ls[0], cv2.IMREAD_GRAYSCALE)
        tags = scan_image(img)
        if len(ls) != 1 or len(tags) != 1:
            print("One tag at a time")
        else:
            img = cv2.imread(ls[0], cv2.IMREAD_GRAYSCALE)
            tags = scan_image(img)

            for t in tags:
                print("Information for Tag {0}".format(t))
                name = None
                while not name:
                    name = input("Enter Equipment Name >> ")
                owner = None
                while not owner:
                    owner = input("Enter Ownership Here >> ")
            # push dict and fields to db

    def do_highlight(self, arg):
        """test highlight"""
        ls = arg.split()

        for l in ls:
            a = cv2.imread(l, cv2.IMREAD_GRAYSCALE)
            cv2.imwrite('highlighted_' + l, highlight_image(a))

    def do_exit(self, arg):
        sys.exit()


if __name__ == '__main__':
    cred = credentials.Certificate("path/to/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    CommandLineTool().cmdloop()
