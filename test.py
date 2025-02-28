import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QPoint
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Случайные окружности")
        self.setGeometry(100, 100, 800, 600)
        self.pushButton = QPushButton("Добавить окружность", self)
        self.pushButton.clicked.connect(self.draw_circle)
        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.circles = []

    def draw_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            x, y, diameter, color = circle
            painter.setBrush(color)
            painter.drawEllipse(QPoint(x + diameter // 2, y + diameter // 2), diameter // 2, diameter // 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())