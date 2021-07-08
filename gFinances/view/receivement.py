from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.animation import Animation

class Receivement(Screen):
    def __init__(self, **kwargs):
        super(Receivement, self).__init__(**kwargs)

    def Return(self, *args, **kwargs):
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        buttons = BoxLayout(spacing=10)
        self.pop = Popup(title='Deseja retornar sem salvar?', content=box, size_hint=[None, None], size=['150sp', '100sp'])

        btnConfirm = Button(text='Yes', on_release=self.Confirm)
        btnCancel = Button(text='No', on_release=self.pop.dismiss)

        buttons.add_widget(btnConfirm)
        buttons.add_widget(btnCancel)

        box.add_widget(buttons)

        anim = Animation(size=[200, 150], duration=0.4, t='out_back')
        anim.start(self.pop)

        self.pop.open()

    def Confirm(self, *args):
        self.pop.dismiss()
        App.get_running_app().root.current = 'finances'
