import kivy

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from control.transaction import Transaction
from view.menu import Menu
from view.finances import Finances
from view.receivement import Receivement
from view.expense import Expense
from style import Buttons

class Manager(ScreenManager):
    pass

class GFinances(App):
    def build(self):
        return Manager()

GFinances().run()
