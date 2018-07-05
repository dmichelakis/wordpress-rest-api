import os
import configparser


class Configuration:

    def __init__(self):
        self.file_path = os.path.basename('production.ini')

    def get_configuration_for(self, section, option):

        config = configparser.ConfigParser()
        config.read(self.file_path)

        return config.get(section, option)