import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('Шестая программа')

        self.lineed = QLineEdit(self)
        self.lineed.resize(self.lineed.sizeHint())
        self.lineed.setGeometry(20, 40, 130, 50)

        self.lineed2 = QLineEdit(self)
        self.lineed2.resize(self.lineed2.sizeHint())
        self.lineed2.setGeometry(175, 40, 130, 50)

        self.linedname = QLabel(self)
        self.linedname.setText("Веведите координаты")
        self.linedname.setGeometry(20, 15, 130, 30)

        self.linedname2 = QLabel(self)
        self.linedname2.setText("Веведите масштаб")
        self.linedname2.setGeometry(175, 15, 130, 30)

        self.btn = QPushButton(self)
        self.btn.setText("Найти")
        self.btn.setGeometry(120, 100, 90, 30)
        self.btn.clicked.connect(self.share)

        self.linedname4 = QLabel(self)
        self.linedname4.setGeometry(100, 170, 500, 30)
        self.image = QLabel(self)

    def share(self):
        coords = self.lineed.text()
        mash = self.lineed2.text()
        api_server = "http://static-maps.yandex.ru/1.x/"
        params = {
            "ll": ",".join([coords]),
            "spn": ",".join([mash, mash]),
            "l": "map"
        }
        response = requests.get(api_server, params=params)

        self.map_file = "map.jpg"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        self.pixmap = QPixmap(self.map_file)
        self.image.move(120, 150)
        self.image.resize(250, 250)
        self.image.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            mash += 0.5
        if event.key() == Qt.Key_PageDown:
            mash -= 0.5

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
