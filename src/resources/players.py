from flask_restful import Resource
import pandas as pd
import os

from src.config.config import get_config_by_env


class Players(Resource):
    def get(self) -> tuple:
        """
        GET players handler

        :return: tuple
        """
        df = pd.read_csv(get_config_by_env(os.getenv("ENV")).CSV_FILE)
        return df.to_dict("records"), 200
