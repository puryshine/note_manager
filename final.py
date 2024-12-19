from importlib import reload
from date_changer import date_changer
import add_input
import status_
from add_list import heads



# данный фаил объединяет все предущие в один формат
note = ["Название заметки:", add_input.title,
        "Заголовки:", heads,
        "Содержание заметки:", add_input.content,
        "Статус заметки:", status_.status,
        "Дата создания:", date_changer(add_input.created_date),
        "Дата окончания", date_changer(add_input.issue_date)
        ]

print(*note, sep='\n')

_ = ''  # случайная переменная
while _ != 50:
    if input("Желаете изменить статус заметки? Да/Нет").lower() == 'да':
        reload(status_)
        print(*note, sep='\n')     # не работает не представляю почему ;(
