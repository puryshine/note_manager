from datechanger import datechanger  # используется не date_changer, тк при его создании обязателен тест, что излишне
# для формата final
import add_input
import status_
from add_list import heads

from update_status import update_status


# данный фаил объединяет все предущие в один формат
note = {"название": add_input.title,
        "заголовки": heads,
        "содержание": add_input.content,
        "cтатус": status_.status,
        "дата создания": datechanger(add_input.created_date),
        "дата окончания": datechanger(add_input.issue_date)
        }
print("\nНазвание заметки:", note["название"], "\nЗаголовки:", sep='\n')
print(*note["заголовки"])
print("\nСодержание заметки:", note["содержание"], "\nСтатус:", sep='\n')
print(note["cтатус"], "\nДата создания:", sep="\n")
print(*note["дата создания"])
print("\nДата окончания:")
print(*note["дата окончания"])

update_status(input())
print(note["статус"])
