from set_country import country


class Airplane:
    """Принимает список от APIAdapter и возвращает словарь в нужном формате"""

    def __init__(self, country: str , callsign: str, origin_country: str, velocity: float, altitude: float) -> None:
        self.validate_data(callsign, origin_country, velocity, altitude)
        self.country = country
        self.callsign = callsign.strip()
        self.origin_country = origin_country.strip()
        self.velocity = velocity
        self.altitude = altitude

    def validate_data(self, callsign, origin_country, velocity, altitude):
        """Проверяем на соответсвие необходимых данных"""
        if not callsign or not isinstance(callsign, str):
            raise ValueError("Позывной должен быть непустой строкой")
        if not origin_country or not isinstance(origin_country, str):
            raise ValueError("Страна регистрации должна быть непустой строкой")
        if velocity < 0:
            raise ValueError("Скорость не может быть отрицательной")
        if altitude < 0:
            raise ValueError("Высота не может быть отрицательной")

    @classmethod
    def cast_to_object_list(cls, data: list[dict[list[list]]]):
        """Формируем список с необходимыми данными"""
        airplanes = []
        for item in data:
            for key, value in item.items():
                for i in value:
                    try:
                        country = key
                        callsign = i[1] or "N/A"
                        origin_country = i[2] or "Unknown"
                        velocity = float(i[9]) * 3.6 if i[9] else 0
                        altitude = float(i[7]) if i[7] else 0

                        airplanes.append(cls(country, callsign, origin_country, velocity, altitude))
                    except (ValueError, IndexError, TypeError):
                        continue
        return airplanes

    def to_dict(self):
        """Возвращаем словарем"""
        return {"country": self.country,
            "callsign": self.callsign,
            "origin_country": self.origin_country,
            "velocity": self.velocity,
            "altitude": self.altitude,
        }
