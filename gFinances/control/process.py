from model.data import Data

class Process:
    def __init__(self):
        self.data = Data()

    def RequestReceivement(self):
        total = 0
        query = """
        SELECT value FROM receivement
        WHERE SUBSTR(receipt_date, 4, 2) = '07';
        """

        cursor = self.data.Read(query)

        for value in cursor.fetchall():
            total = total + float(value[0])

        return str(total)

    def RequestExpense(self):
        total = 0
        query = """
        SELECT value FROM expense
        WHERE SUBSTR(expense_date, 4, 2) = '07';
        """

        cursor = self.data.Read(query)

        for value in cursor.fetchall():
            total = total + float(value[0])

        return str(total)
