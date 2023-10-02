# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.text import LabelBase, DEFAULT_FONT

LabelBase.register(DEFAULT_FONT, "C:\\Windows\\Fonts\\Cour.ttf")
Builder.load_file("QuizPage.kv")


class QuizPageApp(App):
    def build(self):
        return QuizManager()


class LoginManager(ScreenManager):
    pass


class Question1(Screen):
    pass


class Question2(Screen):
    pass


class Correct(Screen):
    pass


class Incorrect(Screen):
    pass


QuizPageApp().run()
