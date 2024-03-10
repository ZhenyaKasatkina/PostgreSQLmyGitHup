# PostgreSQLmyGitHup

Проект состоит из трех основных компонентов:
main.py, functions.py и postgres_db.py.

functions.py содержит функцию get_repos_stats(), которая собирает 
статистику по репозиториям заданного пользователя на GitHub. 
Эта функция использует библиотеку requests, чтобы обращаться к API GitHub 
и получать информации о репозиториях пользователя. 
Затем функция обрабатывает полученные данные и возвращает список словарей, 
содержащих статистику по каждому репозиторию.

postgres_db.py содержит класс PostgresDB, который обеспечивает взаимодействие 
с базой данных Postgres. Класс реализует методы, чтобы создать таблицу, 
добавить данные в таблицу, экспортировать данные в формат JSON и 
получить данные из таблицы.

main.py является точкой входа в проект. Его основная функция main() 
вызывает функцию get_repos_stats(), чтобы собрать статистику по 
репозиториям пользователя, и затем использует класс PostgresDB
для сохранения данных в базу данных. В конце функция вызывает другой 
метод класса PostgresDB, чтобы экспортировать данные в формате JSON.