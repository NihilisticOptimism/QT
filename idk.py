import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import QRect

class AboutMe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 200, 1000, 1000)
        self.setWindowTitle('Обо мне')
        self.box = QVBoxLayout(self)
        self.box.setGeometry(QRect(100, 100, 500, 600))
        self.label1 = QLabel(self)
        self.label1.setText("Боришпольский Ян Андреевич")
        self.label1.setGeometry(100, 100, 500, 100)
        self.label2 = QLabel(self)
        self.label2.setText("Бывший ученик ГБОУ школы 1517")
        self.label2.setGeometry(100, 300, 500, 100)
        self.button = QPushButton("Изменить", self)
        self.button.move(400, 200)
        self.button.clicked.connect(self.change)
        self.box.addWidget(self.label1)
        self.box.addWidget(self.label2)
        self.box.addWidget(self.button)

    def change(self):
        self.label2.setText("Хочет спать")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    Am = AboutMe()
    Am.show()
    sys.exit(app.exec())