from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.metrics import dp
from kivy.core.window import Window

class CalculatorApp(App):
    def build(self):
        screen_width, screen_height = Window.size

        font_size = dp(screen_width * 0.1)

        self.operand = ""
        self.result = TextInput(font_size=font_size, readonly=True, halign="right", multiline=False)

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(self.result)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=font_size, on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        self.secret_menu = BoxLayout(orientation='vertical', spacing=5, padding=10)
        self.secret_menu.add_widget(Label(text="Label 1", font_size=font_size/2))
        self.secret_menu.add_widget(Label(text="Label 2", font_size=font_size/2))

        for i in range(1, 11):
            self.secret_menu.add_widget(Button(text=f"Button {i}", font_size=font_size/3))

        self.secret_menu.opacity = 0  # Hide initially
        self.secret_menu.size_hint_y = None
        self.secret_menu.height = 0
        layout.add_widget(self.secret_menu)

        return layout

    def show_secret_menu(self):
        self.root.clear_widgets()
        self.root.add_widget(self.secret_menu)
        self.secret_menu.opacity = 1
        self.secret_menu.size_hint_y = 1
        self.secret_menu.height = self.secret_menu.minimum_height

    def on_button_press(self, instance):
        text = instance.text
        if text == "C":
            self.operand = ""
        elif text == "=":
            try:
                self.operand = str(eval(self.operand))
                if self.operand == "109296":
                    self.operand = "Welcome"
                    print("PASSWORD RECEIVED")
                    self.show_secret_menu()
            except Exception:
                self.operand = "Error"
        else:
            self.operand += text

        self.result.text = self.operand


if __name__ == "__main__":
    CalculatorApp().run()
