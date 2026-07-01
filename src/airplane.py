class Airplane:
    def __init__(self, callsign: str, origin_country: str, velocity: float, altitude: float) -> None:
        self.validate_data(callsign, origin_country, velocity, altitude)
        self.callsign = callsign.strip()
        self.origin_country = origin_country.strip()
        self.velocity = velocity
        self.altitude = altitude

    def validate_data(self, callsign, origin_country, velocity, altitude):
        if not callsign or not isinstance(callsign, str):
            raise ValueError("Позывной должен быть непустой строкой")
        if not origin_country or not isinstance(origin_country, str):
            raise ValueError("Страна регистрации должна быть непустой строкой")
        if velocity < 0:
            raise ValueError("Скорость не может быть отрицательной")
        if altitude < 0:
            raise ValueError("Высота не может быть отрицательной")

    @classmethod
    def cast_to_object_list(cls, data):
        airplanes = []
        for item in data:
            for i in item:
                try:
                    callsign = i[1] or "N/A"
                    origin_country = i[2] or "Unknown"
                    velocity = float(i[9]) * 3.6 if i[9] else 0
                    altitude = float(i[7]) if i[7] else 0

                    airplanes.append(cls(callsign, origin_country, velocity, altitude))
                except (ValueError, IndexError, TypeError):
                    continue
        return airplanes

    def to_dict(self):
        return {
            "callsign": self.callsign,
            "origin_country": self.origin_country,
            "velocity": self.velocity,
            "altitude": self.altitude,
        }
