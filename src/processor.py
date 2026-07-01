from functools import reduce

#Esta función transforma los datos del formulario en un diccionario limpio.
def normalize_preferences(form_data):
    return {
        "genre": form_data.get("genre", ""),
        "platform": form_data.get("platform", ""),
        "mode": form_data.get("mode", ""),
        "difficulty": form_data.get("difficulty", ""),
        "duration": form_data.get("duration", ""),
        "mood": form_data.get("mood", ""),
    }


def score_game(game, preferences, logical_bonus=0):
    weights = {
        "genre": 3,
        "platform": 2,
        "mode": 2,
        "difficulty": 1,
        "duration": 1,
        "mood": 3,
    }
    #calcula el puntaje base
    base_score = reduce(
        lambda total, item: total + (item[1] if preferences.get(item[0]) == game.get(item[0]) else 0),
        weights.items(),
        0,
    )

    mode_bonus = 1 if preferences.get("mode") and game.get("mode") == "ambos" else 0
    return base_score + mode_bonus + logical_bonus

#Primero transforma cada juego agregándole puntaje, luego filtra los que no sirven, y finalmente los ordena de mayor a menor compatibilidad.
def rank_games(games, preferences, logical_matches):
    logical_ids = set(logical_matches)

    scored_games = map(
        lambda game: {
            **game,
            "score": score_game(game, preferences, 3 if game["id"] in logical_ids else 0),
            "logical_match": game["id"] in logical_ids,
        },
        games,
    )

    useful_games = filter(lambda game: game["score"] > 0, scored_games)
    return sorted(useful_games, key=lambda game: game["score"], reverse=True)


def build_explanation(game, preferences):
    matched_fields = list(
        filter(
            lambda field: preferences.get(field) and preferences[field] == game.get(field),
            ["genre", "platform", "mode", "difficulty", "duration", "mood"],
        )
    )

    labels = {
        "genre": "genero",
        "platform": "plataforma",
        "mode": "modo",
        "difficulty": "dificultad",
        "duration": "duracion",
        "mood": "estado de animo",
    }

    if not matched_fields:
        return "Es la opcion con mejor compatibilidad general dentro de la base de conocimiento."

    readable = ", ".join(map(lambda field: labels[field], matched_fields))
    return f"Coincide con tus preferencias de {readable}."
