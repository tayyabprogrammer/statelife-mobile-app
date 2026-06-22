from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDTextButton
from kivy.metrics import dp

class MyLoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = MDBoxLayout(orientation='vertical', padding=dp(30), spacing=dp(20))
        
        title_label = MDLabel(
            text="Sign In", halign="center", font_style="H4", bold=True,
            size_hint_y=None, height=dp(60)
        )
        layout.add_widget(title_label)
        
        form_layout = MDBoxLayout(orientation='vertical', spacing=dp(15), size_hint_x=0.9, pos_hint={"center_x": 0.5})
        
        self.email_input = MDTextField(hint_text="Email Address", icon_left="email", mode="round")
        form_layout.add_widget(self.email_input)
        
        self.password_input = MDTextField(hint_text="Password", icon_left="key", password=True, mode="round")
        form_layout.add_widget(self.password_input)
        
        login_btn = MDRaisedButton(text="LOG IN", font_style="Button", size_hint_x=1, pos_hint={"center_x": 0.5}, height=dp(50))
        form_layout.add_widget(login_btn)
        layout.add_widget(form_layout) 
        
        signup_layout = MDBoxLayout(orientation='horizontal', size_hint_y=None, height=dp(30))
        signup_layout.add_widget(MDLabel(text="Don't have an account?", halign="right", theme_text_color="Secondary"))
        
        signup_btn = MDTextButton(
            text=" Sign Up", theme_text_color="Custom", text_color=self.theme_cls.primary_color, bold=True,
            on_release=self.go_to_signup
        )
        signup_layout.add_widget(signup_btn)
        layout.add_widget(signup_layout)
        
        self.add_widget(layout)

    def go_to_signup(self, instance):
        self.manager.current = "signup"
        self.manager.transition.direction = "left"