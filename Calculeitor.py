from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math

class CalculatorApp(App):
    def build(self):
        self.operators = ["+", "-", "*", "/", "^", "%"]
        self.specials = ["C", "√", "sin", "cos", "tan", "="]
        self.last_was_operator = None
        self.last_button = None
        self.solution = TextInput(font_size=72, readonly=True, halign="right", multiline=False, size_hint=(1, None), height=120)
        self.current_input = TextInput(font_size=32, readonly=True, halign="right", multiline=False, size_hint=(1, None), height=120)
        
        main_layout = GridLayout(rows=3, padding=10, spacing=10)
        
        main_layout.add_widget(self.current_input)
        main_layout.add_widget(self.solution)
        
        buttons = [
            ("7", [1, 1, 1, 1]), ("8", [1, 1, 1, 1]), ("9", [1, 1, 1, 1]), ("/", [0.7, 0.7, 0.7, 1]),
            ("4", [1, 1, 1, 1]), ("5", [1, 1, 1, 1]), ("6", [1, 1, 1, 1]), ("*", [0.7, 0.7, 0.7, 1]),
            ("1", [1, 1, 1, 1]), ("2", [1, 1, 1, 1]), ("3", [1, 1, 1, 1]), ("-", [0.7, 0.7, 0.7, 1]),
            ("C", [1, 0, 0, 1]), ("0", [1, 1, 1, 1]), (".", [1, 1, 1, 1]), ("+", [0.7, 0.7, 0.7, 1]),
            ("sin", [0.5, 0.5, 1, 1]), ("cos", [0.5, 0.5, 1, 1]), ("tan", [0.5, 0.5, 1, 1]), ("√", [0.5, 0.5, 1, 1]),
            ("^", [0.7, 0.7, 0.7, 1]), ("%", [0.7, 0.7, 0.7, 1]), ("=", [0, 1, 0, 1])
        ]
        
        button_grid = GridLayout(cols=4, spacing=10)
        
        for (text, color) in buttons:
            btn = Button(text=text, pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=color)
            btn.bind(on_press=self.on_button_press)
            button_grid.add_widget(btn)
        
        main_layout.add_widget(button_grid)
        
        return main_layout

    def on_button_press(self, instance):
        current = self.current_input.text
        button_text = instance.text

        if button_text == "C":
            self.current_input.text = ""
            self.solution.text = ""
        elif button_text == "=":
            try:
                self.solution.text = str(eval(self.current_input.text))
            except Exception:
                self.solution.text = "Error"
        elif button_text == "%":
            try:
                self.solution.text = str(float(current) / 100)
            except Exception:
                self.solution.text = "Error"
        elif button_text in self.operators:
            if self.last_was_operator is None:
                self.current_input.text += button_text
            elif self.last_was_operator:
                return
            else:
                self.current_input.text += button_text
            self.last_was_operator = True
        elif button_text in ["sin", "cos", "tan", "√"]:
            try:
                if button_text == "sin":
                    self.solution.text = str(math.sin(math.radians(float(current))))
                elif button_text == "cos":
                    self.solution.text = str(math.cos(math.radians(float(current))))
                elif button_text == "tan":
                    self.solution.text = str(math.tan(math.radians(float(current))))
                elif button_text == "√":
                    self.solution.text = str(math.sqrt(float(current)))
            except Exception:
                self.solution.text = "Error"
        else:
            if current == "0":
                self.current_input.text = button_text
            else:
                self.current_input.text += button_text
            self.last_was_operator = False

        self.current_input.text = self.current_input.text
        self.last_button = button_text

if __name__ == "__main__":
    CalculatorApp().run()
