from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.behaviors import DragBehavior
from kivy.uix.floatlayout import FloatLayout

class DraggableButton(DragBehavior, Button):
    pass

class Kurdappbuilder(App):
    def build(self):
        layout = FloatLayout()
        
        # دروستکردنی دوگمەیەکی تاقیکردنەوە کە دەتوانرێت ڕابکێشرێت
        btn = DraggableButton(
            text="Drag Me!",
            size_hint=(None, None),
            size=(200, 100),
            pos=(200, 200),
            background_color=(0, 0.5, 1, 1)
        )
        
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    Kurdappbuilder().run()
