# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout

Builder.load_file("QuizPage.kv")


class QuizPageApp(App):
    def build(self):
        return QuizManager()


class QuizManager(ScreenManager):
    pass


class Question1(Screen):
    def answered(self,correctness):
        if correctness:
            self.manager.current = "yes"
        else:
            self.manager.current = "no"


class Question2(Screen):
    pass


class Correct(Screen):
    def proceed(self):
        self.manager.current = "two"


class Incorrect(Screen):
    def proceed(self):
        self.manager.current = "two"


QuizPageApp().run()
