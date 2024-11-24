
1 import kivy
3 from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
2
from kivy.app import App
4
from kivy.uix.label import Label
5
6
from kivy.uix.text input import TextInput
7
8
10
11
from kivy.uix.spinner import Spinner
kivy.require('2.1.0')
12 class TemperatureConverter(BoxLayout):
13 ▼
14
15
16
17
18
19
20
21
22
23
24
25
26 ✓
27
28
DERELLA 22 2 2 2 2 2 2 2 2 2 2 2☹****
29
30
<
def __init__(self, **kwargs):
super(TemperatureConverter, self).__init__(**kwargs)
self.orientation = 'vertical'
# Label to prompt the user
self.label = Label(text='Masukkan suhu:') self.add_widget(self.label)
# Text input field for the temperature self.input = TextInput(text='', multiline=False) self.add_widget(self.input)
# Spinner (dropdown) to select the conversion type self.spinner = Spinner(
text='Pilih Suhu',
values=('Celcius ke Fahrenheit', 'Celcius ke Kelvin',
'Fahrenheit ke Celcius', 'Fahrenheit ke Kelvin', 'Kelvin ke Celcius', 'Kelvin ke Fahrenheit')
self.add_widget(self.spinner)
# Button to trigger conversion
31
>
32
33
34
35
36
37
38
self.button = Button(text='Konversi')
self.button.bind(on_press=self.convert_temperature)
self.add_widget(self.button)