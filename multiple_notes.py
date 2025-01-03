from datetime import datetime

status_lib = {"а": 'Активный', "о": 'Отменен', "з": 'Завершен'}
notes = []

while True:

    title = input("Введите название заметки")
    heads = (input('Введите первый заголовок'), input('Введите второй заголовок'), input('Введите третий заголовок'))
    # в прошлых заданиях количество заголовков было не менее трех
    content = input("Введите содержание заметки")
    status_temp = 0
    while status_temp not in ["а", "о", "з"]:
        status_temp = input("Введите статус заметки буквой: А — Активный, О — Отменен, З — Завершен").lower()
    status = status_lib[status_temp]
    while True:
        try:
            created_date = datetime.strptime(input("Введите дату создания в формате ДД-ММ-ГГГГ"), '%d-%m-%Y')
            break
        except ValueError:
            print("Неверный формат даты, попробуйте ещё раз")

    while True:
        try:
            issue_date = datetime.strptime(input("Введите деадлайн в формате ДД-ММ-ГГГГ"), '%d-%m-%Y')
            break
        except ValueError:
            print("Неверный формат даты, попробуйте ещё раз")

    note = {"Название заметки": title,
            "Заголовки": heads,
            "Содержание": content,
            "Статус": status,
            "Дата создания": created_date,
            "Дата окончания": issue_date
            }
    notes.append(note)

    for _ in range(len(notes)): # вызов названий заметок путем перебора всех имеющихся
        print(f'Заметка №{_ + 1}:')
        print(notes[_].get("Название заметки"))

    while True:
        add_input = input("Добавить ещё заметок? да/нет").lower()
        # используется add_input, т.к. add_input.py использвать не планирую
        if add_input == 'да':
            break
        elif add_input == 'нет':
            break
    if add_input == 'нет':
        break