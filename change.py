from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget

from Main import Ui_Form
from tupian import Ui_Form as Ui_Page2
from Main import Ui_Form as Ui_Page1

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowTitle("Qt Designer 页面跳转示例")

        # 创建 QStackedWidget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # 创建页面实例
        self.page1 = Ui_Page1()
        self.page2 = Ui_Page2()

        # 创建 QWidget 实例并应用界面
        self.widget_page1 = QWidget()
        self.widget_page2 = QWidget()

        self.page1.setupUi(self.widget_page1)
        self.page2.setupUi(self.widget_page2)

        # 将页面添加到 QStackedWidget
        self.stacked_widget.addWidget(self.widget_page1)
        self.stacked_widget.addWidget(self.widget_page2)

        # 连接按钮点击事件
        self.page1.picture.clicked.connect(self.go_to_page2)
        self.page2.backbutton.clicked.connect(self.go_to_page1)

    def go_to_page2(self):
        # 切换到第二个页面
        self.stacked_widget.setCurrentIndex(1)

    def go_to_page1(self):
        # 切换到第一个页面
        self.stacked_widget.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()