from pprint import pprint

import requests


class APIAdapter:
    """Получение координат стран и вывод данных по самолетам в их воздушном пространстве"""

    NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
    OPENSKY_URL = "https://opensky-network.org/api/states/all"

    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Gluyki/1.0 betonbar@bk.ru"})

    def get_country_coordinates(self, country_list: list):
        """Получение координат с сайта https://nominatim.openstreetmap.org"""
        country_coordinates = []
        for country in country_list:
            params = {"q": country, "format": "json", "limit": 1}
            try:
                response = self.session.get(self.NOMINATIM_URL, params=params, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if not data:
                        raise Exception(f"Страна '{country}' не найдена в Nominatim")

                    if "boundingbox" not in data[0]:
                        raise Exception("Boundingbox отсутствует в ответе API")

                    bbox = data[0]["boundingbox"]
                    if len(bbox) != 4:
                        raise Exception("Неверный формат boundingbox")

                    bbox_save = {
                        country: {
                            "south": float(bbox[0]),
                            "north": float(bbox[1]),
                            "west": float(bbox[2]),
                            "east": float(bbox[3]),
                        }
                    }
                    country_coordinates.append(bbox_save)
                else:
                    raise Exception(f"Ошибка API Nominatim: {response.status_code}")
            except requests.exceptions.Timeout:
                raise Exception("Таймаут при запросе к Nominatim")
            except Exception as e:
                raise Exception(f"Ошибка при запросе к Nominatim: {str(e)}")
        return country_coordinates

    def get_airplanes_in_area(self, coords_list: list[dict]) -> list[list[list]]:
        """Получает список словарей с координатами стран
        возвращает список с данными о самолетах с сайта https://opensky-network.org"""

        new_airplane_list = []
        for coor in coords_list:
            for key, value in coor.items():
                params = {
                    "lamin": value["south"],
                    "lamax": value["north"],
                    "lomin": value["west"],
                    "lomax": value["east"],
                }
            try:
                response = self.session.get(self.OPENSKY_URL, params=params, timeout=15)
                if response.status_code == 200:
                    data = response.json()
                    total = data.get("states", []) if data else []
                    f = {key: total}
                    new_airplane_list.append(f)
                else:
                    raise Exception(f"Ошибка API OpenSky: {response.status_code}")
            except requests.exceptions.Timeout:
                raise Exception("Таймаут при запросе к OpenSky")
            except Exception as e:
                raise Exception(f"Ошибка при запросе к OpenSky: {str(e)}")
        return new_airplane_list
