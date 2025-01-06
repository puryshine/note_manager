def update_note_function():  # в задании нет перебора по заметкам, думаю функцию можно применять по индексу
    print(f'Текущие данные заметки:\n{note}')
    while True:
        print("Поля заметки:\nИмя, Заголовки, Содержание, Статус, Дата окончания")
        add_input = input("Введите поле заметки, что хотите изменить").capitalize()
        if add_input == "Заголовки":
            heads = input("Введите новый заголовок")
        elif add_input == "Содержание":
            content = input("Введите новое содержание")
        elif add_input == "Имя"
            name = input("Введите новое имя пользователя")
        elif add_input == "Дата окончания":
            while True:
                try:
                    issue_date = datetime.strptime(input("Введите дедлайн в формате ДД-ММ-ГГГГ"), '%d-%m-%Y')
                    break
                except ValueError:
                    print("Неверный формат даты, попробуйте ещё раз")
        elif add_input == "Статус":
            status_temp = input("Введите статус заметки буквой: А — Активный, О — Отменен, З — Завершен").lower()
            while True:
                if status_temp != "а" and status_temp != "о" and status_temp != "з":
                    status_temp = input(
                        "Введите статус заметки буквой: А — Активный, О — Отменен, З — Завершен"
                    ).lower()
                    break
            status_lib = {"а": 'Активный', "о": 'Отменен', "з": 'Завершен'}
            status = (status_lib[update_status(request)])
        else:
            print("Неверное имя поля, попробуйте ещё раз")

        while True:
            add_input = input("Желаете обновить какое-то поле ещё?(да/нет)").lower()
            if add_input == 'да':
                break
            elif add_input == 'нет':
                break
        if add_input == 'нет':
            break