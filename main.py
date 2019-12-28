from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5 import uic
import sys


class MainWidget(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.btn = QPushButton('Рисовать', self)
        self.btn.move(200, 200)


class MyWidget(MainWidget, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.btn.clicked.connect(self.run)
        self.color = QColor('yellow')

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            for i in range(randint(1, 10)):
                qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
                r = randint(1, 100z)
                qp.drawEllipse(randint(0, 501), randint(0, 501), r, r)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.exit(app.exec_())
