# note_manager
greetings.py - демонстрация аргументами и выводом
как это должно работать
add_input.py - содержит в себе функции по созданию основных
параметров заметки
add_list.py - модуль создания трех заголовков
date_changer.py - конвертер типа datetime в формат день, месяц
datechanger.py - копия date_changer.py, но не содержит 
тестирование функции, для того чтобы не нагромождать input'ами
final.py
status_.py - вынужденный костыль, содержит функцию 
создания статуса
final.py - объединяющее звено этих модулей в единое целое, 
кроме greetings.py
add_titles_loop.py - позволяет обновлять статус заметки.
на данный момент не интегрирован в finals.py
update_status.py - обновляет статус заметки. пока не работает
check_deadline.py - вычисляет сколько дней осталось до дедлайна
на текущую дату
delete_notes.py - удаляет заметки по имени пользователя/заголовку
multiple_notes.py - позволяет создавать несколько заметок
create_note_function.py - создает заметку, но не добавляет
к списку уже имеющихся
display_note_function.py - функция вывода всех заметок