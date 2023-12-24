import os


class DevConfig:
    def __init__(self):
        self.ENV = "development"
        self.DEBUG = True
        self.PORT = 5000
        self.HOST = '0.0.0.0'
        self.TESTING = False
        self.CSV_FILE = os.path.join(os.getcwd(), "player.csv")
