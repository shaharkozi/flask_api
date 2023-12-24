from src.config.test_config import TestConfig
from src.config.dev_config import DevConfig
from src.config.prod_config import ProdConfig


class Config:
    def __init__(self):
        self.dev_conf = DevConfig()
        self.test_conf = TestConfig()
        self.prod_conf = ProdConfig()


def get_config_by_env(env):
    config = Config()
    if env == "test":
        return config.test_conf
    elif env == "dev":
        return config.dev_conf

    return config.prod_conf
