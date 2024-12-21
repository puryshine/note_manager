# функциональность статуса на основе данных
import status_

def update_status(): # :) нет слов и идей. Всё что я пробовал, в finals не работает, тк импорт не перезаписывается
    while True:
        if request == 'да':
            status_lib = {"а": 'Активный', "о": 'Отменен', "з": 'Завершен'}
            status_temp = input("Введите статус заметки буквой: А — Активный, О — Отменен, З — Завершен").lower()

            while True:
                if status_temp != "а" and status_temp != "о" and status_temp != "з":
                    status_temp = input(
                        "Введите статус заметки буквой: А — Активный, О — Отменен, З — Завершен").lower()
                    status = (status_lib[status_temp])
                    return status
                    False
        elif request == 'нет':
            return


print("Желаете изменить статус заметки? Да/Нет") # не запускается. думаю
request = input().lower()
update_status(request)