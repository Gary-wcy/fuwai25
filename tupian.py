# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tupian.ui'
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
        Form.resize(1512, 1072)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 1411, 951))
        self.label.setPixmap(QPixmap(u"images/resources/backgound_2.png"))
        self.label.setScaledContents(True)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(200, 260, 70, 70))
        self.label_6.setPixmap(QPixmap(u"images/resources/\u56fe\u7247_2.png"))
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(207, 340, 54, 311))
        self.label_7.setTextFormat(Qt.TextFormat.AutoText)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
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
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(390, 210, 731, 531))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(1, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.left_img = QLabel(self.widget)
        self.left_img.setObjectName(u"left_img")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_img.sizePolicy().hasHeightForWidth())
        self.left_img.setSizePolicy(sizePolicy1)
        self.left_img.setMinimumSize(QSize(100, 100))
        self.left_img.setMaximumSize(QSize(320, 400))
        self.left_img.setStyleSheet(u"QLabel {\n"
"	border-radius: 10px; /* \u8bbe\u7f6e\u8fb9\u6846\u5706\u89d2\u534a\u5f84 */\n"
"	border-bottom: 4px solid rgb(101,102,103) ; /*\u795e\u79d8\u7070*/\n"
"    border-left: 4px solid rgb(101,102,103) ; \n"
"    border-top: 4px solid rgb(139,140,140) ;  /* \u9ad8\u7ea7\u7070\u8272 */\n"
"    border-right: 4px solid rgb(139,140,140) ;\n"
"    padding: 5px; /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */\n"
"}")
        self.left_img.setPixmap(QPixmap(u"images/resources/\u4eba\u50cf_1.png"))
        self.left_img.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.left_img)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.verticalSpacer_2 = QSpacerItem(1, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.right_img = QLabel(self.widget)
        self.right_img.setObjectName(u"right_img")
        sizePolicy1.setHeightForWidth(self.right_img.sizePolicy().hasHeightForWidth())
        self.right_img.setSizePolicy(sizePolicy1)
        self.right_img.setMaximumSize(QSize(320, 400))
        self.right_img.setStyleSheet(u"QLabel {\n"
"	border-radius: 10px; /* \u8bbe\u7f6e\u8fb9\u6846\u5706\u89d2\u534a\u5f84 */\n"
"    border-top: 4px solid rgb(101,102,103);  /* \u9ad8\u7ea7\u7070\u8272 rgb(139,140,140) */\n"
"    border-right: 4px solid rgb(101,102,103) ;\n"
"    border-bottom: 4px solid rgb(139,140,140)  ; /*\u795e\u79d8\u7070rgb(101,102,103)*/\n"
"    border-left: 4px solid rgb(139,140,140)  ; \n"
"    padding: 5px; /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */\n"
"}")
        self.right_img.setPixmap(QPixmap(u"images/resources/\u4eba\u50cf.png"))
        self.right_img.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.right_img)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.up_load_button = QPushButton(self.widget)
        self.up_load_button.setObjectName(u"up_load_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.up_load_button.sizePolicy().hasHeightForWidth())
        self.up_load_button.setSizePolicy(sizePolicy2)
        self.up_load_button.setStyleSheet(u"QPushButton {\n"
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
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(2, 110, 180);\n"
"    transform: scale(2); \n"
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

        self.horizontalLayout_2.addWidget(self.up_load_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.start_button = QPushButton(self.widget)
        self.start_button.setObjectName(u"start_button")
        sizePolicy2.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy2)
        self.start_button.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.start_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:700;\">\u5355<br/>\u5f20<br/>\u56fe<br/>\u7247<br/>\u68c0<br/>\u6d4b</span></p></body></html>", None))
        self.backbutton.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de\u4e3b\u9875", None))
        self.closebutton.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u68c0\u6d4b\u524d\u56fe\u7247</span></p></body></html>", None))
        self.left_img.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u68c0\u6d4b\u540e\u56fe\u7247</span></p></body></html>", None))
        self.right_img.setText("")
        self.up_load_button.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20\u56fe\u7247", None))
        self.start_button.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u68c0\u6d4b", None))
    # retranslateUi

