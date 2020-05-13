from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.label import Label


class MusicApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.window_x = Window.size[0]
        self.window_y = Window.size[1]
        self.all_window = BoxLayout(orientation='vertical', size_hint=[1, 1])
        if True:  # Make fast_menu
            self.fast_menu = BoxLayout(size_hint=[1, .0625])
            self.btn1 = Button(text='music', size_hint=[1, 1], on_press=self.press_chart)
            self.btn2 = Button(text='+', size_hint=[1, 1], on_press=self.press_add_music)
            self.btn3 = Button(text='profil', size_hint=[1, 1], on_press=self.press_profile)
            self.fast_menu.add_widget(self.btn1)
            self.fast_menu.add_widget(self.btn2)
            self.fast_menu.add_widget(self.btn3)
        if True:  # Make main_menu and variety of main menu
            self.profile_menu = BoxLayout()
            self.make_profile_menu()
            self.chart_menu = BoxLayout()
            self.make_chart_menu()
            self.add_music_menu = BoxLayout()
            self.make_add_music_menu()
            self.main_menu = BoxLayout(size_hint=[1, .9375])
            self.main_menu.add_widget(self.profile_menu)
        self.all_window.add_widget(self.main_menu)
        self.all_window.add_widget(self.fast_menu)

    def build(self):
        return self.all_window

    def press_chart(self, instance):  # at the moment it is finished
        self.main_menu.clear_widgets()
        self.main_menu.add_widget(self.chart_menu)

    def press_add_music(self, instance):  # at the moment it is finished
        self.main_menu.clear_widgets()
        self.main_menu.add_widget(self.add_music_menu)

    def press_profile(self, instance):  # at the moment it is finished
        self.main_menu.clear_widgets()
        self.main_menu.add_widget(self.profile_menu)

    def make_profile_menu(self):  # a lot of work
        self.profile_menu.add_widget(Button(text='profile', size_hint=[1, 1]))

    def make_add_music_menu(self):  # a lot of work
        self.add_music_menu.add_widget(Button(text='add music', size_hint=[1, 1]))

    def make_chart_menu(self):  # a lot of work
        self.chart_menu.add_widget(Button(text='chart', size_hint=[1, 1]))


if __name__ == '__main__':
    app = MusicApp()
    app.run()
