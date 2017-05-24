from Config import Config
from Collections.Collection import Collection
from Models.Sprinkler import Sprinkler

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
