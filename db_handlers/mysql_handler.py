import pymysql
from config.config import Config

class MySQLHandler:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try: 
            self.connection = pymysql.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                database=Config.DB_NAME
            )
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        except pymysql.MySQLError as e:
            print(f'MySQL connection error: {e}')
            raise

    def disconnect(self):
        if self.connection:
            self.connection.close()
    
    def execute_query(self, query, params=None):
        self.connect()
        try:
            self.cursor.execute(query, params)
            if query.strip().upper.startswith('SELECT'):
                result = self.cursor.fetchall()
            else:
                self.connection.commit()
                result = self.cursor.rowcount
            return result
        except Exception as e:
            self.connection.rollback()
            raise e
        finally:
            self.disconnect()

