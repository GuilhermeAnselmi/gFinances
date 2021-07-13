import os

from model.data import Data

class Transaction:
    def __init__(self, description, value, date):
        self.description = description
        self.value = value
        self.date = date

        self.data = Data()

    def SendReceivement(self):
        query = "insert into receivement(description, value, receipt_date) " \
                "values(" \
                "   '" + self.description + "'," \
                "   '" + self.value + "'," \
                "   '" + self.date + "'" \
                ")"

        return self.data.Write(query)

    def SendExpense(self):
        query = "insert into expense(description, value, expense_date) " \
                "values(" \
                "   '" + self.description + "'," \
                "   '" + self.value + "'," \
                "   '" + self.date + "'" \
                ")"

        return self.data.Write(query)
