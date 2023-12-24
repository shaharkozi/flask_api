from flask import Flask
from flask_restful import Api
import os

from src.resources.player import Player
from src.resources.players import Players
from src.config.config import get_config_by_env


def create_app() -> Flask:
    """
    function which uses as app creator

    :return: Flask application
    """
    app = Flask(__name__)

    api = Api(app)

    api.add_resource(Player, "/player/<string:playerID>")
    api.add_resource(Players, "/players")

    return app


if __name__ == "__main__":
    os.environ["ENV"] = "prod"
    config = get_config_by_env(os.getenv("ENV"))
    application = create_app()
    application.config.from_object(config)
    application.run(port=config.PORT, host=config.HOST, debug=config.DEBUG)
