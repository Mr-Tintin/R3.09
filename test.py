import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setGeometry(100, 100, 200, 300)
    window.setWindowTitle("My Simple GUI")

    layout = QVBoxLayout()

    label = QLabel("Choose your nickname")
    text = QTextEdit()
    button = QPushButton("Press ME!")
    button.clicked.connect(lambda: on_clicked(text.toPlainText()))
    layout.addWidget(label)
    layout.addWidget(text)
    layout.addWidget(button)
    window.setLayout(layout)
    window.show()
    app.exec_()
def on_clicked(msg):
    message = QMessageBox()
    message.setText(msg)
    message.exec_()

if __name__ == '__main__':
    main()