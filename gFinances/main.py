import kivy

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from view.menu import Menu
from view.finances import Finances
from style import Buttons

class Manager(ScreenManager):
    pass

class GFinances(App):
    def build(self):
        return Manager()

GFinances().run()
