from config import config
from src import api_client
from src.airplane import Airplane
from src.api_client import APIAdapter
from src.utils import JSONSaver


def main():
    data = APIAdapter()
    json_saver = JSONSaver()
    coords = data.get_country_coordinates(['Canada'])
    for country_data in coords:
        # Получаем координаты из словаря
        airplanes_data = APIAdapter.get_airplanes_in_area(
            south=country_data["south"],
            north=country_data["north"],
            west=country_data["west"],
            east=country_data["east"]
        )
    # airplanes = Airplane.cast_to_object_list(airplanes_data)
    #
    # for airplane in airplanes:
    #     json_saver.add_airplane(airplane)
    #
    # print(f"\nПолучено и сохранено {len(airplanes)} самолётов")
        print(country_data)




if __name__ == '__main__':
    main()