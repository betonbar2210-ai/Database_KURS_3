import psycopg2


class BDManager:
    """Класс фильтрации Базы данных SQL запросами"""

    def __init__(self, database_name: str, params: dict):
        self.database_name = database_name
        self.params = params

    def get_countries_and_aeroplanes_count(self):
        """получает список всех стран и количество самолетов в их воздушных пространствах"""
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute("""
                SELECT country, COUNT(DISTINCT callsign) as airplane_count
                FROM airplanes
                GROUP BY country
                """)
            total = cur.fetchall()
        conn.close()
        return total

    def get_all_aeroplanes(self):
        """получает список всех воздушных судов"""
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute("""
                SELECT country, callsign, origin_country, velocity, altitude
                FROM airplanes
                """)
            all_air = cur.fetchall()
        conn.close()
        return all_air

    def get_avg_speed(self):
        """получает среднюю скорость по самолетам."""
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute("""
        SELECT AVG(velocity)
        FROM airplanes
        """)
            avg_speed = cur.fetchone()[0]
        conn.close()
        return avg_speed

    def get_aeroplanes_with_higher_speed(self):
        """получает список всех самолетов, у которых скорость выше средней."""
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute("""
                SELECT country, callsign, origin_country, velocity, altitude,
                    (SELECT AVG(velocity) FROM airplanes) as avg_speed
                FROM airplanes
                WHERE velocity > (SELECT AVG(velocity) FROM airplanes)
                ORDER BY velocity
                """)
            total = cur.fetchall()
            result = []
            for i in total:
                result.append((i[0], i[1], i[2], float(i[3]), float(i[4])))
        conn.close()
        return result

    def get_aeroplanes_with_keyword(self, symbol):
        """Выводим список самолетов и страны регистрации, в позывном которых содержатся переданные в метод символы."""
        conn = psycopg2.connect(dbname=self.database_name, **self.params)
        with conn.cursor() as cur:
            cur.execute(
                """
                            SELECT callsign, origin_country
                            FROM airplanes
                            WHERE callsign LIKE %s
                        """,
                (f"{symbol}",),
            )

            result = cur.fetchall()
            return result
