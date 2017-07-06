import os
import sys, getopt
import ConfigParser
from config import Config
from os.path import expanduser


def user_options():
    print "awsvm - A tool to switch aws credentials"
    print "  -?\t\tDisplay Help"
    print "  -l\t\tList accounts"
    print "  -a\t\tAdd account"
    print "  -d\t\tDelete account"
    exit(1)


def set_selection(config, selection):
    config.set_selection(selection)


def main(argv):
    lAccounts = True
    config = Config()

    try:
        opts, args = getopt.getopt(argv, "?adl", ["list", "add"])
    except getopt.GetoptError:
        user_options()

    for opt, arg in opts:
        if opt == '-?':
            user_options()
        elif opt in ('-l', '--list'):
            config.list_accounts()
            lAccounts = False
        elif opt in ('-a', '--add'):
            config.add_account()
            lAccounts = False
        elif opt == '-d':
            config.delete_account()
            lAccounts = False

    try:
        set_selection(config, argv[0])
    except:
        if lAccounts:
            config.list_accounts()

if __name__ == '__main__':
    main(sys.argv[1:])
