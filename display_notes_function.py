from datetime import datetime
def  display_notes_function(notes):
    for _ in range(len(notes)):  # вызов названий заметок путем перебора всех имеющихся
        print("Текущий список заметок:")
        print(f'Заметка №{_ + 1}:')
        print(f'Имя пользователя: {notes[_].get("Имя")}\n \nЗаголовки: {notes[_].get("Заголовки")}'
              f'Содержание: {notes[_].get("Содержание")}\n \n'
              f'Статус: {notes[_].get("Статус")}\n \n'
              f'Дата создания: {format(notes[_].get("Дата создания"), "%d-%m-%Y")}\n \n'
              f'Дата окончания: {format(notes[_].get("Дата окончания"), "%d-%m-%Y")}')

# не тестил