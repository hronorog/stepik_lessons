from itertools import combinations_with_replacement


def make_option_list():
    check_list = ("работа с явными и неявными ожиданиями",
                  "как получать значения атрибутов html-элементов",
                  "работа с выпадающими списками",
                  "настройка запуска определенного набора тестов",
                  "работа с отчётами для упавших автотестов",
                  "переключение между окнами браузера")

    for x in (3, 4, 5):
        for i in combinations_with_replacement(check_list, x):
            if len(set(i)) > 2:
                print(i)
                for y in i:
                    print(y)


make_option_list()
