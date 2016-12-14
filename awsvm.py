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
    exit(1)


def default_exists(selection):
    aws_default_id = config.get('default', 'aws_access_key_id')

    for section in config.sections():
        # If the default key does not exist, then we do not want to overwrite it
        if section != 'default' \
                and config.get(section, 'aws_access_key_id') == aws_default_id:
            return True
    return False


def set_selection(config, selection):
    config.set_selection(selection)


def backup_config(config):
    config.list_accounts()
    if not config.default_backup_exists():
        config.backup_default()


def main(argv):
    config = Config()

    try:
        opts, args = getopt.getopt(argv, "l?a")
    except getopt.GetoptError:
        user_options()

    for opt, arg in opts:
        if opt == '-?':
            user_options()
        elif opt == '-l':
            config.list_accounts()
        elif opt == '-a':
            config.add_account()

    try:
        set_selection(config, argv[0])
    except:
        config.list_accounts()

if __name__ == '__main__':
    main(sys.argv[1:])
