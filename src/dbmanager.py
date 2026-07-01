import psycopg2

params = config()
class BDManager():
    def get_countries_and_aeroplanes_count(self):
        """получает список всех стран и количество самолетов в их воздушных пространствах"""
        pass

    def get_all_aeroplanes(self):
        """получает список всех воздушных судов"""
        pass

    def get_avg_speed(self):
        """получает среднюю скорость по самолетам."""
        pass

    def get_aeroplanes_with_higher_speed(self):
        """ получает список всех самолетов, у которых скорость выше средней."""
        pass

    def get_aeroplanes_with_keyword(self):
        """получает список всех самолетов, в позывном которых содержатся переданные в метод символы."""