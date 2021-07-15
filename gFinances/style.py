from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.label import Label
from kivy.properties import ListProperty

class Buttons(ButtonBehavior, Label):
    colored = ListProperty([0.1, 0.1, 1, 1])
    coloredClick = ListProperty([0.1, 0.1, 0.5, 1])

    def __init__(self, **kwargs):
        super(Buttons, self).__init__(**kwargs)
        self.ButtonDefinition()

    def on_pos(self, *args):
        self.ButtonDefinition()

    def on_size(self, *args):
        self.ButtonDefinition()

    def on_press(self, *args):
        self.colored, self.coloredClick = self.coloredClick, self.colored
        self.ButtonDefinition()

    def on_release(self, *args):
        self.colored, self.coloredClick = self.coloredClick, self.colored
        self.ButtonDefinition()

    def ButtonDefinition(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.colored)
            Ellipse(size=[self.height, self.height], pos=self.pos)
            Ellipse(size=[self.height, self.height], pos=[self.x + self.width - self.height, self.y])
            Rectangle(size=[self.width - self.height, self.height], pos=[self.x + self.height / 2.0, self.y])
