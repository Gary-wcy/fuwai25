# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'duotupian.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1558, 963)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 1411, 951))
        self.label.setPixmap(QPixmap(u"images/resources/backgound_2.png"))
        self.label.setScaledContents(True)
        self.backbutton = QPushButton(Form)
        self.backbutton.setObjectName(u"backbutton")
        self.backbutton.setGeometry(QRect(180, 140, 141, 51))
        self.backbutton.setStyleSheet(u"QPushButton {\n"
"    /* \u9ed8\u8ba4\u72b6\u6001\u4e0b\u7684\u6837\u5f0f */\n"
"    color: white;\n"
"    background-color: rgb(48, 124, 208);\n"
"    border: 2px solid rgb(48, 124, 208);\n"
"    border-radius: 5px;\n"
"    padding: 5px 15px;\n"
"    margin: 5px;\n"
"    font-size: 14px;\n"
"    transition: all 0.3s; /* \u5e73\u6ed1\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u6837\u5f0f */\n"
"    background-color: rgb(2, 110, 180);\n"
"    transform: scale(2); /* \u6309\u94ae\u653e\u592710% */\n"
"    border-color: rgb(2, 110, 180);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* \u9f20\u6807\u70b9\u51fb\u65f6\u7684\u6837\u5f0f */\n"
"    background-color: rgb(1, 90, 150);\n"
"    transform: scale(0.5); /* \u6309\u94ae\u7f29\u5c0f5% */\n"
"    border-color: rgb(1, 90, 150);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* \u6309\u94ae\u7981\u7528\u65f6\u7684\u6837\u5f0f */\n"
"    color: gray;\n"
"    background-color: rgb(150, 150, 150);\n"
""
                        "    border-color: rgb(150, 150, 150);\n"
"}")
        icon = QIcon()
        icon.addFile(u"images/resources/\u9000\u51fa.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backbutton.setIcon(icon)
        self.backbutton.setIconSize(QSize(30, 30))
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(207, 340, 54, 311))
        self.label_7.setTextFormat(Qt.TextFormat.AutoText)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.closebutton = QPushButton(Form)
        self.closebutton.setObjectName(u"closebutton")
        self.closebutton.setGeometry(QRect(1220, 140, 40, 40))
        self.closebutton.setStyleSheet(u"QPushButton {\n"
"    /* \u9ed8\u8ba4\u72b6\u6001\u4e0b\u7684\u6837\u5f0f */\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px 15px;\n"
"    margin: 5px;\n"
"    font-size: 14px;\n"
"    transition: all 0.3s; /* \u5e73\u6ed1\u8fc7\u6e21\u6548\u679c */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u6837\u5f0f */\n"
"    background-color: rgb(2, 110, 180);\n"
"    transform: scale(2); /* \u6309\u94ae\u653e\u592710% */\n"
"    border-color: rgb(2, 110, 180);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* \u9f20\u6807\u70b9\u51fb\u65f6\u7684\u6837\u5f0f */\n"
"    background-color: rgb(1, 90, 150);\n"
"    transform: scale(0.5); /* \u6309\u94ae\u7f29\u5c0f5% */\n"
"    border-color: rgb(1, 90, 150);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    /* \u6309\u94ae\u7981\u7528\u65f6\u7684\u6837\u5f0f */\n"
"    color: gray;\n"
"    background-color: rgb(150, 150, 150);\n"
"    border-color: rgb(150, 150, 150);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"images/resources/\u5173\u95ed.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closebutton.setIcon(icon1)
        self.closebutton.setIconSize(QSize(30, 30))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 260, 70, 70))
        self.label_2.setPixmap(QPixmap(u"images/resources/\u591a\u7ec4\u56fe\u7247.png"))
        self.label_2.setScaledContents(True)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(360, 220, 761, 552))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pictures_img = QLabel(self.layoutWidget)
        self.pictures_img.setObjectName(u"pictures_img")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pictures_img.sizePolicy().hasHeightForWidth())
        self.pictures_img.setSizePolicy(sizePolicy)
        self.pictures_img.setMaximumSize(QSize(759, 460))
        self.pictures_img.setStyleSheet(u"QLabel {\n"
"	border-radius: 10px; /* \u8bbe\u7f6e\u8fb9\u6846\u5706\u89d2\u534a\u5f84 */\n"
"    border-top: 4px solid rgb(101,102,103);  /* \u9ad8\u7ea7\u7070\u8272 rgb(139,140,140) */\n"
"    border-right: 4px solid rgb(101,102,103) ;\n"
"    border-bottom: 4px solid rgb(139,140,140)  ; /*\u795e\u79d8\u7070rgb(101,102,103)*/\n"
"    border-left: 4px solid rgb(139,140,140)  ; \n"
"    padding: 5px; /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */\n"
"}")
        self.pictures_img.setPixmap(QPixmap(u"images/resources/\u4eba\u50cf.png"))
        self.pictures_img.setScaledContents(True)

        self.verticalLayout.addWidget(self.pictures_img)

        self.verticalSpacer = QSpacerItem(10, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.up_load_button_2 = QPushButton(self.layoutWidget)
        self.up_load_button_2.setObjectName(u"up_load_button_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.up_load_button_2.sizePolicy().hasHeightForWidth())
        self.up_load_button_2.setSizePolicy(sizePolicy1)
        self.up_load_button_2.setStyleSheet(u"QPushButton{color:white}\n"
"QPushButton:hover{background-color: rgb(2,110,180);}\n"
"QPushButton{background-color:rgb(48,124,208)}\n"
"QPushButton{border:2px}\n"
"QPushButton{border-radius:5px}\n"
"QPushButton{padding:5px 5px}\n"
"QPushButton{margin:5px 5px}")

        self.horizontalLayout.addWidget(self.up_load_button_2)

        self.horizontalSpacer = QSpacerItem(3, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.stop_button = QPushButton(self.layoutWidget)
        self.stop_button.setObjectName(u"stop_button")
        sizePolicy1.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy1)
        self.stop_button.setStyleSheet(u"QPushButton{color:white}\n"
"QPushButton:hover{background-color: rgb(2,110,180);}\n"
"QPushButton{background-color:rgb(48,124,208)}\n"
"QPushButton{border:2px}\n"
"QPushButton{border-radius:5px}\n"
"QPushButton{padding:5px 5px}\n"
"QPushButton{margin:5px 5px}")

        self.horizontalLayout.addWidget(self.stop_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.backbutton.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de\u4e3b\u9875", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:700;\">\u591a<br/>\u5f20<br/>\u56fe<br/>\u7247<br/>\u68c0<br/>\u6d4b</span></p></body></html>", None))
        self.closebutton.setText("")
        self.label_2.setText("")
        self.pictures_img.setText("")
        self.up_load_button_2.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u68c0\u6d4b\u6587\u4ef6\u5939", None))
        self.stop_button.setText(QCoreApplication.translate("Form", u"\u505c\u6b62\u68c0\u6d4b", None))
    # retranslateUi

