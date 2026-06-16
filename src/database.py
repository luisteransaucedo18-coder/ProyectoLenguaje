import os

from supabase import Client, create_client

from src.data import GAMES


LOCAL_IMAGES_BY_GAME_ID = {game["id"]: game["image"] for game in GAMES}


class SupabaseGameRepository:
    def __init__(self):
        self.url = os.getenv("NEXT_PUBLIC_SUPABASE_URL") or os.getenv("SUPABASE_URL", "")
        self.key = (
            os.getenv("NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY")
            or os.getenv("SUPABASE_PUBLISHABLE_KEY", "")
        )
        self.client: Client | None = None
        self.last_error = None

    def initialize(self):
        if not self.url or not self.key:
            self.last_error = "faltan NEXT_PUBLIC_SUPABASE_URL o NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY"
            return False

        try:
            self.client = create_client(self.url, self.key)
            self.client.table("games").select("id").limit(1).execute()
            self.last_error = None
            return True
        except Exception as exc:
            self.last_error = str(exc)
            self.client = None
            return False

    def get_all_games(self):
        if not self.client:
            return GAMES

        try:
            response = (
                self.client.table("games")
                .select("id,name,genre,platform,mode,difficulty,duration,mood,image,tags")
                .order("name")
                .execute()
            )
            return [
                {
                    **game,
                    "image": LOCAL_IMAGES_BY_GAME_ID.get(game["id"], game.get("image", "")),
                }
                for game in response.data
            ] or GAMES
        except Exception as exc:
            self.last_error = str(exc)
            return GAMES

    def status(self):
        if self.last_error:
            return {
                "connected": False,
                "message": f"Supabase no conectado: {self.last_error}",
            }

        return {
            "connected": True,
            "message": "Conectado a Supabase PostgreSQL",
        }
