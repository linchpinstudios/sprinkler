from 'Config.py' import Config
from 'Collections/Collection.py' import Collection
from 'Models/Sprinkler.py' import Sprinkler

import CHIP_IO.GPIO as GPIO
import time

class App(object):

    def __init__(self):
        self.bootstrap()

    def bootstrap(self):
        self.config = Config()

    def createSprinklers(self):
        self.sprinklers = Collection()

        for sprinkler in self.config.get('Sprinklers')
            self.sprinklers.add( Sprinkler(sprinkler['name'], sprinkler['pin']) )

    def run(self):
        for sprinkler in self.sprinklers.items()
            sprinkler.start()
            time.sleep(5)
            sprinkler.stop()
            time.sleep(10)


app = App()
app.run()
