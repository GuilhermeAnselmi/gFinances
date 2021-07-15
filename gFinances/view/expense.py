from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.popup import Popup

from control.transaction import Transaction

class Expense(Screen):
    def __init__(self, **kwargs):
        super(Expense, self).__init__(**kwargs)

    def Save(self, *args, **kwargs):
        box = BoxLayout(orientation='vertical', padding=20, spacing=10)
        buttons = BoxLayout(spacing=20)
        pop = Popup(content=box, size_hint=[None, None], size=['150dp', '100dp'])

        btnOk = Button(text='Ok', on_release=pop.dismiss)

        buttons.add_widget(btnOk)
        box.add_widget(buttons)

        anim = Animation(size=[650, 400], duration=0.4, t='out_back')
        anim.start(pop)

        description = self.ids.txtDescription.text
        value = self.ids.txtValue.text
        day = self.ids.txtDay.text
        month = self.ids.txtMonth.text
        year = self.ids.txtYear.text

        if description != '' and value != '' and day != '' and month != '' and year != '':
            if float(value) >= 0.0:
                if (int(day) > 0 and int(day) <= 31) and (int(month) > 0 and int(month) <= 12) and len(year) <= 4:
                    if len(day) == 1:
                        day = "0" + day

                    if len(month) == 1:
                        month = "0" + month

                    date = day + "/" + month + "/" + year
                    self.transaction = Transaction(description, value, date)

                    verify = self.transaction.SendExpense()

                    if verify:
                        self.ids.txtDescription.text = ""
                        self.ids.txtValue.text = ""
                        self.ids.txtDay.text = ""
                        self.ids.txtMonth.text = ""
                        self.ids.txtYear.text = ""
                        App.get_running_app().root.current = 'finances'
                    else:
                        pop.title = "Error sending data"
                        pop.open()
                else:
                    pop.title = "Invalid date formatting"
                    pop.open()
            else:
                pop.title = "Cannot use negative value"
                pop.open()
        else:
            pop.title = "Enter data to continue"
            pop.open()

    def Return(self, *args, **kwargs):
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        buttons = BoxLayout(spacing=20)
        self.pop = Popup(title='Do you want to return without saving?', content=box, size_hint=[None, None], size=['150dp', '100dp'])

        btnConfirm = Button(text='Yes', on_release=self.Confirm)
        btnCancel = Button(text='No', on_release=self.pop.dismiss)

        buttons.add_widget(btnConfirm)
        buttons.add_widget(btnCancel)

        box.add_widget(buttons)

        anim = Animation(size=[650, 400], duration=0.4, t='out_back')
        anim.start(self.pop)

        self.pop.open()

    def Confirm(self, *args):
        self.pop.dismiss()
        App.get_running_app().root.current = 'finances'
