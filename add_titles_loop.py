from add_list import heads
heads = list(heads)
request = input("Добавьте заголовок, для отмены оставьте строчку пустой")
while request != '':      # цикл для реализации повторного запроса заголовка
    if request not in heads: # отсечение повторов
        heads.append(request) # добавляем новый заголовок в конец списка, если таковой имеется
    else:
        print('Такой заголовок уже имеется')
    print("Заголовки:")
    print(*heads)
    request = input("Добавьте заголовок, для отмены оставьте строчку пустой")
heads = tuple(heads)
print("\nЗаголовки:")
print(*heads)
