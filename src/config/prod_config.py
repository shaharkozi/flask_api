import os


class ProdConfig:
    def __init__(self):
        self.ENV = "production"
        self.DEBUG = False
        self.PORT = 80
        self.HOST = '0.0.0.0'
        self.TESTING = False
        self.CSV_FILE = os.path.join(os.getcwd(), "player.csv")
