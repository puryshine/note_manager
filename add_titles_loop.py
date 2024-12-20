from add_list import heads
zapros = input("добавьте заголовок, для отмены оставьте строчку пустой")
while zapros != '':
    heads.append(zapros)
    print(*heads)
    zapros = input("добавьте заголовок, для отмены оставьте строчку пустой")
print(*heads)