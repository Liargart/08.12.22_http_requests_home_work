print('Задание 1')

# Кто самый умный супергерой?
# Есть API (https://akabab.github.io/superhero-api/api/) по информации о супергероях с информацией по всем супергероям.
# Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.


import requests


class Heroes:
    # list_of_heroes

    def smartest_hero(self, heroes):
        heroes_intelligence = {}
        uri_all_heroes = 'https://akabab.github.io/superhero-api/api/all.json'
        headers = {'Content-Type': 'application/json'}
        response = requests.get(uri_all_heroes, headers=headers)
        for record in response.json():
            for hero in heroes:
                if record['name'] == hero:
                    heroes_intelligence[hero] = record['powerstats']['intelligence']
        print(f'Самый умный супергерой из списка - это  {max(heroes_intelligence, key=heroes_intelligence.get)}\n')

hr = Heroes()
heroes_list = ['Hulk', 'Captain America', 'Thanos']
hr.smartest_hero(heroes_list)


print('Задание 2\n')
# У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов существует Полигон.
# Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет на Яндекс.Диск
# с таким же именем.
# # Все ответы приходят в формате json;
# Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
# Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".
# HOST: https://cloud-api.yandex.net:443
# # Важно: Токен публиковать в github не нужно, переменную для токена нужно оставить пустой!

TOKEN = ''

class Yandex:
    host = 'https://cloud-api.yandex.net/'

    def __init__(self, token1):
        self.token = token1

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

# загрузка файла с компьютера
# Шаг 1. Получение ссылки для загрузки файла на Яндекс. Диск
    def get_upload_link(self, disk_file_name):
        uri = 'v1/disk/resources/upload/'
        url = self.host + uri
        params = {'path': f'/{disk_file_name}'}
        response = requests.get(url, headers=self.get_headers(), params=params)
        # print(response.json())
        # print(f'Статус: {response.status_code}')
        return response.json()['href']

# Шаг 2. Отправка файла с компьютера на Яндекс. Диск
    def get_from_pc(self, local_file_name, disk_file_name):
        upload_link = self.get_upload_link(disk_file_name)
        response = requests.put(upload_link, headers=self.get_headers(), data=open(local_file_name, 'rb'))
        print(f'Статус: {response.status_code}')


ya = Yandex(TOKEN)
path_to_file = 'D:\Temp\s1200.jpg'
ya.get_from_pc(path_to_file, 'test1.jpg')













