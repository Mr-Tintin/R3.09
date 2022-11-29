import socket
import threading

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'TEST'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        
        self.show()
    
class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Tab 1")
        #self.tabs.addTab(self.tab2,"Tab 2")
        
        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.sh_srv = QComboBox()
        self.sh_srv.addItem("Serveur_1")
        self.sh_srv.addItem("Serveur_2")
        self.sh_srv.addItem("Serveur_3")
        self.__ok = QPushButton("Ok")
        self.__ok.clicked.connect(self.choix_du_serveur)
        self.tab1.layout = QVBoxLayout(self)
        self.tab1.layout.addWidget(self.sh_srv)
        self.tab1.layout.addWidget(self.__ok)
        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def creat_tab(self):
        x = 1
        if x < 3:
            Tab = "tab" + str(x)
            tab = "self.tab" + str(x)
            self.tabs.addTab(tab, Tab)
            x += 1

    def choix_du_serveur(self):
        if self.sh_srv.currentText() == "Serveur_1":
            print("Serveur_1")
            self.creat_tab()

        elif self.sh_srv.currentText() == "Serveur_2":
            print("Serveur_2")
            self.creat_tab()

        elif self.sh_srv.currentText() == "Serveur_3":
            print("Serveur_3")
            self.creat_tab()


    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())