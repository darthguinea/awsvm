import ConfigParser
from os.path import expanduser

class Config(object):

    def __init__(self, creds_file='~/.aws/credentials'):
        self.creds_file = expanduser(creds_file)
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open(expanduser(creds_file)))


    def set_selection(self, selection):
        if not self.default_backup_exists():
            self.backup_default()

        for section in self.config.sections():
            if selection == section:
                aws_id = self.config.get(selection, 'aws_access_key_id')
                aws_key = self.config.get(selection, 'aws_secret_access_key')

        self.config.set('default', 'aws_access_key_id', aws_id)
        self.config.set('default', 'aws_access_key_id', aws_id)

        with open(self.creds_file, 'w') as configfile:
            self.config.write(configfile)


    def list_accounts(self):
        print "You have the following AWS accounts: "
        for section in self.config.sections():
            print "\t{0:20}{1}".format(section, self.config.get(section, 'aws_access_key_id'))
        print


    def default_backup_exists(self):
        default_key_id = self.config.get('default', 'aws_access_key_id')
        for section in self.config.sections():
            if section != 'default' \
                    and default_key_id == self.config.get(section, 'aws_access_key_id'):
                return True
        return False


    def backup_default(self):
        print "A backup of 'default' does not exist"
        section = raw_input("Please enter a backup name for 'default': ")

        if section.strip() is "":
            print "Not backing up, exiting "
            exit()

        default_id  = self.config.get('default', 'aws_access_key_id')
        default_key = self.config.get('default', 'aws_secret_access_key')

        self.config.add_section(section)
        self.config.set(section, 'aws_access_key_id', default_id)
        self.config.set(section, 'aws_secret_access_key', default_key)

        with open(self.creds_file, 'w') as configfile:
            self.config.write(configfile)
