import sqlite3

class Data:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()

    def Write(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
            self.conn.close()

            return True
        except:
            return False

    def Read(self, query):
        try:
            self.cursor.execute(query)

            return self.cursor
        except:
            return False
