from src.functions import get_repos_stats
from src.config import config
from src.postgres_db import PostgresDB

"""main.py является точкой входа в проект. Его основная функция main() 
вызывает функцию get_repos_stats(), чтобы собрать статистику по 
репозиториям пользователя, и затем использует класс PostgresDB
для сохранения данных в базу данных. В конце функция вызывает другой 
метод класса PostgresDB, чтобы экспортировать данные в формате JSON."""

LOGIN = 'ZhenyaKasatkina'
PARAMS = config()


def main():
    print(f"получение инфо по репозиториям профиля {LOGIN} на GitHup")
    repo_data = get_repos_stats(LOGIN)
    print(f"Сохранение данных в таблицу '{LOGIN}' базы данных 'Postgres'.")
    instance = PostgresDB(repo_data, LOGIN, PARAMS)
    instance.add_table()
    instance.save_data_in_table()
    print("Выводим список репозиториев с данными по алфавиту и завершаем работу программы")
    data = instance.get_data_alphabetically()
    for item in data:
        print(item)
    instance.export_to_json()
    instance.conn.close()


if __name__ == '__main__':
    main()
