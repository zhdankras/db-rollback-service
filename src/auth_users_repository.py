from mysql.connector import MySQLConnection, Error
from confluence_parse import content_parse

auth_users_macro_id = '13594000-dd74-4857-8952-d4f82c710888'

class AuthUsers:

    def __init__(self, connection: MySQLConnection):
        self.conn = connection

    def insert_auth_users(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(content_parse(auth_users_macro_id))
                self.conn.commit()
            return f"INFO: Insert data into auth_users table: Done!"
        except Error as e:
            return f"ERROR: {e}"
