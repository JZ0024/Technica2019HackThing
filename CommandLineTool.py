#!/urs/bin/env python3

import cmd
import sys
import readline
import rlcompleter
from AprilTagStuff import *
from Database import *
from google.cloud import firestore

#firebase = firebase.FirebaseApplication('')


class CommandLineTool(cmd.Cmd):
    intro = 'Welcome to Galaxy MilkyWay. Type help or ? to list commands \n'
    prompt = '(Database)'
    file = None


    # read line functionality
    readline.parse_and_bind("tab: complete")

# ----- commands in database ( methods to be updated after 10:15 PM 09Nov19 -----
# getting the collection of users from db


#users_ref = db.collection(u'users')
#docs = users_ref.stream()

#for doc in docs:
    #print(u'{} => {}'.format(doc.id, doc.to_dict()))


    def do_update(self, arg):
        """Pulls old image from database and compares it to new image"""
        # pull old image
        img1 = #pull from db
        tags = scan_image(img1)
        for tag in tags:
            print("Updating tag %s location".format(# db tag name))
            # update database
        print("Finished Update")


    def do_sync(self, arg):
        """Scan tagged equipment into system **one at a time**"""
        ls = arg.split()
        if ls.size > 1:
            print("One at a time")
        else:
            tags = get_tags(ls[0])

            for t in tags:
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
    CommandLineTool().cmdloop()
