from datetime import datetime
from statuses_lib import statuses
from datetime import date


title = input("Введите заголовок заметки:",)
content = input("Введите описание заметки:" )

status_temp = input("Введите статус заметки буквой: А — Активный, О — Отменен, К — Крайне важный").lower()
status_count = False
while status_count == False:
    if status_temp != "а" and status_temp != "о" and status_temp != "к":
        status_temp = input("Введите статус заметки буквой: А — Активный, О — Отменен, К — Крайне важный").lower()
    else:
        status_count = True
status = statuses[status_temp] #защита от дурочка, чтобы один из трех всё-же выбрали и программа не улетала в ошибку


created_date_temp = date.today()                # временное значение, что возвращает день создания заметки
created_date = created_date_temp                # константа, дабы дата не изменилась


issue_date_day = input("Введите день истечения заметки:")
issue_date_month = input("Введите месяц истечения заметки:")
issue_date_year = input("Введите год истечения заметки:")
while len(issue_date_year) < 4:
    issue_date_year = "0" + issue_date_year
issue_date_temp = issue_date_day + '-' + issue_date_month + '-' + issue_date_year
issue_date = datetime.strptime(issue_date_temp, '%d-%m-%Y')         #функция strptime переводит str в datetime

print(issue_date_temp)
print(issue_date)
# print(created_date.day, created_date.month, created_date.year, sep='-')
# print(status)