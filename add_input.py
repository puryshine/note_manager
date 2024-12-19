from datetime import datetime
from datetime import date


title = input("Введите заголовок заметки:",)
content = input("Введите описание заметки:" )

# status_lib = {"а": 'Активный', "о": 'Отменен', "к": 'Крайне важный'}
# status_temp = input("Введите статус заметки буквой: А — Активный, О — Отменен, К — Крайне важный").lower()
# status_count = False
# while status_count == False:
#     if status_temp != "а" and status_temp != "о" and status_temp != "к":
#         status_temp = input("Введите статус заметки буквой: А — Активный, О — Отменен, К — Крайне важный").lower()
#     else:
#         status_count = True
# status=(status_lib[status_temp]) #защита от дурочка, чтобы один из трех всё-же выбрали и программа не улетала в ошибку
# функция статуса перенесена в модуль status_ для использования в final.py

created_date_temp = date.today()                # временное значение, что возвращает день создания заметки
created_date = created_date_temp                # константа, дабы дата не изменилась


issue_date_day = input("Введите день истечения заметки:")
issue_date_month = input("Введите месяц истечения заметки:")
issue_date_year = input("Введите год истечения заметки:")
while len(issue_date_year) < 4:
    issue_date_year = "0" + issue_date_year
issue_date_temp = issue_date_day + '-' + issue_date_month + '-' + issue_date_year
issue_date = datetime.strptime(issue_date_temp, '%d-%m-%Y')         #функция strptime переводит str в datetime

