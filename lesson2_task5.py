def month_to_season(month):
    season1 = [3, 4, 5]
    season2 = [6, 7, 8]
    season3 = [9, 10, 11]
    if month in season1: print("Весна")
    elif month in season2: print("Лето")
    elif month in season3: print("Осень")
    else: print("Зима")
month_to_season(input("Введите порядковый номер месяца:"))
