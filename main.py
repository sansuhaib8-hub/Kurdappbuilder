from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

# کڵاسی ئەو دوگمەیەی کە بەکارهێنەر دروستی دەکات و دەتوانێت ڕایبکێشێت
class BuildWidget(Button):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            # جوڵاندنی دوگمەکە ڕێک لە ژێر پەنجەی بەکارهێنەردا
            self.center_x = touch.x
            self.center_y = touch.y
            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            return True
        return super().on_touch_up(touch)

class KurdAppBuilder(App):
    def build(self):
        # ڕوکاری سەرەکی (ستایلی ستونی)
        main_layout = BoxLayout(orientation='vertical')
        
        # ١. پانێڵی کۆنتڕۆڵ (بۆ زیادکردنی پێکهاتەکان)
        control_panel = BoxLayout(size_hint_y=0.1, spacing=10, padding=10)
        
        # دوگمەی دروستکردنی توخمی نوێ
        add_btn = Button(
            text="Add Button (+)", 
            size_hint_x=0.4,
            background_color=(0, 0.6, 0.3, 1) # ڕەنگی سەوز
        )
        control_panel.add_widget(add_btn)
        
        # ٢. شوێنی کارکردن (Workspace) - کە فەزایەکی ئازادە
        workspace = FloatLayout()
        
        # لۆجیکی زیادکردنی دوگمەی نوێ بۆ سەر شاشەکە کاتێک کلیک لە Add دەکرێت
        def create_new_element(instance):
            new_widget = BuildWidget(
                text=f"Button {len(workspace.children) + 1}",
                size_hint=(None, None),
                size=(180, 65),
                pos=(Window.width / 2 - 90, Window.height / 2),
                background_color=(0, 0.4, 0.8, 1) # ڕەنگی شین
            )
            workspace.add_widget(new_widget)
            
        add_btn.bind(on_press=create_new_element)
        
        # بەستنەوەی بەشەکان بە ڕوکارە سەرەکیەکەوە
        main_layout.add_widget(control_panel)
        main_layout.add_widget(workspace)
        
        return main_layout

if __name__ == "__main__":
    KurdAppBuilder().run()
