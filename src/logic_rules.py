from pyDatalog import pyDatalog


_loaded_games = []


def load_facts(games):
    global _loaded_games
    _loaded_games = list(games)
    _configure_logic(_loaded_games)


def _configure_logic(games):
    global Juego
    global es_genero, tiene_dificultad, tiene_duracion, provoca_animo, tiene_modo
    global recomendado_para_relajarse, recomendado_para_reto, recomendado_para_social, recomendado_por_preferencia

    pyDatalog.Logic()
    pyDatalog.create_terms("Juego, Genero, Dificultad, Duracion, Animo, Modo")
    pyDatalog.create_terms("es_genero, tiene_dificultad, tiene_duracion, provoca_animo, tiene_modo")
    pyDatalog.create_terms("recomendado_para_relajarse, recomendado_para_reto, recomendado_para_social, recomendado_por_preferencia")
    local_terms = locals()
    Juego = local_terms["Juego"]
    es_genero = local_terms["es_genero"]
    tiene_dificultad = local_terms["tiene_dificultad"]
    tiene_duracion = local_terms["tiene_duracion"]
    provoca_animo = local_terms["provoca_animo"]
    tiene_modo = local_terms["tiene_modo"]
    recomendado_para_relajarse = local_terms["recomendado_para_relajarse"]
    recomendado_para_reto = local_terms["recomendado_para_reto"]
    recomendado_para_social = local_terms["recomendado_para_social"]
    recomendado_por_preferencia = local_terms["recomendado_por_preferencia"]

    recomendado_para_relajarse(Juego) <= (
        provoca_animo(Juego, "relajarse")
        & tiene_dificultad(Juego, "baja")
    )

    recomendado_para_reto(Juego) <= (
        provoca_animo(Juego, "reto")
        & tiene_dificultad(Juego, "alta")
    )

    recomendado_para_social(Juego) <= (
        tiene_modo(Juego, "multiplayer")
        & tiene_duracion(Juego, "corta")
    )

    recomendado_para_social(Juego) <= (
        tiene_modo(Juego, "ambos")
        & tiene_duracion(Juego, "corta")
    )

    recomendado_por_preferencia(Juego, "relajarse") <= recomendado_para_relajarse(Juego)
    recomendado_por_preferencia(Juego, "reto") <= recomendado_para_reto(Juego)
    recomendado_por_preferencia(Juego, "competir") <= recomendado_para_social(Juego)
    recomendado_por_preferencia(Juego, "divertirse") <= recomendado_para_social(Juego)

    for game in games:
        +es_genero(game["id"], game["genre"])
        +tiene_dificultad(game["id"], game["difficulty"])
        +tiene_duracion(game["id"], game["duration"])
        +provoca_animo(game["id"], game["mood"])
        +tiene_modo(game["id"], game["mode"])


def infer_recommended_game_ids(preferences):
    mood = preferences.get("mood")
    if not mood:
        return []

    _configure_logic(_loaded_games)
    query_result = recomendado_por_preferencia(Juego, mood)
    if not query_result:
        return []

    return [str(row[0]) for row in query_result]
