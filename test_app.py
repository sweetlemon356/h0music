from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '20')
Config.set('graphics', 'height', '798')


class MusicApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.window_x = Window.size[0]
        self.window_y = Window.size[1]
        self.all_window = BoxLayout(orientation='vertical', size_hint=[1, 1])
        if True:  # Make fast_menu
            self.fast_menu = BoxLayout(size_hint=[1, .0625])
            self.btn1 = Button(text='music', size_hint=[1, 1])
            self.btn2 = Button(text='+', size_hint=[1, 1])
            self.btn3 = Button(text='profil', size_hint=[1, 1], on_press=self.press_profile)
            self.fast_menu.add_widget(self.btn1)
            self.fast_menu.add_widget(self.btn2)
            self.fast_menu.add_widget(self.btn3)
        if True:  # Make main_menu and variety of main menu
            self.profile_menu = BoxLayout()
            self.make_profile_menu()
            self.main_menu = BoxLayout(size_hint=[1, .9375])
            self.main_menu.add_widget(self.profile_menu)
        self.all_window.add_widget(self.main_menu)
        self.all_window.add_widget(self.fast_menu)

    def build(self):
        return self.all_window

    def press_profile(self, instance):
        pass

    def make_profile_menu(self):
        self.profile_menu.add_widget(Button(text='name', size_hint=[1, 1]))


if __name__ == '__main__':
    MusicApp().run()
