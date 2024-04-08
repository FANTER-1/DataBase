import psycopg2
import psycopg2.extras

class Database:
    def __init__(self, dbname, user, password, host):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host
        )
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def submit_data(self, coordinates, height, name, photos, user_name, email, phone):
        self.cur.execute("""
        INSERT INTO mountain_passes (coordinates, height, name, photos, user_name, email, phone)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (coordinates, height, name, photos, user_name, email, phone))
        self.conn.commit()