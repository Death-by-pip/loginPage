# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout

Builder.load_file("QuizPage.kv")


class Login(Screen):
    def verify(self):
        with open("logins.txt", "r") as f:
            for line in f:
                if line.split(" ")[0] == self.ids.username.text:
                    if line.split(" ")[1] == self.ids.password.text:
                        self.manager.current = "one"
                    else:
                        self.invalid("Invalid password")
        self.invalid("Username not found")

    def invalid(self, message):
        self.ids.invalid_txt.text = message

    def register(self):
        self.manager.current = "new"


class Register(Screen):
    def back(self):
        self.manager.current = "login"
    def verify(self):
        if self.ids.username.text=="":
            self.invalid("Enter Username")
            return
        if self.ids.pass1.text!=self.ids.pass2.text:
            self.invalid("Passwords must match")
            return
        txt = self.ids.pass1.text
        if len(txt)<8:
            self.invalid("Password is of insufficient length")
        LIST = []
        check = False
        for i in txt:
            list_ = "a,b,c,d,e,f,g,h,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
            [LIST.append(n) for n in list_]
            if i in list_:
                check = True
                break
        if check:
            check = False
            for i in txt:
                list_ = "a,b,c,d,e,f,g,h,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".upper().split(",")
                [LIST.append(n) for n in list_]
                if i in list_:
                    check = True
                    break
        if check:
            check = False
            for i in txt:
                list_ = "1,2,3,4,5,6,7,8,9,0".split(",")
                [LIST.append(n) for n in list_]
                if i in list_:
                    check = True
                    break
        if check:
            check = False
            for i in txt:
                list_ = "` ~ , . < > / ? ; ' : \" [ ] { } \\ | ! @ # $ % ^ & * ( ) - _ = +".split(" ")
                [LIST.append(n) for n in list_]
                if i in list_:
                    check = True
                    break
        if not check:
            self.invalid("password has insufficient characters")
        check = True
        for i in txt:
            if not (i in LIST):
                self.invalid("invalid character used")
                return
        for i in self.ids.username.text:
            if not (i in LIST):
                self.invalid("invalid character used")
                return
        with open("logins.txt","r") as f:
            for line in f:
                if line.split(" ")[0]==self.ids.username.text:
                    self.invalid("Username already in use")
                    return
        with open("logins.txt","a") as f:
            f.write("\n"+self.ids.username.text+" "+txt)
        self.manager.current = "login"

    def invalid(self, message):
        self.ids.invalid_txt.text = message


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
    def answered(self,correctness):
        if correctness:
            self.manager.current = "win"
        else:
            self.manager.current = "no"
    pass


class Correct(Screen):
    def proceed(self):
        self.manager.current = "two"


class Incorrect(Screen):
    def proceed(self):
        self.manager.current = "login"


QuizPageApp().run()
