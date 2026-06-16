from src.controller import GameRecommendationController


app = GameRecommendationController().create_app()


if __name__ == "__main__":
    app.run(debug=True)
