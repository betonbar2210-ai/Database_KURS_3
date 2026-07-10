answer_country = input("Введите интересующие страны через запятую\n")
country_list = answer_country.split(',')
country = [item.strip().capitalize() for item in country_list]

