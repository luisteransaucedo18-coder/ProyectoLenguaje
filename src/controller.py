from flask import Flask, render_template, request
from dotenv import load_dotenv

from src.data import GAMES, OPTIONS
from src.database import MySQLGameRepository
from src.logic_rules import infer_recommended_game_ids, load_facts
from src.processor import build_explanation, normalize_preferences, rank_games


class GameRecommendationController:
    def __init__(self):
        load_dotenv()
        self.repository = MySQLGameRepository()
        self.database_connected = self.repository.initialize()
        self.games = self.repository.get_all_games() if self.database_connected else GAMES
        self.database_status = self.repository.status()
        self.options = OPTIONS
        load_facts(self.games)

    def create_app(self):
        app = Flask(
            __name__,
            template_folder="../templates",
            static_folder="../static",
        )

        @app.get("/")
        def index():
            return render_template(
                "index.html",
                options=self.options,
                games=self.games,
                preferences={},
                recommendations=[],
                selected_game=None,
                database_status=self.database_status,
            )

        @app.post("/recommend")
        def recommend():
            preferences = normalize_preferences(request.form)
            logical_matches = infer_recommended_game_ids(preferences)
            recommendations = rank_games(self.games, preferences, logical_matches)
            selected_game = recommendations[0] if recommendations else None

            if selected_game:
                selected_game = {
                    **selected_game,
                    "explanation": build_explanation(selected_game, preferences),
                }

            return render_template(
                "index.html",
                options=self.options,
                games=self.games,
                preferences=preferences,
                recommendations=recommendations,
                selected_game=selected_game,
                database_status=self.database_status,
            )

        return app
