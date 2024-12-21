status_lib = {"а": 'Активный', "о": 'Отменен', "з": 'Завершен'}
status_temp = input("Введите статус заметки буквой: А — Активный, О — Отменен, З — Завершен").lower()

while True:
    if status_temp != "а" and status_temp != "о" and status_temp != "з":
        status_temp = input("Введите статус заметки буквой: А — Активный, О — Отменен, З — Завершен").lower()
    else:
        False
status=(status_lib[status_temp]) #защита, чтобы один из трех вариантов всё-же выбрали и программа не улетала в ошибку