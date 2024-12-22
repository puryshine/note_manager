from datetime import datetime, timedelta
from add_input import issue_date  # импортирую из add_input чтобы не создавать "фаил - костыль" без тестовых input'ов


def check_deadline(issue_date):
    print(f'Текущая дата: {datetime.today().day}-{datetime.today().month}-{datetime.today().year}')
    if datetime.today() < issue_date:  # если дедлайн позже текущей даты
        deltatime = issue_date - datetime.today()  # вычисляется разность дат
        if deltatime < timedelta(days=1):
            return print("Дедлайн истёк сегодня :(")  # если разность меньше суток, то выводится это сообщение
        return print("Дедлайн истёк", deltatime.days, "дней назад!")
    else:
        deltatime = datetime.today() - issue_date  # если дедлайн раньше текущей даты
        if deltatime < timedelta(days=1):
            return print("Дедлайн сегодня!!!")  # если до дедлайна осталось меньше суток, то выводится это сообщение
        return print("Дедлайн истекает через", deltatime.days, "дней")


check_deadline(issue_date)

# issue_date = datetime.strptime('20-12-2024', '%d-%m-%Y')

check_deadline(issue_date)
