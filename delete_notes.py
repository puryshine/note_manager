def delete_notes(notes):
    while True:
        add_input = input("Желаете удалить заметку? Да/Нет").lower()
        # используется add_input, т.к. add_input.py использвать не планирую
        if add_input == 'да':
            break
        elif add_input == 'нет':
            break
    if add_input == "нет":
        break
    find_key = input("Введите имя пользователя или заголовок заметки \nкоторый желаете удалить").lower().strip()
    for _ in range(len(notes)):
        if find_key in notes[_].get('Имя') and notes[_].get("Заголовки"):
            print(f"Такое имя пользователя/заголовок ({find_key}) найдено!")
            print(f'Вот заметка: {notes[_].get("Имя"), notes[_].get("Заголовки")}') # В терминал
            while True:
                add_input = input("Удалить?(да/нет)").lower()
                if add_input == "да":
                    notes.pop(_)
                    break
                elif add_input == "нет":
                    break
        else:
            print(f"{find_key} не найден")
    for _ in range(len(notes)):  # вызов названий заметок путем перебора всех имеющихся
        print("Текущий список заметок:")
        print(f'Заметка №{_ + 1}:')
        print(notes[_].get("Имя"), notes[_].get("Заголовки"))