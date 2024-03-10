import requests

"""functions.py содержит функцию get_repos_stats(), которая собирает статистику
по репозиториям заданного пользователя на GitHub. Эта функция использует библиотеку
requests, чтобы обращаться к API GitHub и получать информации о
репозиториях пользователя. Затем функция обрабатывает полученные данные и
возвращает список словарей, содержащих статистику по каждому репозиторию."""


def get_repos_stats(user_login):
    data = []
    bases_url = 'https://api.github.com'
    method_name = f"/users/{user_login}/repos"
    response = requests.get(f"{bases_url}{method_name}")
    # print(response.json(), len(response.json()))
    # print(response.status_code)
    for item in response.json():
        data.append({'id_repository': item['id'],
                     'name_repository': item['name'],
                     'language': item['language'],
                     'size': item['size'],
                     'stars': item['stargazers_count'],        # количество звезд
                     'forks_count': item['forks_count'],       # ответвление
                     'archived': item['archived'],             # в архиве
                     'visibility': item['visibility'],         # видимость
                     'clone_url': item['clone_url']})          # ссылка для клонирования

    return data

# https://github.com/ZhenyaKasatkina/
# x = get_repos_stats('ZhenyaKasatkina')
# print(x)
