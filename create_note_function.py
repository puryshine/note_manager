from datetime import datetime
def create_note_function():
    status_lib = {"а": 'Активный', "о": 'Отменен', "з": 'Завершен'}
    name = input("Введите имя пользователя")
    heads = input('Введите заголовок')
    content = input("Введите содержание заметки")
    status_temp = 0
    while status_temp not in ["а", "о", "з"]:
        status_temp = input("Введите статус заметки буквой: А — Активный, О — Отменен, З — Завершен").lower()
    status = status_lib[status_temp]
    created_date = datetime.now()
    while True:
        try:
            issue_date = datetime.strptime(input("Введите дедлайн в формате ДД-ММ-ГГГГ"), '%d-%m-%Y')
            break
        except ValueError:
            print("Неверный формат даты, попробуйте ещё раз")

    note = {"Имя": name,
            "Заголовки": heads,
            "Содержание": content,
            "Статус": status,
            "Дата создания": created_date,
            "Дата окончания": issue_date
            }
    return note
note = create_note_function()
print(note)