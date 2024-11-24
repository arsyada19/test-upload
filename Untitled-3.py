from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class MainWin (QWidget):
    def _init_(self):
        super()._init_()
        self.setAppear()
        self.initUI()
        # self.connect()
        self.show()

    def setAppear(self):
        self.setWindowTitle("Ruffler Test")
        self.resize(700,500)

    def initUI(self):
        self.b1 = QPushButton("next")
        self.t1 = QLabel('This application allows you to use the Rufier test to make an initial diagnosis of your health.\n'
                   'The Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion.\n'
                   'The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds; \n'
                   'then, within 45 seconds, the subject performs 30 squats.\n'
                   'When the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds\n'
                   'and then for the last 15 seconds of the first minute of the recovery period.\n'
                   'Important! If you feel unwell during the test (dizziness,\n'
                   'tinnitus, shortness of breath, etc.), stop the test and consult a physician.')

        #layout
        self.main_layout = QVBoxLayout()
        self.hlayout1 = QHBoxLayout()
        self.hlayout2 = QHBoxLayout()
        self.hlayout3 = QHBoxLayout()

        self.hlayout1.addWidget(self.t1)
        self.hlayout2.addWidget(self.b1)

        self.main_layout.addLayout(self.hlayout1)
        self.main_layout.addLayout(self.hlayout2)

        self.setLayout(self.main_layout)

    # #def connect(self):
    #     self.b1.clicked.connect(self.nextclick)
    # #def nexclick(self):
    #     self.SecondWin = SecondWin()
    #     self.hide()


#Object
app = QApplication([])
window = MainWin()
app.exec_()