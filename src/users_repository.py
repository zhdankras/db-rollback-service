from mysql.connector import MySQLConnection, Error
from confluence_parse import content_parse

users_macro_id = '75f67e9f-51ac-4ecc-a91f-dda9c5172e2f'

class Users:

    def __init__(self, connection: MySQLConnection):
        self.conn = connection

    def insert_users(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(content_parse(users_macro_id)) 
                self.conn.commit()
            return f"INFO: Insert data into users table: Done!"
        except Error as e:
            return f"ERROR: {e}"
