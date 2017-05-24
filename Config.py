import yaml

class Config(object):

    def __init__(self, configFile = 'config.yaml'):
        self.configFile = configFile
        self.load()

    def load(self):
        with open(self.configFile, 'r') as configYAML:
            self.config = yaml.load( configYAML )

    def get(self, key):
        return self.config[key]

    def set(self, key, value):
        self.config[key] = value
        return 1
