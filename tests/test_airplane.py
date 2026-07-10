import pytest

from src.airplane import Airplane


def test_airplane_init(air_fly_1):
    assert air_fly_1.country == "Cuba"
    assert air_fly_1.callsign == "UPS496"
    assert air_fly_1.origin_country == "United States"
    assert air_fly_1.velocity == 194.9
    assert air_fly_1.altitude == 305.87


def test_callsign_no(air_fly_1):
    with pytest.raises(ValueError, match="Позывной должен быть непустой строкой"):
        Airplane("Cuba", "", "United States", 194.9, 305.87)


def test_country_no_raises(air_fly_1):
    with pytest.raises(ValueError, match="Страна регистрации должна быть непустой строкой"):
        Airplane("Cuba", "UPS496", "", 194.9, 305.87)


def test_velocity_no_raises(air_fly_1):
    with pytest.raises(ValueError, match="Скорость не может быть отрицательной"):
        Airplane("Cuba", "UPS496", "United States", -1, 305.87)


def test_altitude_no_raises(air_fly_1):
    with pytest.raises(ValueError, match="Высота не может быть отрицательной"):
        Airplane("Cuba", "UPS496", "United States", 194.9, -1010)


def test_airplane_to_dict_(air_fly_3):
    data = air_fly_3.to_dict()
    assert data == {
        "country": "Cuba",
        "altitude": 400,
        "callsign": "FRA50",
        "origin_country": "France",
        "velocity": 600,
    }


def test_cast_valid_open_sky_row(test_fly_2):
    planes = Airplane.cast_to_object_list(test_fly_2)
    assert len(planes) == 1
    p = planes[0]
    assert p.callsign == "N/A"
    assert p.origin_country == "United States"
    assert p.velocity == 804.3480000000001
    assert p.altitude == 11277.6
