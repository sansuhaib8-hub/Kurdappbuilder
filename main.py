from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

# ڕەنگی پێشینەی گشتی تاریک
Window.clearcolor = (0.05, 0.06, 0.1, 1)

class KurdAppBuilder(App):
    def build(self):
        # لایەوتی سەرەکی (ستونی)
        root_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # ----------------- پانێڵی سەرەوە (TOP BAR) -----------------
        top_bar = BoxLayout(orientation='horizontal', size_hint_y=0.1, spacing=10)
        
        title_label = Label(
            text="[b]Kurdappbuilder[/b]  project: KURDCONNECT", 
            markup=True, 
            color=(0, 0.8, 1, 1),
            font_size='18sp',
            size_hint_x=0.6,
            halign='left'
        )
        top_bar.add_widget(title_label)
        
        run_btn = Button(text="▶ Run", size_hint_x=0.15, background_color=(0, 0.6, 0.8, 1))
        deploy_btn = Button(text="🚀 Deploy", size_hint_x=0.15, background_color=(0, 0.8, 0.4, 1))
        
        top_bar.add_widget(run_btn)
        top_bar.add_widget(deploy_btn)
        root_layout.add_widget(top_bar)
        
        # ----------------- بەشی ناوەڕاست (MAIN BODY) -----------------
        main_body = BoxLayout(orientation='horizontal', size_hint_y=0.9, spacing=10)
        
        # لایەنی چەپ: لیستی پێکهاتەکان
        left_sidebar = BoxLayout(orientation='vertical', size_hint_x=0.2, spacing=5)
        left_sidebar.add_widget(Label(text="[b]LAYOUT[/b]", markup=True, color=(0, 0.8, 1, 1), size_hint_y=0.1))
        left_sidebar.add_widget(Button(text="Text Component", size_hint_y=0.15, background_color=(0.1, 0.15, 0.25, 1)))
        left_sidebar.add_widget(Button(text="Button Component", size_hint_y=0.15, background_color=(0.1, 0.15, 0.25, 1)))
        left_sidebar.add_widget(Button(text="List Component", size_hint_y=0.15, background_color=(0.1, 0.15, 0.25, 1)))
        left_sidebar.add_widget(Widget()) 
        
        # ناوەڕاست: شوێنی مۆبایلە ساختەکە (WORKSPACE)
        workspace = FloatLayout(size_hint_x=0.5)
        
        phone_screen = BoxLayout(
            orientation='vertical',
            size_hint=(None, None),
            size=(240, 420),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        # شێوازی دروستی ڕەنگکردنی پاشبنەمای BoxLayout لە ڕێگەی Canvas
        with phone_screen.canvas.before:
            Color(0.02, 0.03, 0.05, 1)
            phone_rect = Rectangle(pos=phone_screen.pos, size=phone_screen.size)
            
        # بەستنەوەی قەبارەی ڕەنگەکە بە قەبارەی شاشەکەوە تا تێک نەچێت
        phone_screen.bind(
            pos=lambda obj, val: setattr(phone_rect, 'pos', val),
            size=lambda obj, val: setattr(phone_rect, 'size', val)
        )
        
        phone_screen.add_widget(Label(text="KurdConnect Phone Frame", color=(0.5, 0.5, 0.5, 1)))
        workspace.add_widget(phone_screen)
        
        # لایەنی ڕاست: پانێڵی تایبەتمەندییەکان
        right_sidebar = BoxLayout(orientation='vertical', size_hint_x=0.3, spacing=5)
        right_sidebar.add_widget(Label(text="[b]PROPERTIES[/b]", markup=True, color=(0, 0.8, 1, 1), size_hint_y=0.1))
        right_sidebar.add_widget(Label(text="ID: btn_send", halign='left', size_hint_y=0.1))
        right_sidebar.add_widget(Label(text="Type: Button", halign='left', size_hint_y=0.1))
        right_sidebar.add_widget(Label(text="Style: Neon Glow", halign='left', size_hint_y=0.1))
        right_sidebar.add_widget(Widget()) 
        
        main_body.add_widget(left_sidebar)
        main_body.add_widget(workspace)
        main_body.add_widget(right_sidebar)
        
        root_layout.add_widget(main_body)
        return root_layout

if __name__ == "__main__":
    KurdAppBuilder().run()
