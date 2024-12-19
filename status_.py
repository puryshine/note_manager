status_lib = {"а": 'Активный', "о": 'Отменен', "к": 'Крайне важный'}
status_temp = input("Введите статус заметки буквой: А — Активный, О — Отменен, К — Крайне важный").lower()
status_count = False
while status_count == False:
    if status_temp != "а" and status_temp != "о" and status_temp != "к":
        status_temp = input("Введите статус заметки буквой: А — Активный, О — Отменен, К — Крайне важный").lower()
    else:
        status_count = True
status=(status_lib[status_temp]) #защита от дурочка, чтобы один из трех всё-же выбрали и программа не улетала в ошибку