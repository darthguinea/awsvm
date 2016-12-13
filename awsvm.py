import os
import sys, getopt
import ConfigParser
from config import Config
from os.path import expanduser


def user_options():
    print "awsvm:\t\t- Switch aws credentials"
    print "  -?\t\tDisplay Help"
    print "  -l\t\tList accounts"
    exit(1)


def list_accounts():
    print "You have the following AWS accounts configured:\n"
    for section in config.sections():
        print "\t{0:20}{1}".format(section, config.get(section, 'aws_access_key_id'))
    exit()


def default_exists(selection):
    aws_default_id = config.get('default', 'aws_access_key_id')

    for section in config.sections():
        # If the default key does not exist, then we do not want to overwrite it
        if section != 'default' \
                and config.get(section, 'aws_access_key_id') == aws_default_id:
            return True
    return False


def save_default():
    print "'default' does not have a backup name" 
    var = raw_input("Please enter a name to save 'default' to: ")

    print "1"

    default_id = config.get('default', 'aws_access_key_id')
    default_key = config.get('default', 'aws_secret_access_key')

    print "2"

    config.set(var, 'aws_access_key_id', default_id)
    config.set(var, 'aws_secret_access_key', default_key)

    print "3"

    print "path" + expanduser(creds_file)

    with open(expanduser(creds_file), 'w') as configfile:
        config.write(configfile)


def set_selection(config, selection):
    config.set_selection(selection)


def backup_config(config):
    config.list_accounts()
    if not config.default_backup_exists():
        config.backup_default()


def main(argv):
    config = Config()

    try:
        opts, args = getopt.getopt(argv, "l?")
    except getopt.GetoptError:
        user_options()

    for opt, arg in opts:
        if opt == '-?':
            user_options()
        elif opt == '-l':
            config.list_accounts()

    try:
        set_selection(config, argv[0])
    except:
        config.list_accounts()

if __name__ == '__main__':
    main(sys.argv[1:])
