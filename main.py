from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Line

# ڕەنگی پێشینەی تاریکی سایبەرپەنک
Window.clearcolor = (0.02, 0.03, 0.06, 1)

class CyberPanel(BoxLayout):
    """پانێڵێکی تایبەت بە ڕەنگی پاشبنەمای تاریک و هێڵی دەوروبەری نیۆن"""
    def __init__(self, border_color=(0, 0.5, 0.8, 1), bg_color=(0.04, 0.06, 0.12, 0.7), **kwargs):
        super().__init__(**kwargs)
        self.border_color = border_color
        self.bg_color = bg_color
        with self.canvas.before:
            Color(*self.bg_color)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            Color(*self.border_color)
            self.border = Line(rectangle=(self.x, self.y, self.width, self.height), width=1.2)
        self.bind(pos=self._update_canvas, size=self._update_canvas)

    def _update_canvas(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.border.rectangle = (self.x, self.y, self.width, self.height)

class WorkspaceGrid(FloatLayout):
    """شوێنی کارکردن کە هێڵکاری کاڵی شینی نیۆنی تێدایە وەک وێنەکە"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(size=self._draw_grid, pos=self._draw_grid)

    def _draw_grid(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 0.6, 1, 0.08) # هێڵی زۆر کاڵی شین
            step = 35
            # هێڵە ستوونییەکان
            for x in range(int(self.x), int(self.x + self.width), step):
                Line(points=[x, self.y, x, self.y + self.height], width=1)
            # هێڵە ئاسۆییەکان
            for y in range(int(self.y), int(self.y + self.height), step):
                Line(points=[self.x, y, self.x + self.width, y], width=1)

class CyberButton(Button):
    """دوگمەی ستایلی سایبەرپەنک بە هێڵکاری دەوروبەر"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0.06, 0.1, 0.18, 1)
        self.color = (0, 0.8, 1, 1)
        self.bold = True
        with self.canvas.after:
            Color(0, 0.6, 0.9, 0.4)
            self.border = Line(rectangle=(self.x, self.y, self.width, self.height), width=1)
        self.bind(pos=self._update_border, size=self._update_border)

    def _update_border(self, *args):
        self.border.rectangle = (self.x, self.y, self.width, self.height)

class KurdAppBuilder(App):
    def build(self):
        # ١. لایەوتی سەرەکی گشتی
        root_layout = BoxLayout(orientation='vertical', padding=8, spacing=8)
        
        # ----------------- پانێڵی سەرەوە (TOP BAR) -----------------
        top_bar = BoxLayout(orientation='horizontal', size_hint_y=0.12, spacing=10)
        
        title_label = Label(
            text="[b]Kurdappbuilder[/b]  [color=00ffcc]project: KURDCONNECT (v1.0)[/color]", 
            markup=True, 
            color=(0, 0.8, 1, 1),
            font_size='16sp',
            size_hint_x=0.5,
            halign='left'
        )
        top_bar.add_widget(title_label)
        
        # دوگمەکانی سەرەوە بەبێ ئیمۆجی تێکچوو
        run_btn = Button(text="RUN", size_hint_x=0.12, bold=True, background_normal='', background_color=(0, 0.4, 0.6, 1))
        deploy_btn = Button(text="DEPLOY", size_hint_x=0.12, bold=True, background_normal='', background_color=(0, 0.6, 0.3, 1))
        settings_btn = Button(text="SETTINGS", size_hint_x=0.12, bold=True, background_normal='', background_color=(0.1, 0.15, 0.25, 1))
        
        top_bar.add_widget(run_btn)
        top_bar.add_widget(deploy_btn)
        top_bar.add_widget(settings_btn)
        root_layout.add_widget(top_bar)
        
        # ----------------- بەشی ناوەڕاست (MAIN BODY) -----------------
        main_body = BoxLayout(orientation='horizontal', size_hint_y=0.88, spacing=8)
        
        # لایەنی چەپ: LAYOUT PANEL
        left_sidebar = CyberPanel(orientation='vertical', size_hint_x=0.22, spacing=8, padding=10)
        left_sidebar.add_widget(Label(text="[b]LAYOUT[/b]", markup=True, color=(0, 0.8, 1, 1), size_hint_y=0.1))
        left_sidebar.add_widget(CyberButton(text="Text", size_hint_y=0.14))
        left_sidebar.add_widget(CyberButton(text="Button", size_hint_y=0.14))
        left_sidebar.add_widget(CyberButton(text="List", size_hint_y=0.14))
        left_sidebar.add_widget(Widget()) # بۆشایی
        
        # ناوەڕاست: WORKSPACE + PHONE FRAME
        workspace = WorkspaceGrid(size_hint_x=0.48)
        
        # دروستکردنی شاشەی مۆبایل بە قەبارەیەکی گونجاو و هێڵی درەوشاوە
        phone_screen = CyberPanel(
            border_color=(0, 0.9, 1, 1), # شینی نیۆنی ڕووناک
            bg_color=(0.01, 0.02, 0.04, 0.95),
            orientation='vertical',
            size_hint=(None, None),
            size=(260, 440),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            padding=8
        )
        phone_screen.add_widget(Label(text="KurdConnect", color=(0, 0.8, 1, 1), bold=True, size_hint_y=0.1))
        phone_screen.add_widget(Widget()) # ناوەڕۆکی ناو مۆبایلەکە
        workspace.add_widget(phone_screen)
        
        # لایەنی ڕاست: PROPERTIES PANEL
        right_sidebar = CyberPanel(orientation='vertical', size_hint_x=0.3, spacing=6, padding=10)
        right_sidebar.add_widget(Label(text="[b]PROPERTIES[/b]", markup=True, color=(0, 0.8, 1, 1), size_hint_y=0.1))
        
        right_sidebar.add_widget(Label(text="ID: btn_send", color=(0.7, 0.8, 0.9, 1), size_hint_y=0.1, halign='left'))
        right_sidebar.add_widget(Label(text="Type: Button", color=(0.7, 0.8, 0.9, 1), size_hint_y=0.1, halign='left'))
        right_sidebar.add_widget(Label(text="Style: Neon Glow", color=(0.7, 0.8, 0.9, 1), size_hint_y=0.1, halign='left'))
        right_sidebar.add_widget(Widget()) # بۆشایی
        
        # بەستنەوەی سێ پانێڵەکە بە جەستەی سەرەکی
        main_body.add_widget(left_sidebar)
        main_body.add_widget(workspace)
        main_body.add_widget(right_sidebar)
        
        root_layout.add_widget(main_body)
        return root_layout

if __name__ == "__main__":
    KurdAppBuilder().run()
