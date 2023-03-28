from mysql.connector import MySQLConnection, Error
from confluence_parse import content_parse

accounts_macro_id = '94bce89c-7f13-4a79-abfe-bedd6279174e'

class Accounts:

    def __init__(self, connection: MySQLConnection):
        self.conn = connection

    def insert_accounts(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(content_parse(accounts_macro_id))
                self.conn.commit()
            return f"INFO: Insert data into accounts table: Done!"
        except Error as e:
            return f"ERROR: {e}"
