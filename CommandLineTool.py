#!/urs/bin/env python3

import cmd
import sys
import readline
import rlcompleter
from AprilTagStuff import *
from Database import *
import firebase_admin
from firebase_admin import credentials, firestore


class CommandLineTool(cmd.Cmd):
    intro = 'Welcome to Galaxy MilkyWay. Type help or ? to list commands \n'
    prompt = '(Database) '
    file = None

    def do_update(self, arg):
        """Pulls old image from database and compares it to new image"""
        img = cv2.imread(arg, cv2.IMREAD_GRAYSCALE)
        tags = scan_image(img)

        for tag in tags:
            print("Updating tag {0} location".format(tag))
        collect_data(ref, tags, None)

    def do_sync(self, arg):
        """Scan tagged equipment into system **one at a time**"""
        ls = arg.split()
        img = cv2.imread(ls[0], cv2.IMREAD_GRAYSCALE)
        tags = scan_image(img)
        if len(ls) != 1:
            print("One image at a time")
        else:
            img = cv2.imread(ls[0], cv2.IMREAD_GRAYSCALE)
            tags = scan_image(img)
            d2 = {}

            for t in tags:
                print("Information for Tag {0}".format(t))
                name = None
                while not name:
                    name = input("Enter Equipment Name >> ")
                owner = None
                while not owner:
                    owner = input("Enter Ownership Here >> ")
                d2[t] = (name, owner)
            collect_data(ref, tags, d2)

    def do_highlight(self, arg):
        """test highlight"""
        ls = arg.split()

        for l in ls:
            a = cv2.imread(l, cv2.IMREAD_GRAYSCALE)
            cv2.imwrite('highlighted_' + l, highlight_image(a))

    def do_exit(self, arg):
        sys.exit()


if __name__ == '__main__':
    if not len(firebase_admin._apps):
        cred = credentials.Certificate("technica2019-firebase-adminsdk-2gyis-fdf3974fd6.json")
        app = firebase_admin.initialize_app(cred, {
            'projectId': 'technica2019',
        })
    else:
        app = firebase_admin.get_app()
    ref = firestore.client()

    CommandLineTool().cmdloop()
