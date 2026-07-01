import shutil
import tempfile

import pytest


from src.airplane import Airplane
from src.api_client import APIAdapter
from src.utils import JSONSaver


@pytest.fixture
def saver_with_temp_dir(monkeypatch):
    tmp_dir = tempfile.mkdtemp()
    monkeypatch.setattr("src.utils.ROOT_DIR", tmp_dir)
    try:
        yield JSONSaver(filename="test_airplanes.json")
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


@pytest.fixture
def in_area_list():
    return [{'Cuba': {'east': -73.9190004,
           'north': 23.4816972,
           'south': 19.6275294,
           'west': -85.1679702}}]


@pytest.fixture
def test_fly_1():
    return [['ac67fc',
            '',
            'United States',
            1782928012,
            1782928012,
            -83.3326,
            23.3714,
            11277.6,
            False,
            223.43,
            49.86,
            0,
            None,
            11940.54,
            None,
            False,
            0]]


@pytest.fixture
def test_fly_2():
    return [{'Cuba': [['ac67fc',
                '',
                'United States',
                1782928012,
                1782928012,
                -83.3326,
                23.3714,
                11277.6,
                False,
                223.43,
                49.86,
                0,
                None,
                11940.54,
                None,
                False,
                0]]}]

@pytest.fixture
def adapter():
    return APIAdapter()


@pytest.fixture
def air_fly_1():
    return Airplane(
        country="Cuba", callsign="UPS496", origin_country="United States", velocity=194.9, altitude=305.87
    )


@pytest.fixture
def air_fly_2():
    return Airplane(callsign="RUS12", origin_country="Russia", velocity=600, altitude=1000)


@pytest.fixture
def air_fly_3():
    return Airplane(country="Cuba", callsign="FRA50", origin_country="France", velocity=600, altitude=400)
