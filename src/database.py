import json
import os

import mysql.connector
from mysql.connector import Error

from src.data import GAMES


class MySQLGameRepository:
    def __init__(self):
        self.host = os.getenv("MYSQL_HOST", "localhost")
        self.port = int(os.getenv("MYSQL_PORT", "3306"))
        self.user = os.getenv("MYSQL_USER", "root")
        self.password = os.getenv("MYSQL_PASSWORD", "")
        self.database = os.getenv("MYSQL_DATABASE", "gamematch")
        self.last_error = None

    def _connect(self, include_database=True):
        config = {
            "host": self.host,
            "port": self.port,
            "user": self.user,
            "password": self.password,
        }

        if include_database:
            config["database"] = self.database

        return mysql.connector.connect(**config)

    def initialize(self):
        try:
            self._create_database()
            self._create_table()
            self._seed_games()
            self.last_error = None
            return True
        except Error as exc:
            self.last_error = str(exc)
            return False

    def _create_database(self):
        with self._connect(include_database=False) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"CREATE DATABASE IF NOT EXISTS `{self.database}` "
                    "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
                )

    def _create_table(self):
        with self._connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS games (
                        id VARCHAR(80) PRIMARY KEY,
                        name VARCHAR(160) NOT NULL,
                        genre VARCHAR(60) NOT NULL,
                        platform VARCHAR(60) NOT NULL,
                        mode VARCHAR(60) NOT NULL,
                        difficulty VARCHAR(60) NOT NULL,
                        duration VARCHAR(60) NOT NULL,
                        mood VARCHAR(60) NOT NULL,
                        image TEXT NOT NULL,
                        tags JSON NOT NULL
                    )
                    """
                )
            connection.commit()

    def _seed_games(self):
        with self._connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM games")
                total_games = cursor.fetchone()[0]

                if total_games > 0:
                    return

                cursor.executemany(
                    """
                    INSERT INTO games (
                        id, name, genre, platform, mode, difficulty,
                        duration, mood, image, tags
                    )
                    VALUES (
                        %(id)s, %(name)s, %(genre)s, %(platform)s, %(mode)s,
                        %(difficulty)s, %(duration)s, %(mood)s, %(image)s, %(tags)s
                    )
                    """,
                    [
                        {
                            **game,
                            "tags": json.dumps(game["tags"], ensure_ascii=True),
                        }
                        for game in GAMES
                    ],
                )
            connection.commit()

    def get_all_games(self):
        with self._connect() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(
                    """
                    SELECT id, name, genre, platform, mode, difficulty,
                           duration, mood, image, tags
                    FROM games
                    ORDER BY name
                    """
                )
                rows = cursor.fetchall()

        return [
            {
                **row,
                "tags": json.loads(row["tags"]) if isinstance(row["tags"], str) else row["tags"],
            }
            for row in rows
        ]

    def status(self):
        if self.last_error:
            return {
                "connected": False,
                "message": f"MySQL no conectado: {self.last_error}",
            }

        return {
            "connected": True,
            "message": f"Conectado a MySQL: {self.database}",
        }
