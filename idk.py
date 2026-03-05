import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import QRect

class AboutMe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.k = 1

    def initUI(self):
        self.setGeometry(400, 200, 700, 700)
        self.setWindowTitle('Обо мне')
        self.box = QVBoxLayout()
        self.box.setGeometry(QRect(400, 200, 600, 600))
        self.label1 = QLabel(self)
        self.label1.setText("Боришпольский Ян Андреевич")
        self.label1.setGeometry(250, 0, 500, 100)
        self.label2 = QLabel(self)
        self.label2.setText("Бывший ученик ГБОУ школы 1517")
        self.label2.setGeometry(250, 100, 500, 100)
        self.button = QPushButton("Изменить", self)
        self.button.move(0, 0)
        self.button.clicked.connect(self.change)
        self.box.addWidget(self.label1)
        self.box.addWidget(self.label2)
        self.box.addWidget(self.button)

    
    def change(self):
        if self.label2.text() == "Хочет спать":
            self.label2.setText("Бывший ученик ГБОУ школы 1517")
        else:
            self.label2.setText("Хочет спать")

        x = self.button.x()
        y = self.button.y()
        i = (x // 50 + self.k)
        if x > self.width() - 2 * self.button.width() or y > self.height() - 2 * self.button.height():
            self.k = -1
        elif x - self.button.width() < 0 or y - self.button.height() < 0:
            self.k = 1
        self.button.move(i * 50, i * 50)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Am = AboutMe()
    Am.show()
    sys.exit(app.exec())