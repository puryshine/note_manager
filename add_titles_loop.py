from add_list import heads
zapros = input("добавьте заголовок, для отмены оставьте строчку пустой")
while zapros != '':      # цикл для реализации повторного запроса заголовка
    if zapros not in heads:
        heads.append(zapros) # добавляем новый заголовок в конец списка, если таковой имеется
    else:
        print('такой заголовок уже имеется')
    print(*heads)
    zapros = input("добавьте заголовок, для отмены оставьте строчку пустой")
print(*heads)