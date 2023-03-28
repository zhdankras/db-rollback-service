from mysql.connector import MySQLConnection, Error
from confluence_parse import content_parse

projects_macro_id = 'b9f9ec6e-d350-46dd-8ea9-25edc3affbd0'

class Projects:

    def __init__(self, connection: MySQLConnection):
        self.conn = connection

    def insert_projects(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(content_parse(projects_macro_id))
                self.conn.commit()
            return f"INFO: Insert data into projects table: Done!"
        except Error as e:
            return f"ERROR: {e}"
