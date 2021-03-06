# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instagram.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QSize
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QGroupBox, QGraphicsBlurEffect, QHBoxLayout, QLabel
from myfunctions import *

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        #Create Main Window Object
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1324, 818)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint) #Remove application border


        #Palette created by PyQt5
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)


        #Add palette and stylesheet to MainWindow
        MainWindow.setPalette(palette)
        MainWindow.setMouseTracking(False)
        MainWindow.setWindowTitle("")
        MainWindow.setWindowOpacity(100.0)
        MainWindow.setStyleSheet("background: transparent;") #Make main background transparent


        #Create Central Widget object
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")


        #Create MenuGroupBox
        self.menuGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.menuGroupBox.setGeometry(QtCore.QRect(10, 70, 91, 631)) #Size and Position
        self.menuGroupBox.setStyleSheet("/*background-color: rgb(65, 75, 70);*/\n"
                                        "background-color: rgb(53, 61, 57);\n"
                                        "border: 0px solid #900;\n"
                                        "border-radius: 5px;")
        self.menuGroupBox.setTitle("")
        self.menuGroupBox.setObjectName("menuGroupBox")


        #Grid Layout for Menu
        self.gridLayoutWidget = QtWidgets.QWidget(self.menuGroupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 101, 631))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.menuGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.menuGridLayout.setContentsMargins(0, 0, 0, 0)
        self.menuGridLayout.setObjectName("menuGridLayout")


        #Settings Menu Button
        self.settingsMenuButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.settingsMenuButton.setMinimumSize(QtCore.QSize(64, 64))
        self.settingsMenuButton.setStyleSheet(
            "#settingsMenuButton{background-image : url(P:/Finished Coding Projects/Instagram Photo Downloader UNFINISHED/icons/settings.png);\n"
            "background-repeat: no-repeat;} #settingsMenuButton:hover {background-color: rgb(77, 89, 83);}")
        self.settingsMenuButton.setText("")
        self.settingsMenuButton.setObjectName("settingsMenuButton")
        self.menuGridLayout.addWidget(self.settingsMenuButton, 3, 0, 1, 1)


        #Open Folder Menu Button
        self.openFolderButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.openFolderButton.setMinimumSize(QtCore.QSize(64, 64))
        self.openFolderButton.setStyleSheet(
            "#openFolderButton{background-image : url(P:/Finished Coding Projects/Instagram Photo Downloader UNFINISHED/icons/folder.png);\n"
            "background-repeat: no-repeat;} #openFolderButton:hover {background-color: rgb(77, 89, 83);}")
        self.openFolderButton.setText("")
        self.openFolderButton.setObjectName("openFolderButton")
        self.openFolderButton.clicked.connect(myfunctions.openFolderButton)
        self.menuGridLayout.addWidget(self.openFolderButton, 2, 0, 1, 1)




        #Bookmarks Menu Button
        self.bookmarksMenuButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bookmarksMenuButton.setMinimumSize(QtCore.QSize(64, 64))
        self.bookmarksMenuButton.setStyleSheet(
            "#bookmarksMenuButton {background-image : url(P:/Finished Coding Projects/Instagram Photo Downloader UNFINISHED/icons/bookmarks.png);\n"
            "background-repeat: no-repeat;} #bookmarksMenuButton:hover {background-color: rgb(77, 89, 83);}")
        self.bookmarksMenuButton.setText("")
        self.bookmarksMenuButton.setObjectName("bookmarksMenuButton")
        self.menuGridLayout.addWidget(self.bookmarksMenuButton, 1, 0, 1, 1)


        #Main Page Menu Button
        self.mainMenuButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.mainMenuButton.setMinimumSize(QtCore.QSize(64, 64))
        self.mainMenuButton.setStyleSheet(
            "#mainMenuButton {background-image : url(P:/Finished Coding Projects/Instagram Photo Downloader UNFINISHED/icons/profile.png);\n"
            "background-repeat: no-repeat;} #mainMenuButton:hover {background-color: rgb(77, 89, 83);}")
        self.mainMenuButton.setText("")
        self.mainMenuButton.setObjectName("mainMenuButton")
        self.menuGridLayout.addWidget(self.mainMenuButton, 0, 0, 1, 1)


        #Main Frame of application
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setGeometry(QtCore.QRect(99, 9, 1221, 761))
        self.mainFrame.setStyleSheet("#mainFrame {\n"
                                     "background-image : url(P:/Finished Coding Projects/Instagram Photo Downloader UNFINISHED/background-image.png);\n"
                                     "filter: blur(20px);\n"
                                     "-webkit-filter: blur(20px);\n"
                                     "border-radius: 5px;\n"
                                     "}")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")


        #Search Group Box for search bar and search button
        self.searchGroupBox = QtWidgets.QGroupBox(self.mainFrame)
        self.searchGroupBox.setGeometry(QtCore.QRect(240, 20, 751, 79))
        self.searchGroupBox.setStyleSheet("background-color: rgb(53, 61, 57);\n"
                                          "border: 0px solid #900;\n"
                                          "border-radius: 5px;\n"
                                          "backdrop-filter: blur(10px);")
        self.searchGroupBox.setTitle("")
        self.searchGroupBox.setObjectName("searchGroupBox")


        #Search Button creation
        self.searchButton = QtWidgets.QPushButton(self.searchGroupBox)
        self.searchButton.setGeometry(QtCore.QRect(670, 15, 61, 51))
        self.searchButton.setStyleSheet(
            "#searchButton {background-image : url(P:/Finished Coding Projects/Instagram Photo Downloader UNFINISHED/icons/search43.png);\n"
            "background-repeat: no-repeat;} #searchButton:hover {background-color: rgb(77, 89, 83);}")
        self.searchButton.setText("")
        self.searchButton.setObjectName("searchButton")


        #Search Bar Creation
        self.searchBar = QtWidgets.QLineEdit(self.searchGroupBox)
        self.searchBar.setGeometry(QtCore.QRect(20, 20, 641, 41))
        self.searchBar.setAutoFillBackground(False)
        self.searchBar.setStyleSheet("border-radius: 5px;\n"
                                     "background-color: rgb(244, 244, 244);\n"
                                     "")
        self.searchBar.setObjectName("searchBar")


        #Application Exit Group Box
        self.exitBox = QGroupBox(self.mainFrame)
        self.exitBox.setObjectName(u"exitBox")
        self.exitBox.setGeometry(QRect(1170, 10, 41, 41))
        self.exitBox.setStyleSheet(u" #exitBox {background-color: rgb(53, 61, 57);\n"
                                   "border-radius: 5px;}")


        #Exit Button for Application
        self.exitButton = QPushButton(self.mainFrame)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(1170, 10, 41, 41))
        self.exitButton.clicked.connect(myfunctions.exit)
        self.exitButton.setStyleSheet(
            u"#exitButton {background-image : url(P:/Finished Coding Projects/Instagram Photo Downloader UNFINISHED/icons/exit2.png);\n"
            "background-repeat: no-repeat; border-radius: 5px;} #exitButton:hover {background-color: rgb(77, 89, 83);}")






        # Main page scroll window -- to hold grid layout and all images
        self.mainPageScroll = QtWidgets.QScrollArea(self.mainFrame)
        self.mainPageScroll.setGeometry(QtCore.QRect(20, 110, 1181, 631))
        self.mainPageScroll.setStyleSheet("#mainPageScroll {\n"
                                          "    border: 0px solid black;\n"
                                          "    background-color: rgb(53, 61, 57, 200); border-radius: 5px;\n"
                                          "}")
        self.mainPageScroll.setWidgetResizable(True)
        self.mainPageScroll.setObjectName("mainPageScroll")


        #Main Page Window Scroll Grid Layout
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1181, 631))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.mainPageScroll.setWidget(self.scrollAreaWidgetContents)






        self.label_1 = QLabel(self.scrollAreaWidgetContents)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(20, 30, 270, 270))
        self.label_1.setMinimumSize(QSize(270, 270))
        self.label_1.setMaximumSize(QSize(380, 600))
        self.label_1.setStyleSheet(u"")
        self.label_1.setPixmap(QPixmap(u"testpic.jpg"))
        self.label_1.setScaledContents(True)
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 30, 270, 270))
        self.label_2.setMinimumSize(QSize(270, 270))
        self.label_2.setMaximumSize(QSize(380, 600))
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u"testpic.jpg"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(600, 30, 270, 270))
        self.label_3.setMinimumSize(QSize(270, 270))
        self.label_3.setMaximumSize(QSize(380, 600))
        self.label_3.setStyleSheet(u"")
        self.label_3.setPixmap(QPixmap(u"testpic.jpg"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(890, 30, 270, 270))
        self.label_4.setMinimumSize(QSize(270, 270))
        self.label_4.setMaximumSize(QSize(380, 600))
        self.label_4.setStyleSheet(u"")
        self.label_4.setPixmap(QPixmap(u"testpic.jpg"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(310, 340, 270, 270))
        self.label_5.setMinimumSize(QSize(270, 270))
        self.label_5.setMaximumSize(QSize(380, 600))
        self.label_5.setStyleSheet(u"")
        self.label_5.setPixmap(QPixmap(u"testpic.jpg"))
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(600, 340, 270, 270))
        self.label_6.setMinimumSize(QSize(270, 270))
        self.label_6.setMaximumSize(QSize(380, 600))
        self.label_6.setStyleSheet(u"")
        self.label_6.setPixmap(QPixmap(u"testpic.jpg"))
        self.label_6.setScaledContents(True)
        self.leftArrow = QPushButton(self.scrollAreaWidgetContents)
        self.leftArrow.setObjectName(u"leftArrow")
        self.leftArrow.setGeometry(QRect(80, 420, 111, 101))
        self.leftArrow.setStyleSheet(u"#leftArrow {\n"
                                     "background-image : url(P:/Finished Coding Projects/Instagram Photo Downloader UNFINISHED/icons/chevron_left.png);\n"
                                     "background-repeat: no-repeat;\n"
                                     "}\n"
                                     "\n"
                                     "#leftArrow:hover {\n"
                                     "	background-color: rgb(77, 89, 83);\n"
                                     "}\n"
                                     "\n"
                                     "")
        self.rightArrow = QPushButton(self.scrollAreaWidgetContents)
        self.rightArrow.setObjectName(u"rightArrow")
        self.rightArrow.setGeometry(QRect(980, 420, 121, 111))
        self.rightArrow.setStyleSheet(u"#rightArrow {\n"
                                      "\n"
                                      "background-repeat: no-repeat; border-radius:5px;\n"
                                      "background-image : url(P:/Finished Coding Projects/Instagram Photo Downloader UNFINISHED/icons/chevron_right.png);\n"
                                      "}\n"
                                      "\n"
                                      "#rightArrow:hover {\n"
                                      "	background-color: rgb(77, 89, 83);\n"  
                                      "}")






        # Main Page Window Blur Effect
        #self.blur_effect = QGraphicsBlurEffect()
        #self.mainPageScroll.setGraphicsEffect(self.blur_effect)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass






if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground, 60)
    MainWindow.show()
    sys.exit(app.exec_())
