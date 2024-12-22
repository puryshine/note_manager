status_lib = {"а": 'Активный', "о": 'Отменен', "з": 'Завершен'}
status_temp = 0
status_count = False
while status_count == False:
    if status_temp != "а" and status_temp != "о" and status_temp != "з":
        status_temp = input("Введите статус заметки буквой: А — Активный, О — Отменен, З — Завершен").lower()
        status_count = False
    else:
        status_count = True

status=(status_lib[status_temp]) #защита, чтобы один из трех вариантов всё-же выбрали и программа не улетала в ошибку

print(status)