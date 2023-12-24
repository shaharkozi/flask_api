from flask_restful import Resource, reqparse
import pandas as pd
import os

from src.config.config import get_config_by_env

player_args_parser = reqparse.RequestParser()
player_args_parser.add_argument("playerID", location="view_args", type=str, help="the player id")


class Player(Resource):
    def get(self, playerID) -> tuple:
        """
        GET player handler

        :param playerID:str
        :return: tuple
        """
        args = player_args_parser.parse_args()
        df = pd.read_csv(get_config_by_env(os.getenv("ENV")).CSV_FILE)
        player = df[df["playerID"] == args["playerID"]]

        if player.empty:
            return {"msg": "player not found"}, 404

        return player.iloc[0].to_dict(), 200

