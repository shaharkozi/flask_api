import json
import os
import unittest

from app import create_app
from src.config.config import get_config_by_env


class TestApi(unittest.TestCase):
    def setUp(self) -> None:
        os.environ["ENV"] = "test"
        config = get_config_by_env(os.environ["ENV"])
        application = create_app()
        application.config.from_object(config)
        self.app = application.test_client()

    def test_get_players(self) -> None:
        response = self.app.get("/players")
        players_list = json.loads(response.data)
        self.assertEqual(len(players_list), 3)
        self.assertEqual(response.status_code, 200)

    def test_get_player(self) -> None:
        response = self.app.get("/player/aardsda01")
        player = json.loads(response.data)
        self.assertEqual(player["birthYear"], 1981)
        self.assertEqual(response.status_code, 200)

    def test_get_player_not_found(self) -> None:
        response = self.app.get("/player/test_not_exist")
        player = json.loads(response.data)
        self.assertEqual(player["msg"], "player not found")
        self.assertEqual(response.status_code, 404)

    def test_get_incorrect_path(self) -> None:
        response = self.app.get("/test_path_not_exist")
        self.assertEqual(response.status_code, 404)
