import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

class Layout(QWidget):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton('1')
        self.button2 = QPushButton('2')
        self.button3 = QPushButton('3')
        self.button4 = QPushButton('4')
        self.button5 = QPushButton('5')
        self.button6 = QPushButton('6')
        self.button7 = QPushButton('7')
        self.button8 = QPushButton('8')
        self.button9 = QPushButton('9')
        self.button0 = QPushButton('0')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Layout()

    layout = QGridLayout()
    # レイアウトにウィジェットを追加
    layout.addWidget(window.button1, 0,1)
    layout.addWidget(window.button2, 0,2)
    layout.addWidget(window.button3, 0,3)
    layout.addWidget(window.button4, 1,1)
    layout.addWidget(window.button5, 1,2)
    layout.addWidget(window.button6, 1,3)
    layout.addWidget(window.button7, 2,1)
    layout.addWidget(window.button8, 2,2)
    layout.addWidget(window.button9, 2,3)
    layout.addWidget(window.button0, 3,2)



    # ウィジェットにレイアウトをセット
    window.setLayout(layout)

    window.show()
    sys.exit(app.exec_())
