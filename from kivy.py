from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.progressbar import ProgressBar

from kivy.clock import Clock

from kivy.animation import Animation

btn_color = (0.98, 0.31, 0.8, 1)
class InputScreen (Screen):
def __init__(self, **kwargs):
super().__init__(**kwargs)
self.layout
=
BoxLayout (orientation = "vertical', spacing=10')
#menu untuk input data
self.label_alas
self.input_alas
=
Label(text='Masukkan panjang alas:') TextInput(multiline=False)
self.label_tinggi = Label(text='Masukkan tinggi segitiga:') self.input_tinggi = Text Input (multiline=False)
#menu menampilkan data yang diinput

self.layout.add_widget(self.label_alas)
self.layout.add_widget(self.input_alas)

self.layout.add_widget(self.label_tinggi)
28
self.layout.add_widget(self.input_tinggi)
2

self.calculate_button
=
Button(text='Hitung Luas Segitiga')




self.calculate_button.bind(on_press=self.calculate_area)
self.layout.add_widget(self.calculate_button)
self.result_label = Label(text='') self.layout.add_widget(self.result_label)
self.add_widget(self.layout)
def calculate_area(self, instance):
try:
alas = float(self.input_alas.text) tinggi
=
luas = 0.5 * alas * tinøøi
float(self.input_tinggi.text)
> ValueError


luas
=

=
'result'
alas = float(self.input_alas.text)
tinggi
=
float(self.input_tinggi.text)
0.5 * alas * tinggi
self.result_label.text = f'Luas Segitiga: {luas}'
self.manager.get_screen('result').start_progress_animation() # Panggil metode di layar result
self.manager.current

Clock.schedule_once(self.stop_progress, 5)

except ValueError:

self.result_label.text
=
'Masukkan angka yang valid'

=
'input'
def stop_progress(self, *args):
self.manager.get_screen('result').stop_progress_animation()
self.manager.current

class ResultScreen (Screen):

= None

def __init__(self, **kwargs):
super().__init__(**kwargs)
self.layout
=
BoxLayout (orientation='vertical', spacing=10)
self.result_label = Label(text='Memproses menghitung luas segitiga') self.progress_bar = ProgressBar(max=100, value=0)
self.layout.add_widget(self.result_label) self.layout.add_widget(self.progress_bar)
self.add_widget(self.layout)
self.anim = None # Menyimpan referensi ke animasi
def on_enter(self, *args):
pass
def start_progress_animation(self): self.progress_bar.value = 0
self.anim = Animation(value=100, max=100, duration=5) self.anim.start(self.progress_bar)
def stop_progress_animation(self):
if self.anim:
self.anim.cancel(self.progress_bar)
self.anim
self.progress_bar.value = 0


class TriangleApp (App):

def build(self):


sm = ScreenManager() input_screen
=
InputScreen(name='input')

51 ✓ • 52
def stop_progress (self, *args):
self.manager.get_screen('result').stop_progress_animation()
self.manager.current
'input'
def __init__(self, **kwargs):
super().__init__(**kwargs)
=
BoxLayout (orientation='vertical', spacing=10)
self.layout self.result_label
=

class ResultScreen (Screen):

self.progress_bar


Label(text='Memproses menghitung luas segitiga') ProgressBar(max=100, value=0)
self.layout.add_widget(self.result_label) self.layout.add_widget(self.progress_bar)
self.add_widget(self.layout)
self.anim = None # Menyimpan referensi ke animasi
def on_enter(self, *args):
pass
def start_progress_animation(self):
self.progress_bar.value = 0
self.anim =
Animation(value=100, max=100, duration=5)
self.anim.start(self.progress_bar)
def stop_progress_animation(self):
if self.anim:
self.anim.cancel(self.progress_bar)
self.anim
=
None
self.progress_bar.value
if
name
____main__'

TriangleApp().run()

class TriangleApp (App):
def build(self):
sm = ScreenManager()
input_screen
result_screen

InputScreen (name='input')
ResultScreen (name='result')
sm.add_widget(input_screen)
sm.add_widget(result_screen)
return sm