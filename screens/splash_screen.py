from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

class MySplashScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # 1. Background ko pure WHITE kar diya (RGB: 1, 1, 1)
        self.md_bg_color = (1, 1, 1, 1) 
        
        layout = MDBoxLayout(orientation='vertical', padding="20dp")
        

        logo_label_head = MDLabel(
            text="STATE LIFE",
            halign="center",          
            valign="middle",          
            theme_text_color="Custom",
            text_color=(0, 0.28, 0.67, 1),      
            font_style="H3",               # H4 thoda bara tha, H5 clean dikhega
            bold=True
        )
        logo_label = MDLabel(
            text="\nINSURANCE CORPORATION OF PAKISTAN",
            halign="center",          
            valign="middle",          
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),       # Pure Black Text
            font_style="H5",               # H4 thoda bara tha, H5 clean dikhega
            bold=True
        )
        
        # 3. Ek choti si decorative BLUE layer (line/bar) text ke niche
        # Yeh aapki "JUST SOME LAYER BLUE" wali requirement poori karegi
        blue_bar = MDBoxLayout(
            size_hint=(None, None),
            size=("150dp", "5dp"),        # Width: 150dp, Height: 5dp
            pos_hint={"center_x": 0.5},   # Screen ke center mein line lane ke liye
            md_bg_color=(0, 0.28, 0.67, 1) # Corporate Blue Color
        )
        
        # Widgets ko order mein add kiya (Pehle text, phir line)
        layout.add_widget(logo_label_head)
        layout.add_widget(logo_label) 
        layout.add_widget(blue_bar)
        
        # Extra spacing management taake line text ke bilkul sath perfect lage
        layout.spacing = "20dp"
        
        self.add_widget(layout)