import sqlite3
import os

class Data:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()

    def VerifyData(self):
        if os.path.isfile("data.db"):
            query1 = """
            CREATE TABLE IF NOT EXISTS receivement (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                description VARCHAR(0, 100) NOT NULL,
                value DOUBLE NOT NULL DEFAULT (0.0),
                receipt_date DATE NOT NULL DEFAULT (date() ) 
            );
            """

            query2 = """
            CREATE TABLE IF NOT EXISTS expense (
                id  INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                description VARCHAR(0, 100) NOT NULL,
                value DOUBLE NOT NULL DEFAULT (0.0),
                expense_date DATE NOT NULL DEFAULT (date() ) 
            );
            """

            try:
                self.cursor.execute(query1)
                self.cursor.execute(query2)

                return True
            except:
                return False

    def Write(self, query):
        verify = self.VerifyData()

        if verify:
            try:
                self.cursor.execute(query)
                self.conn.commit()

                return True
            except:
                self.conn.close()
                return False
        else:
            self.conn.close()
            return False

    def Read(self, query):
        verify = self.VerifyData()

        if verify:
            try:
                self.cursor.execute(query)

                return self.cursor
            except:
                self.conn.close()
                return False
        else:
            self.conn.close()
            return False

    def Close(self):
        try:
            self.conn.close()

            return True
        except:
            return False
