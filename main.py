from pprint import pprint

from config import config
from set_country import country
from src.airplane import Airplane
from src.api_client import APIAdapter
from src.create_bd import CreateDB
from src.dbmanager import BDManager
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

    params = config()
    file_save = json_saver.read_data()
    db = CreateDB("skypro3", params, file_save)
    db.to_create()
    db.save_result()
    print("База данных создана, данные записаны")

    filter_air = BDManager("skypro3", params)
    while True:
        answer_1 = input(
            "Введите цифру какие данные вывести:\n"
            "1 Средняя скорость всех самолетов\n"
            "2 Список самолетов выше средней\n"
            "3 Список всех самолетов\n"
            "4 Список самолетов и какой стране принадлежит в позывном которых содержатся интересующие символы\n"
            "5 Страна и количество самолетов в пределах ее территории\n"
            "6 Выход\n"
        )
        if answer_1 == "1":
            pprint(filter_air.get_avg_speed())
        elif answer_1 == "2":
            pprint(filter_air.get_aeroplanes_with_higher_speed())
        elif answer_1 == "3":
            pprint(filter_air.get_all_aeroplanes())
        elif answer_1 == "4":
            answer_symbol = input("Какие символы интересуют в позывном(пример позывного: CKS263)\n").upper()
            pprint(filter_air.get_aeroplanes_with_keyword(answer_symbol))
        elif answer_1 == "5":
            pprint(filter_air.get_countries_and_aeroplanes_count())
        elif answer_1 == "6":
            print("База с данными создана обращайтесь с новыми запросами")
            break
        else:
            print("Введите цифру от 1 до 6")


if __name__ == "__main__":
    main()
