from datetime import datetime


def update_note_function(note):  # в задании нет перебора по заметкам, думаю функцию можно применять по индексу
    print(f'Текущие данные заметки:\n{note}')
    while True:
        print("Поля заметки:\nИмя, Заголовки, Содержание, Статус, Дата окончания")
        add_input = input("Введите поле заметки, что хотите изменить").capitalize()
        if add_input == "Заголовки":
            while True:
                add_input = input("Желаете заголовки?(да/нет)").lower()
                if add_input == "да":
                    heads = input("Введите новый заголовок")
                    break
                elif add_input == 'нет':
                    break
        elif add_input == "Содержание":
            while True:
                add_input = input("Желаете содержание заметки?(да/нет)").lower()
                if add_input == "да":
                    content = input("Введите новое содержание")
                    break
                elif add_input == 'нет':
                    break
        elif add_input == "Имя":
            while True:
                add_input = input("Желаете имя пользователя?(да/нет)").lower()
                if add_input == "да":
                    name = input("Введите новое имя пользователя")
                    break
                elif add_input == 'нет':
                    break
        elif add_input == "Дата окончания":
            while True:
                add_input = input("Желаете дедлайн?(да/нет)").lower()
                if add_input == "да":
                    while True:
                        try:
                            issue_date = datetime.strptime(input("Введите дедлайн в формате ДД-ММ-ГГГГ"), '%d-%m-%Y')
                            break
                        except ValueError:
                            print("Неверный формат даты, попробуйте ещё раз")
                            break
                elif add_input == 'нет':
                    break
        elif add_input == "Статус":
            while True:
                add_input = input("Желаете изменить статус заметки?(да/нет)").lower()
                if add_input == "да":
                    status_temp = input(
                        "Введите статус заметки буквой: А — Активный, О — Отменен, З — Завершен").lower()
                    while True:
                        if status_temp != "а" and status_temp != "о" and status_temp != "з":
                            status_temp = input(
                                "Введите статус заметки буквой: А — Активный, О — Отменен, З — Завершен"
                            ).lower()
                            break
                    break
                elif add_input == 'нет':
                    break
            status_lib = {"а": 'Активный', "о": 'Отменен', "з": 'Завершен'}
            status = (status_lib[status_temp])
        else:
            print("Неверное имя поля, попробуйте ещё раз")
        print(f'Текущие данные заметки:\n{note}')
        while True:
            add_input = input("Желаете обновить какое-то поле ещё?(да/нет)").lower()
            if add_input == 'да':
                break
            elif add_input == 'нет':
                break
        if add_input == 'нет':
            break

# без теста