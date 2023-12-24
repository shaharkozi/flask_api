import os


class TestConfig:
    def __init__(self):
        self.ENV = "production"
        self.DEBUG = False
        self.PORT = 5000
        self.HOST = '0.0.0.0'
        self.TESTING = True
        self.CSV_FILE = os.path.join(os.getcwd(), "tests/player.csv")
