import ConfigParser
from os.path import expanduser


class Config(object):

    def __init__(self, creds_file='~/.aws/credentials'):
        self.creds_file = expanduser(creds_file)
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open(expanduser(creds_file)))


    def get_user_input(self, message):
        var = raw_input(message + " (type q to quit): ")

        if var.strip() == "q":
            exit(0)
        
        return var.strip()


    def set_selection(self, selection):
        if not self.default_backup_exists():
            self.backup_default()

        for section in self.config.sections():
            if selection == section:
                aws_id = self.config.get(selection, 'aws_access_key_id')
                aws_key = self.config.get(selection, 'aws_secret_access_key')

        self.config.set('default', 'aws_access_key_id', aws_id)
        self.config.set('default', 'aws_access_key_id', aws_id)

        print "Using AWS config " + selection

        with open(self.creds_file, 'w') as configfile:
            self.config.write(configfile)


    def list_accounts(self):
        print "You have the following AWS accounts: "

        aws_id = self.config.get('default', 'aws_access_key_id')

        for section in self.config.sections():
            if section != 'default' \
                    and self.config.get(section, 'aws_access_key_id') == aws_id:
                print "\t{0}{1:19}{2}".format('*', section, self.config.get(section, 'aws_access_key_id'))
            else:
                print "\t{0:20}{1}".format(section, self.config.get(section, 'aws_access_key_id'))
        print


    def default_backup_exists(self):
        default_key_id = self.config.get('default', 'aws_access_key_id')
        for section in self.config.sections():
            if section != 'default' \
                    and default_key_id == self.config.get(section, 'aws_access_key_id'):
                return True
        return False

    
    def add_account(self):
        name = self.get_user_input("Enter profile name")
        for profile in self.config.sections():
            if profile == name:
                print "Profile name '" + profile + "' already exists"
                exit(1)
        aws_id = self.get_user_input("Enter your aws_access_key_id")
        aws_key = self.get_user_input("Enter your aws_secret_access_key")
    
        if aws_id == "" or aws_key == "":
            print "AWS Key or ID cannot be blank, account not added!"
            exit(1)

        if len(aws_id) != 21 and len(aws_key) != 41:
            print "Keys do not appear valid, exiting"
            exit(1)

        self.config.add_section(name)
        self.config.set(name, 'aws_access_key_id', aws_id)
        self.config.set(name, 'aws_secret_access_key', aws_key)

        with open(self.creds_file, 'w') as configfile:
            self.config.write(configfile)       

        exit(0)


    def backup_default(self):
        print "A backup of 'default' does not exist"
        section = self.get_user_input("Please enter a backup name for 'default': ")

        if section is "":
            print "Not backing up, exiting "
            exit(0)

        default_id  = self.config.get('default', 'aws_access_key_id')
        default_key = self.config.get('default', 'aws_secret_access_key')

        self.config.add_section(section)
        self.config.set(section, 'aws_access_key_id', default_id)
        self.config.set(section, 'aws_secret_access_key', default_key)

        with open(self.creds_file, 'w') as configfile:
            self.config.write(configfile)
