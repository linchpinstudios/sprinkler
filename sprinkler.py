from Config import Config
from Collections.Collection import Collection
from Models.Sprinkler import Sprinkler

import time

class App(object):

    def __init__(self):
        self.sprinklers = Collection()
        self.bootstrap()

    def bootstrap(self):
        self.config = Config()

    def createSprinklers(self):
        sprinklers = self.config.get('Sprinklers')

        for sprinkler in sprinklers
            self.sprinklers.add( Sprinkler(sprinkler['name'], sprinkler['pin']) )

    def run(self):
        for sprinkler in self.sprinklers.items()
            sprinkler.start()
            time.sleep(5)
            sprinkler.stop()
            time.sleep(10)


app = App()
app.run()
