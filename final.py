from date_changer import date_changer
import add_input
import status_
from add_list import heads

# from update_status import update_status



# данный фаил объединяет все предущие в один формат
note = {"Название заметки:", add_input.title,
        "Заголовки:", heads,
        "Содержание заметки:", add_input.content,
        "Статус заметки:", status_.status,
        "Дата создания:", date_changer(add_input.created_date),
        "Дата окончания", date_changer(add_input.issue_date)
        }
print(*note[0:3], sep='\n')
print(*note[3])
print(*note[4:9], sep='\n')
print(*note[9])
print(note[10])
print(*note[11])



# update_status(input())

