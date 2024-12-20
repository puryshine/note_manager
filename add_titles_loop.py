from add_list import heads
zapros = input("добавьте заголовок, для отмены оставьте строчку пустой")
while zapros != '':
    heads.append(zapros)
    zapros = input("добавьте заголовок, для отмены оставьте строчку пустой")
    print(f'{heads}')