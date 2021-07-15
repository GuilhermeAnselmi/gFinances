from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

from control.process import Process

class Finances(Screen):
    def __init__(self, **kwargs):
        super(Finances, self).__init__(**kwargs)
        self.process = Process()

    def on_enter(self, *args, **kwargs):
        receivement = self.process.RequestReceivement()
        expense = self.process.RequestExpense()
        total = float(receivement) - float(expense)

        self.ids.lblReceivement.text = "R$ " + receivement
        self.ids.lblExpense.text = "R$ " + expense
        self.ids.lblTotal.text = "R$ " + str(total)
