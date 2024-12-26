import configparser
import os

class Configuration():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.path.dirname(__file__), 'conf/config.ini'))

    def get(self, section, key):
        return self.config.get(section, key)
    
#Example
config = Configuration()
print(config.get("camera", "server_url"))