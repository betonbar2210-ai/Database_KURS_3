from config import config
from set_country import country
from src import api_client
from src.airplane import Airplane
from src.api_client import APIAdapter
from src.utils import JSONSaver


def main():
    data = APIAdapter()
    json_saver = JSONSaver()
    json_saver.clear_all()
    coords = data.get_country_coordinates(country)
    airplane_country = data.get_airplanes_in_area(coords)
    airplan = Airplane.cast_to_object_list(airplane_country)

    for air in airplan:
        json_saver.add_airplane(air)


if __name__ == '__main__':
    main()