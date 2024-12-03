import configparser
import os

# Use relative path
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)


class ReadConfig:
    @staticmethod
    def get_value(key):
        """Retrieve value from config file."""
        return config.get('common info', key)

    @staticmethod
    def get_application_url():
        return ReadConfig.get_value('baseUrl')

    @staticmethod
    def get_user_email():
        return ReadConfig.get_value('username')

    @staticmethod
    def get_user_password():
        return ReadConfig.get_value('password')

    @staticmethod
    def get_invalid_user_email():
        return ReadConfig.get_value('email')

    @staticmethod
    def get_invalid_password():
        return ReadConfig.get_value('userpassword')

    @staticmethod
    def get_project_name():
        return ReadConfig.get_value('projectname')

    @staticmethod
    def get_first_name():
        return ReadConfig.get_value('firstname')

    @staticmethod
    def get_last_name():
        return ReadConfig.get_value('lastname')

    @staticmethod
    def get_email():
        return ReadConfig.get_value('email')

    @staticmethod
    def get_new_user_password():
        return ReadConfig.get_value('userpassword')
