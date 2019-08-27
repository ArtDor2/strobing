# this is a software-based black frame insertion overlay drawer to reduce motion blur in 60-fps locked content on 120hz+ monitors.

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CustomWindow(QMainWindow):
    def paintEvent(self, event=None):
        painter = QPainter(self)

        for n, in range(10000):
            if n % 2 == 0:
                painter.setOpacity(1)
                painter.setBrush(Qt.black)
                painter.setPen(QPen(Qt.black))   
                painter.drawRect(self.rect())
            else:
                painter.setOpacity(0)
                painter.setBrush(Qt.black)
                painter.setPen(QPen(Qt.black))   
                painter.drawRect(self.rect())


app = QApplication(sys.argv)

# Create the main window
window = CustomWindow()

window.setWindowFlags(Qt.FramelessWindowHint)
window.setAttribute(Qt.WA_NoSystemBackground, True)
window.setAttribute(Qt.WA_TranslucentBackground, True)

# Create the button
pushButton = QPushButton(window)
pushButton.setGeometry(QRect(240, 190, 90, 31))
pushButton.setText("Finished")
pushButton.clicked.connect(app.quit)

# Center the button
qr = pushButton.frameGeometry()
cp = QDesktopWidget().availableGeometry().center()
qr.moveCenter(cp)
pushButton.move(qr.topLeft())

# Run the application
window.showFullScreen()
sys.exit(app.exec_())