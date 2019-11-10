#!/urs/bin/env python3

import cmd
import sys
import readline
import rlcompleter

from Database import *
from firebase import firebase

firebase = firebase.FirebaseApplication('')



class CommandLineTool(cmd.Cmd):
    intro = 'Welcome to Galaxy MilkyWay. Type help or ? to list commands \n'
    prompt = '(Database)'
    file = None


# read line functionality
readline.parse_and_bind("tab: complete")


# ----- commands in database ( methods to be updated after 10:15 PM 09Nov19 -----
def do_undo(self, arg):
    """Undo (repeatedly) the last database action(s):  UNDO"""


def do_reset(self, arg):
    """Clear the screen and return turtle to center:  RESET"""
    reset()


def do_bye(self, arg):
    """close the window:  BYE"""
    print('Thank you for using the database')
    self.close()
    bye()
    return True


if __name__ == '__main__':
    CommandLineTool().cmdloop()
