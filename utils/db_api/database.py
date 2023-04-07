import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Groups (
            id int NOT NULL,
            name varchar(255) NOT NULL,
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, parameters=(), commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_group(self, chat_id: int, name: str = "Name"):

        sql = """
        INSERT or IGNORE INTO Groups(id, name) VALUES(?, ?)
        """
        self.execute(sql, parameters=(chat_id, name,), commit=True)

    def select_all_groups(self):
        sql = """
        SELECT id FROM Groups
        """
        result = self.execute(sql, fetchall=True)
        return [item[0] for item in result]
