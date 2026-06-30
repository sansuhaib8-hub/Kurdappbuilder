from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window

# پێشینەی تاریک
Window.clearcolor = (0.02, 0.03, 0.06, 1)

class KurdAppBuilder(App):
    def build(self):
        # لایەوتی سەرەکی سادە بۆ تاقیکردنەوەی ڕووناكی ئەپەکە
        root = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # نازناو
        title = Label(
            text="[b]Kurdappbuilder[/b] - Cyberpunk UI", 
            markup=True, 
            color=(0, 0.8, 1, 1),
            font_size='20sp',
            size_hint_y=0.2
        )
        root.add_widget(title)
        
        # ناوەڕۆک
        body = BoxLayout(orientation='horizontal', size_hint_y=0.6, spacing=10)
        
        left_panel = Button(text="Layout Panel", background_color=(0.05, 0.1, 0.2, 1), color=(0, 0.8, 1, 1))
        center_panel = Button(text="Phone Workspace", background_color=(0.01, 0.02, 0.04, 1), color=(0, 0.9, 1, 1))
        right_panel = Button(text="Properties", background_color=(0.05, 0.1, 0.2, 1), color=(0, 0.8, 1, 1))
        
        body.add_widget(left_panel)
        body.add_widget(center_panel)
        body.add_widget(right_panel)
        root.add_widget(body)
        
        # خوارەوە
        footer = Button(text="RUN / DEPLOY", size_hint_y=0.2, background_color=(0, 0.5, 0.4, 1))
        root.add_widget(footer)
        
        return root

if __name__ == "__main__":
    KurdAppBuilder().run()
