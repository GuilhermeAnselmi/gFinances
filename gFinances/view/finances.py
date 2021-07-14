from kivy.uix.screenmanager import Screen

from control.process import Process

class Finances(Screen):
    def __init__(self, **kwargs):
        super(Finances, self).__init__(**kwargs)

        self.process = Process()

    def on_enter(self, *args, **kwargs):
        receivement = self.process.RequestReceivement()
        expense = self.process.RequestExpense()
        total = float(receivement) - float(expense)

        self.ids.lblReceivement.text = receivement
        self.ids.lblExpense.text = expense
        self.ids.lblTotal.text = str(total)
