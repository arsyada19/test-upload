from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout

app = QApplication([])

my_win = QWidget()
my_win.setWindowTitle('Aplikasi pertama')
my_win.move(900, 70)
my_win.resize(400,200)
my_win.show()

line = QHBoxLayout()
judul = QLabel('Halo Dunia')

app.exec_()