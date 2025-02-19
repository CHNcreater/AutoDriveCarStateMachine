import configparser
import os

class Configuration():
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.path.dirname(__file__), 'conf/config.ini'))

    def get(self, section, key):
        return self.config.get(section, key)
    
#Example
if __name__ == '__main__':
    config = Configuration()
    print(config.get("camera", "server_url"))