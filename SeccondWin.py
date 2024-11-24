from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class SeccondWin (QWidget):
    def __init__(self):
        super().__init__()
        self.setAppear()
        self.initUI()
        # self.connect()
        self.show()

    def setAppear(self):
        self.setWindowTitle("Ruffler Test")
        self.resize(700,500)

    def timertest(self):
        global time
        time = QTime(0,0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1000)

    def  Timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.timerlabel.setText(time.toString("hh:mm:ss"))
        self.timerlabel.setFont(QFont("Times"), 36, QFont.Bold)
        self.timerlabel.setStyleSheet("Color rgo: (0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()


    def connects(self):
        self.buttontest1.clicked.connect(self.timerEvent1)



    def initUI(self):
        #1st
        self.label1 = QLabel("Enter your full name:")
        self.nameedit = QTextEdit("Full name")
        #2nd
        self.label2 = QLabel("Enter your age:")
        self.ageedit = QTextEdit("Age")

        #1st test
        self.instruction1 = QLabel("Lie on your back and take your pulse for 15 seconds. Click the Start first test button to start the timer.\nWrite down the result in the appropriate field.")
        self.buttontest1 = QPushButton("Start first test")
        self.result1 = QTextEdit("0")

        #2nd test
        self.instruction2 = QLabel("Perform 30 squats in 45 seconds. To do this, click the Start doing squats button\nto start the squat counter")
        self.buttontest2 = QPushButton("Start doing squats")
        self.result2 = QTextEdit("0")

        #3rd test
        self.instruction3 = QLabel("Lie on your back and take your pulse for the first 15 seconds of the minute, then for the last 15 seconds of the minute.\nPress the Start final test button to start the timer.\nThe seconds that should be measured are indicated in green and the seconds that should not be measured are indicated in black. Write down the results in the appropriate fields.")
        self.buttontest3 = QLabel("Start final test")
        self.result3 = QTextEdit("0")

        #timer
        self.timerlabel = QLabel("00:00:00")

        #layout
        self.layout1 = QHBoxLayout()


        #Connect Layout
        self.hlayout.addWidget(self.label1, alignment=Qt.AlignCenter)
        self.hlayout.addWidget(self.label2, alignment=Qt.AlignCenter)
        self.hlayout.addWidget(self.lined, alignment=Qt.AlignCenter)
        self.hlayout.addWidget(self.button, alignment=Qt.AlignCenter)

        self.setLayout(self.layout)




        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.label1)
        self.mainlayout.addWidget(self.nameedit)
        self.mainlayout.addWidget(self.labelage)
        self.mainlayout.addWidget(self.ageedit)
        self.mainlayout.addWidget(self.instruction1)
        self.mainlayout.addWidget(self.buttontest1)
        self.mainlayout.addWidget(self.result1)
        self.mainlayout.addWidget(self.instruction2)

        self.mainlayout.addLayout(self.buttontest2), alignment == Qt.AlignLeft
        self.mainlayout.addLayout(self.timerlabel), alignment == Qt.AlignRight
        self.mainlayout.addLayout(self.hlayout)


        self.mainlayout.addWidget(self.buttontest2)
        self.mainlayout.addWidget(self.result2)
        self.mainlayout.addWidget(self.instruction3)
        self.mainlayout.addWidget(self.buttontest3)
        self.mainlayout.addWidget(self.result3)


