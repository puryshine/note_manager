# функциональность статуса на основе данных
import status_



# def update_status(
#         request):  # :) нет слов и идей. Всё что я пробовал, в finals не работает, тк импорт не перезаписывается
#     if request == 'да':
#         status_temp = input("Введите статус заметки буквой: А — Активный, О — Отменен, З — Завершен").lower()
#         status_count = False
#         while status_count == False:
#             if status_temp != "а" and status_temp != "о" and status_temp != "з":
#                 status_temp = input(
#                     "Введите статус заметки буквой: А — Активный, О — Отменен, З — Завершен"
#                     ).lower()
#             if status_temp == "а" and status_temp == "о" and status_temp == "з":
#                 status_count = True
#     else:
#         break
#     return status_temp


def update_status(
        request):
    if request == 'да':
        status_temp = input("Введите статус заметки буквой: А — Активный, О — Отменен, З — Завершен").lower()
        while True:
            if status_temp != "а" and status_temp != "о" and status_temp != "з":
                status_temp = input(
                    "Введите статус заметки буквой: А — Активный, О — Отменен, З — Завершен"
                ).lower()
            else:
                break

    return status_temp

print("Желаете изменить статус заметки? Да/Нет")
status_lib = {"а": 'Активный', "о": 'Отменен', "з": 'Завершен'}
request = input().lower()

status = (status_lib[update_status(request)])
print(status)
