from add_list import heads
zapros = input("Введите заголовок, для отмены оставьте строчку пустой")
while zapros != '':
    heads.append(zapros)
    zapros = input("Введите заголовок, для отмены оставьте строчку пустой")
    print(*heads)