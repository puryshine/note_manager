status_lib = {"а": 'Активный', "о": 'Отменен', "з": 'Завершен'}
status_temp = 0
status_count = False
while status_temp not in ["а", "о", "з"]:
    status_temp = input("Введите статус заметки буквой: А — Активный, О — Отменен, З — Завершен").lower()
status = status_lib[status_temp]

print(status)
