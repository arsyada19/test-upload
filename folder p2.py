folder p1

from PyQt5.QtCore import Qt, QTimer, QTime,QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QHBoxLayout, QVBoxLayout,
                             QGridLayout, QGroupBox,
                             QRadioButton, QPushButton,
                             QLabel, QListWidget, QLineEdit)

from p1 import *

class MainWin(QWidget):
    def _init_(self):
        super()._init_()
        self.set_appear()# mengatur seperti apa tampilan jendela
        self.initUI() # membuat dan mengkonfigurasi elemen grafis
        self.connects() # membangun hubungan antar elemen
        self.show() # start

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(text_instruction)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

app = QApplication([])
mw = MainWin()
app.exec_()
