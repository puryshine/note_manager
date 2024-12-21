from add_list import heads
heads = list(heads)
zapros = input("Добавьте заголовок, для отмены оставьте строчку пустой")
while zapros != '':      # цикл для реализации повторного запроса заголовка
    if zapros not in heads: # отсечение повторов
        heads.append(zapros) # добавляем новый заголовок в конец списка, если таковой имеется
    else:
        print('Такой заголовок уже имеется')
    print(*"Заголовки: \n", heads)
    zapros = input("Добавьте заголовок, для отмены оставьте строчку пустой")
heads = tuple(heads)
print(*"Заголовки: \n", heads)
