from datetime import datetime
from datetime import date
def datechanger(_):
    return(_.day, _.month)            # Предоставление даты в формате: "день месяц"

test_date_day = input("Введите день:")
test_date_month = input("Введите месяц:")
test_date_year = input("Введите год:")           # Ввод года нужен для создания даты
while len(test_date_year) < 4:
    test_date_year = "0" + test_date_year
test_date_temp = test_date_day + '-' + test_date_month + '-' + test_date_year
test_date = datetime.strptime(test_date_temp, '%d-%m-%Y')         # Функция strptime переводит str в datetime

print(*datechanger(test_date))