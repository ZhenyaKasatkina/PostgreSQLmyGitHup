import psycopg2
import json

"""postgres_db.py содержит класс PostgresDB, который обеспечивает взаимодействие 
с базой данных Postgres. Класс реализует методы, чтобы создать таблицу, 
добавить данные в таблицу, экспортировать данные в формат JSON и 
получить данные из таблицы."""


class PostgresDB:
    def __init__(self, data: dict, name_table: str, params: dict):
        self.data = data
        self.params = params
        self.conn = psycopg2.connect(**self.params)
        self.conn.autocommit = True
        self.name_table = name_table

    def add_table(self):
        """
        Создание новой табл в БД
        """
        with self.conn.cursor() as cur:
            cur.execute(f"DROP TABLE {self.name_table}")
            cur.execute(f"""CREATE TABLE {self.name_table} 
            (id_repository serial PRIMARY KEY, 
            name_repository VARCHAR(255), 
            language VARCHAR(50), 
            size INT, 
            stars INT, 
            forks_count INT, 
            archived BOOLEAN, 
            visibility VARCHAR(255), 
            clone_url TEXT)""")

    def save_data_in_table(self):
        """
        Загрузка данных в созданную табл
        """
        with self.conn.cursor() as cur:
            for data in self.data:
                cur.execute(
                    f"""INSERT INTO {self.name_table} (id_repository, name_repository, 
                    language, size, stars,  forks_count, archived, visibility, clone_url) 
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (data['id_repository'], data['name_repository'],
                                                                    data['language'], data['size'], data['stars'],
                                                                    data['forks_count'], data['archived'],
                                                                    data['visibility'], data['clone_url'])
                )

    def export_to_json(self):
        """
        Выгружает данные в формате JSON
        :return: новый файл json с данными из таблицы
        """
        with self.conn.cursor() as cur:
            cur.execute(f"SELECT * FROM {self.name_table}")
            data = cur.fetchall()
            data_dict = [{"id": d[0], "name": d[1], "language": d[2], "size": d[3], "stars": d[4],
                          "forks_count": d[5], "clone_url": d[8]} for d in data]
            with open(f"{self.name_table}.json", "w") as f:
                json.dump(data_dict, f, indent=4)

    def get_data_alphabetically(self):
        """
        Фильтр по алфавиту
        :return: список кортежей данных по каждому репозиторию
        """
        with self.conn.cursor() as cur:
            cur.execute(f"""SELECT * FROM {self.name_table}
            ORDER BY name_repository""")
            rows = cur.fetchall()
            return rows
