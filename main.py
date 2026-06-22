from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.clock import Clock  
from screens.splash_screen import MySplashScreen
from screens.login_screen import MyLoginScreen
from screens.signup_screen import MySignupScreen

class MainAuthApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"

        self.screen_manager = MDScreenManager()

        # Screens ko initialize kar ke manager mein add karna
        splash = MySplashScreen(name="splash")
        login = MyLoginScreen(name="login")
        signup = MySignupScreen(name="signup") 

        self.screen_manager.add_widget(splash)
        self.screen_manager.add_widget(login)
        self.screen_manager.add_widget(signup) 

        return self.screen_manager

    def on_start(self):
        Clock.schedule_once(self.go_to_login, 3)

    def go_to_login(self, dt):
        self.screen_manager.current = "login"

if __name__ == "__main__":
    MainAuthApp().run()