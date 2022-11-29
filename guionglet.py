"""
Imports
"""
 
try:
    from PyQt5 import QtWidgets, QtCore, QtGui
    from PyQt5.QtCore import Qt, QPoint
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDesktopWidget, QTreeWidget, QMenu, QDialog, QLineEdit, QVBoxLayout, QMessageBox
    from PyQt5.QtWidgets import *
    import PyQt5
    import sys
 
except Exception as e:
    print("Error [16.00] : \n \t", e)
    exit()
 
class Root(QMainWindow):
 
    def __init__(self, y_pos, x_pos, width, height):
        super(Root, self).__init__()
        self.setGeometry(y_pos, x_pos, width, height)
        self.setWindowTitle("TEST")
        self.ui()
     
    def new_tab(self):
 
        self.widget_new = QtWidgets.QWidget()
        self.centered.addTab(self.widget_new, "Untitled")
        self.centered.setCurrentIndex(self.centered.count() - 1)
 
        self.add_tab.move(100 * self.centered.count(), 0)
 
        self.add_tab.setFixedHeight(28)
        self.add_tab.setFixedWidth(32)
        self.add_tab.setStyleSheet(".QToolButton { border: 1px solid lightgrey; margin-left: 2px; border-bottom: 0px; }")
 
        for widget in range(self.centered.count()):
 
            btn = QtWidgets.QPushButton("×")
            btn.setFixedSize(20, 20)
            btn.setStyleSheet(".QPushButton { padding: 0; margin: 0; border: 1px solid lightgrey; border-radius: 2px; padding-bottom: 1.5px; margin-top: 1.5px; } ::hover { border-color: grey }")
            btn.clicked.connect(lambda: self.delete_tab(btn))
     
            #for each_tab in range(self.centered.count()):
            self.centered.tabBar().setTabButton(widget, self.centered.tabBar().RightSide, btn)
         
    def delete_tab(self, btn):
 
        self.centered.removeTab(self.centered.currentIndex())
 
        self.add_tab.move(100 * self.centered.count(), 0)
 
        if self.centered.count() == 1:
            self.centered.tabBar().setTabButton(0, self.centered.tabBar().RightSide, None)
            self.add_tab.setFixedHeight(20)
            self.add_tab.setFixedWidth(24)
 
    def ui(self):
 
        self.centered = QtWidgets.QTabWidget(self)
        self.centered.setMinimumWidth(1000)
        self.centered.setMinimumHeight(1000)
 
        self.center = QtWidgets.QWidget()
 
        self.centered.addTab(self.center, "Untitled")
 
        self.centered.setStyleSheet("QTabBar::tab { width: 100px }")
 
        self.add_tab = QtWidgets.QToolButton(self.centered)
        self.add_tab.setText("+")
        self.number_tabs = self.centered.count()
        self.add_tab.move(100 * self.number_tabs, 0)
 
        self.add_tab.setFixedHeight(20)
        self.add_tab.setFixedWidth(24)
        self.add_tab.setStyleSheet(".QToolButton { border: 1px solid lightgrey; margin-left: 2px; border-bottom: 0px; }")

        self.add_tab.clicked.connect(self.new_tab)


    def index_changed(self, i): # Not an index, i is a QListItem
        print(i.text())

    def text_changed(self, s): # s is a str
        print(s)


app = QApplication(sys.argv)
if(QDialog.Accepted == True):
    root = Root(0, 0, 1080, 720)
    root.show()
 
sys.exit(app.exec_())