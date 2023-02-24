import pymysql


class DBConnector:
    connection = None

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        if not DBConnector.connection:
            DBConnector.connection = self.connect()

    def connect(self):
        connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return connection

    def execute_many(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        res = cursor.fetchall()
        cursor.close()
        return res

    def execute_one(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        res = cursor.fetchone()
        cursor.close()
        return res

    def close(self, connection):
        connection.close()
