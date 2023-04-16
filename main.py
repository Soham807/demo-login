import kivy
kivy.require("2.0.0")
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
#from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
import requests
import os
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.chip import MDChip
import hashlib
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivymd.uix.behaviors import (
    RectangularRippleBehavior,
    BackgroundColorBehavior,
    CommonElevationBehavior,
)
from kivy.core.text import LabelBase
from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from kivy.clock import Clock
import time
import threading
from firebase_admin import firestore



firebaseConfig = {
  "apiKey": "AIzaSyAzg7ZK3HumOtO30iJvcNgtjMf5rnx0kFw",
  "authDomain": "kivyapp-9081b.firebaseapp.com",
  "databaseURL": "https://kivyapp-9081b-default-rtdb.firebaseio.com",
  "projectId": "kivyapp-9081b",
  "storageBucket": "kivyapp-9081b.appspot.com",
  "messagingSenderId": "1023938036118",
  "appId": "1:1023938036118:web:99248cca6c6b943c93ddb7",
  "measurementId": "G-2Z3H6QTSV9"
}

firebase = firebase.FirebaseApplication("https://kivyapp-9081b-default-rtdb.firebaseio.com/", None)
kv = Builder.load_file("full_login.kv")
cred = credentials.Certificate("kivyapp-9081b-firebase-adminsdk-pjjcl-ae42219984.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

Window.size = (320, 600)

# class WindowManager(ScreenManager):
#     def __init__(self, **kwargs):
#         super(WindowManager, self).__init__(**kwargs)
        

#     def switch_to_screensaver(self):
#         self.current = "signup"
        
#     screen_main = ObjectProperty(None)
#     screen_login = ObjectProperty(None)
#     screen_signup = ObjectProperty(None)
#     screen_signup2 = ObjectProperty(None)
#     screen_dash = ObjectProperty(None)
    
def say_account_exists():
    print("You have already made an account on this device!")
    
    
# class ScreenStart(MDScreen):
#     def choose_entrance(self):
#         lol = open(file="id.txt", mode="r+")
#         if(os.path.getsize("id.txt") == 0):
#             MDApp.get_running_app().sm.current = 'ScreenSignup'
#         else:
#             MDApp.get_running_app().sm.current = 'ScreenDash'
#     if (Window.close == True):
#         lol = open(file="id.txt", mode='r+')
#         lol.truncate(0)



class ScreenMain(MDScreen):
    def go_to_login_screen(self):
        MDApp.get_running_app().sm.current = "ScreenLogin"
    def go_to_signup_screen(self):
        MDApp.get_running_app().sm.current = "ScreenSignup"
        
        
class ScreenLogin(MDScreen):
    def login(self, username, password):
        lol = open(file="id.txt", mode='r+')
        try:
            haha = auth.get_user_by_email(email=username)

            if hashlib.sha3_256(password.encode("utf-8")).hexdigest() == haha.custom_claims["password"]:
                MDApp.get_running_app().sm.current = "ScreenDash"
                lol.write(haha.uid)
            else:
                print("Invalid Credentials")

        except(ValueError):
            print("Invalid Credentials")
        except(firebase_admin._auth_utils.UserNotFoundError):
            print("L")

        lol.close()



class ScreenSignup(MDScreen):
    def signup2(self, username, password):
        lol = open(file="id.txt", mode='r+')

        try:
            user = auth.create_user(email = username, password = password)
            print("done {0}".format(user.uid))
            lol.write(user.uid)
            message = hashlib.sha3_256(password.encode("utf-8")).hexdigest()
            
            auth.set_custom_user_claims(uid=user.uid, custom_claims={"password": message})
            MDApp.get_running_app().sm.current = 'ScreenStartingInfo'
        
        except(ValueError):
            print("Invalid Credentials")
            
        except(firebase_admin.exceptions.InvalidArgumentError):
            print("Invalid mail or password")
        lol.close()

class ScreenStartingInfo(MDScreen):
    pass

class ScreenGoals(MDScreen):
    pass

class ScreenExperienceLevel(MDScreen):
    pass

class ScreenDash(MDScreen):
    pass

    

class Login(MDApp):
    

    
    
    
    def build(self):
        
        self.sm = ScreenManager()
        #sm = ObjectProperty()
        
        
        #screen_manager = WindowManager()
        #self.sm.add_widget(ScreenStart(name="ScreenStart"))
        self.sm.add_widget(ScreenMain(name="ScreenMain"))
        self.sm.add_widget(ScreenLogin(name="ScreenLogin"))
        self.sm.add_widget(ScreenSignup(name="ScreenSignup"))
        self.sm.add_widget(ScreenStartingInfo(name="ScreenStartingInfo"))
        self.sm.add_widget(ScreenGoals(name="ScreenGoals"))
        self.sm.add_widget(ScreenExperienceLevel(name="ScreenExperienceLevel"))
        self.sm.add_widget(ScreenDash(name="ScreenDash"))
        
        
        return self.sm
    
    
    
        
    
        
    # def login(self):
    #     pass
    
    # def signup2(self, username, password):
        
    #     try:
    #         user = auth.create_user(email = username, password = password)
    #         print("done {0}".format(user.uid))
    #         MDApp.get_running_app().scr.current = 'signup2'
            
    #     except:
    #         print("This account already exists. Try logging in.")
            
    # def signup(self, username, password):
    #     self.root.ids["login_scrs"].current = "signup2"
        
            
    
    
        
class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

    




    
if __name__ == "__main__":
    LabelBase.register(name='Tesla',
                   fn_regular='TESLA.ttf')
    Login().run()

    lol = open(file="id.txt", mode='r+')
    lol.truncate(0)
    lol.close()