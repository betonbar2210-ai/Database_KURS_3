from typing import Any

import psycopg2


class CreateDB:
    """Создание базы данных и таблиц и сохранение данных о странах и самолетах."""

    def __init__(self, database_name: str, params: dict, data: list[dict[str, Any]]):
        self.database_name = database_name
        self.params = params
        self.data = data

    def to_create(self):
        """Создаем базу данных"""
        conn = psycopg2.connect(dbname="postgres", **self.params)
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(f"DROP DATABASE IF EXISTS {self.database_name}")
        cur.execute(f"CREATE DATABASE {self.database_name}")

        cur.close()
        conn.close()

        conn = psycopg2.connect(dbname=self.database_name, **self.params)

        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE airplanes(
                    country VARCHAR(20) NOT NULL,
                    callsign VARCHAR(10) NOT NULL,
                    origin_country VARCHAR(50) NOT NULL,
                    velocity DECIMAL NOT NULL,
                    altitude REAL NOT NULL
                )
            """)

        conn.commit()
        conn.close()

    def save_result(self):
        """Записываем данные в базу данных"""
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            for airplane in self.data:
                cur.execute(
                    """
                    INSERT INTO airplanes(country, callsign, origin_country, velocity, altitude)
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING *
                    """,
                    (
                        airplane["country"],
                        airplane["callsign"],
                        airplane["origin_country"],
                        airplane["velocity"],
                        airplane["altitude"],
                    ),
                )
        conn.commit()
        conn.close()
