import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from math import pi

class LuasApp(App):
    def build(self):
        self.title = 'Perhitungan Luas'
        self.layout = BoxLayout(orientation='vertical', spacing=10)

        self.input_layout = BoxLayout(orientation='vertical', spacing=5)
        self.result_label = Label(text='', halign='center')

        self.layout.add_widget(Label(text="Masukkan bentuk geometri (Lingkaran/Segitiga/Persegi Panjang/Persegi/Jajargenjang):"))
        self.layout.add_widget(Label(text="Tulis dalam huruf kecil"))
        self.menu = TextInput(text='', multiline=False)
        self.input_layout.add_widget(self.menu)

        self.layout.add_widget(self.input_layout)
        self.calculate_button = Button(text="Hitung", size_hint=(None, None), size=(100, 50))
        self.calculate_button.bind(on_press=self.calculate)
        self.layout.add_widget(self.calculate_button)
        self.layout.add_widget(self.result_label)
        return self.layout

    def calculate(self, instance):
        shape = self.menu.text.lower()

        if shape == 'lingkaran' or 'Lingkaran' or 'LINGKARAN':
            self.input_layout.clear_widgets()
            self.input_layout.add_widget(Label(text="Masukkan jari-jari:"))
            self.radius_input = TextInput(multiline=False)
            self.input_layout.add_widget(self.radius_input)

        elif shape == 'segitiga' or 'Segitiga' or 'SEGITIGA':
            self.input_layout.clear_widgets()
            self.input_layout.add_widget(Label(text="Masukkan alas:"))
            self.base_input = TextInput(multiline=False)
            self.input_layout.add_widget(self.base_input)
            self.input_layout.add_widget(Label(text="Masukkan tinggi:"))
            self.height_input = TextInput(multiline=False)
            self.input_layout.add_widget(self.height_input)

        elif shape == 'persegi panjang':
            self.input_layout.clear_widgets()
            self.input_layout.add_widget(Label(text="Masukkan panjang:"))
            self.length_input = TextInput(multiline=False)
            self.input_layout.add_widget(self.length_input)
            self.input_layout.add_widget(Label(text="Masukkan lebar:"))
            self.width_input = TextInput(multiline=False)
            self.input_layout.add_widget(self.width_input)

        elif shape == 'jajargenjang':
            self.input_layout.clear_widgets()
            self.input_layout.add_widget(Label(text="Masukkan alas:"))
            self.base_input = TextInput(multiline=False)
            self.input_layout.add_widget(self.base_input)
            self.input_layout.add_widget(Label(text="Masukkan tinggi:"))
            self.height_input = TextInput(multiline=False)
            self.input_layout.add_widget(self.height_input)

        elif shape == 'persegi':
            self.input_layout.clear_widgets()
            self.input_layout.add_widget(Label(text="Masukkan sisi:"))
            self.side_input = TextInput(multiline=False)
            self.input_layout.add_widget(self.side_input)

        else:
            self.result_label.text = "Bentuk geometri tidak valid"
            return

        self.calculate_button.unbind(on_press=self.calculate)
        self.calculate_button.bind(on_press=self.calculate_area)

    def calculate_area(self, instance):
        shape = self.menu.text.lower()

        if shape == 'lingkaran' or 'Lingkaran' or 'Lingkaran':
            radius = float(self.radius_input.text)
            area = pi * radius ** 2
        elif shape == 'segitiga':
            base = float(self.base_input.text)
            height = float(self.height_input.text)
            area = 0.5 * base * height
        elif shape == 'persegi panjang':
            length = float(self.length_input.text)
            width = float(self.width_input.text)
            area = length * width
        elif shape == 'jajargenjang':
            base = float(self.base_input.text)
            height = float(self.height_input.text)
            area = base * height
        elif shape == 'persegi':
            side = float(self.side_input.text)
            area = side ** 2
        else:
            self.result_label.text = "Bentuk geometri tidak valid"
            return

        self.result_label.text = f"Luas {shape}: {area}"

if __name__ == '__main__':
    LuasApp().run()
