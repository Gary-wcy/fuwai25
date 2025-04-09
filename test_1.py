# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1578, 1013)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 1411, 951))
        self.label.setPixmap(QPixmap(u"images/resources/background_1.png"))
        self.label.setScaledContents(True)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(230, 120, 961, 661))
        self.tabWidget.setStyleSheet(u"QTabWidget:pane {\n"
"	border-top:0px \n"
"	solid #e8f3f9;\n"
"	background:  transparent; \n"
"	border-top:2px solid black;\n"
"}\n"
"QTabBar::tab:!selected{\n"
"    background: transparent;\n"
"	color:white\n"
"}\n"
"QTabBar::tab:selected {\n"
"    color: white ;\n"
"	background: transparent;\n"
"	border-bottom:2px solid rgb(28, 72, 193)\n"
"}\n"
"QTabBar::tab{\n"
"	height:40;\n"
"	width:80;\n"
"}")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.left_ing = QLabel(self.tab_2)
        self.left_ing.setObjectName(u"left_ing")
        self.left_ing.setGeometry(QRect(120, 120, 331, 301))
        self.left_ing.setPixmap(QPixmap(u"images/resources/demo.jpg"))
        self.left_ing.setScaledContents(True)
        self.right_ing = QLabel(self.tab_2)
        self.right_ing.setObjectName(u"right_ing")
        self.right_ing.setGeometry(QRect(500, 120, 321, 301))
        self.right_ing.setPixmap(QPixmap(u"images/resources/result.jpg"))
        self.right_ing.setScaledContents(True)
        self.layoutWidget = QWidget(self.tab_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(520, 470, 301, 80))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.up_load_button = QPushButton(self.layoutWidget)
        self.up_load_button.setObjectName(u"up_load_button")
        self.up_load_button.setStyleSheet(u"QPushButton{color:white}\n"
"QPushButton:hover{background-color: rgb(2,110,180);}\n"
"QPushButton{background-color:rgb(48,124,208)}\n"
"QPushButton{border:2px}\n"
"QPushButton{border-radius:5px}\n"
"QPushButton{padding:5px 5px}\n"
"QPushButton{margin:5px 5px}")

        self.verticalLayout.addWidget(self.up_load_button)

        self.start_button = QPushButton(self.layoutWidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setStyleSheet(u"QPushButton{color:white}\n"
"QPushButton:hover{background-color: rgb(2,110,180);}\n"
"QPushButton{background-color:rgb(48,124,208)}\n"
"QPushButton{border:2px}\n"
"QPushButton{border-radius:5px}\n"
"QPushButton{padding:5px 5px}\n"
"QPushButton{margin:5px 5px}")

        self.verticalLayout.addWidget(self.start_button)

        self.layoutWidget_2 = QWidget(self.tab_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(120, 90, 441, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color:white")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color:white")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(355, 10, 241, 31))
        font = QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: white ;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.layoutWidget_3 = QWidget(self.tab_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(600, 490, 301, 80))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.up_load_button_2 = QPushButton(self.layoutWidget_3)
        self.up_load_button_2.setObjectName(u"up_load_button_2")
        self.up_load_button_2.setStyleSheet(u"QPushButton{color:white}\n"
"QPushButton:hover{background-color: rgb(2,110,180);}\n"
"QPushButton{background-color:rgb(48,124,208)}\n"
"QPushButton{border:2px}\n"
"QPushButton{border-radius:5px}\n"
"QPushButton{padding:5px 5px}\n"
"QPushButton{margin:5px 5px}")

        self.verticalLayout_2.addWidget(self.up_load_button_2)

        self.stop_button_2 = QPushButton(self.layoutWidget_3)
        self.stop_button_2.setObjectName(u"stop_button_2")
        self.stop_button_2.setStyleSheet(u"QPushButton{color:white}\n"
"QPushButton:hover{background-color: rgb(2,110,180);}\n"
"QPushButton{background-color:rgb(48,124,208)}\n"
"QPushButton{border:2px}\n"
"QPushButton{border-radius:5px}\n"
"QPushButton{padding:5px 5px}\n"
"QPushButton{margin:5px 5px}")

        self.verticalLayout_2.addWidget(self.stop_button_2)

        self.sp_img = QLabel(self.tab_3)
        self.sp_img.setObjectName(u"sp_img")
        self.sp_img.setGeometry(QRect(100, 50, 750, 350))
        self.sp_img.setScaledContents(True)
        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(355, 10, 241, 31))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: white ;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.Sx_img = QLabel(self.tab)
        self.Sx_img.setObjectName(u"Sx_img")
        self.Sx_img.setGeometry(QRect(100, 50, 750, 350))
        self.Sx_img.setScaledContents(True)
        self.layoutWidget_4 = QWidget(self.tab)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(600, 490, 301, 80))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.start_button_3 = QPushButton(self.layoutWidget_4)
        self.start_button_3.setObjectName(u"start_button_3")
        self.start_button_3.setStyleSheet(u"QPushButton{color:white}\n"
"QPushButton:hover{background-color: rgb(2,110,180);}\n"
"QPushButton{background-color:rgb(48,124,208)}\n"
"QPushButton{border:2px}\n"
"QPushButton{border-radius:5px}\n"
"QPushButton{padding:5px 5px}\n"
"QPushButton{margin:5px 5px}")

        self.verticalLayout_3.addWidget(self.start_button_3)

        self.stop_button = QPushButton(self.layoutWidget_4)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setStyleSheet(u"QPushButton{color:white}\n"
"QPushButton:hover{background-color: rgb(2,110,180);}\n"
"QPushButton{background-color:rgb(48,124,208)}\n"
"QPushButton{border:2px}\n"
"QPushButton{border-radius:5px}\n"
"QPushButton{padding:5px 5px}\n"
"QPushButton{margin:5px 5px}")

        self.verticalLayout_3.addWidget(self.stop_button)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(355, 10, 241, 31))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: white ;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab, "")
        self.exit_button = QPushButton(Form)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(1220, 130, 31, 31))
        icon = QIcon()
        icon.addFile(u"images/resources/\u5173\u95ed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.left_ing.setText("")
        self.right_ing.setText("")
        self.up_load_button.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.start_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u68c0\u6d4b\u540e\u56fe\u7247", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u68c0\u6d4b\u529f\u80fd", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u56fe\u7247\u68c0\u6d4b", None))
        self.up_load_button_2.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u89c6\u9891", None))
        self.stop_button_2.setText(QCoreApplication.translate("Form", u"\u505c\u6b62\u68c0\u6d4b", None))
        self.sp_img.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u89c6\u9891\u68c0\u6d4b\u529f\u80fd", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u89c6\u9891\u68c0\u6d4b", None))
        self.Sx_img.setText("")
        self.start_button_3.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.stop_button.setText(QCoreApplication.translate("Form", u"\u505c\u6b62\u68c0\u6d4b", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u6444\u50cf\u5934\u68c0\u6d4b\u529f\u80fd", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u6444\u50cf\u5934\u68c0\u6d4b", None))
        self.exit_button.setText("")
    # retranslateUi

