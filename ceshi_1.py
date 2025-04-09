import sys


import copy                      # 用于图像复制
import os                        # 用于系统路径查找
import shutil                    # 用于复制

from PySide6 import QtCore
from PySide6.QtGui import *      # GUI组件
from PySide6.QtCore import *     # 字体、边距等系统变量
from PySide6.QtWidgets import *  # 窗口等小组件
import threading                 # 多线程
import sys                       # 系统库
import cv2                       # opencv图像处理
import torch                     # 深度学习框架
import os.path as osp            # 路径查找
import time                      # 时间计算
from ultralytics import YOLO     # yolo核心算法
from test_1 import Ui_Form
from ultralytics import YOLO

IMAGE_LEFT_INIT = "images/resources/demo.jpg"              # 图片检测界面初始化左侧图像
IMAGE_RIGHT_INIT = "images/resources/result.jpg"          # 图片检测界面初始化右侧图像
IMAGE_VID_INIT = "images/UI/up.jpeg"
ICON_IMAGE = "images/resources/logo-1.png"                 # 系统logo界面

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon(ICON_IMAGE))
        self.stopEvent = threading.Event()
        self.webcam = True
        self.stopEvent.clear()
        self.init_vid_id = '0'  # 摄像头修改
        self.vid_source = int(self.init_vid_id)
        self.a=0
        self.model_path = "weights/hongwaiout.pt"  # todo 指明模型加载的位置的设备
        self.model = self.model_load(weights=self.model_path)
        self.output_size = 480
        self.conf_thres = 0.25  # 置信度的阈值
        self.iou_thres = 0.45  # NMS操作的时候 IOU过滤的阈值
        self.vid_gap = 30  # 摄像头视频帧保存间隔。
        self.setupUi(self)
        self.bind()

    # 在类中添加以下方法
    def mousePressEvent(self, event):
        self.drag_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if hasattr(self, 'drag_pos'):
            self.move(self.pos() + event.globalPos() - self.drag_pos)
            self.drag_pos = event.globalPos()

    # 模型初始化
    @torch.no_grad()
    def model_load(self, weights=""):
        """
        模型加载
        """
        model_loaded = YOLO(weights)
        return model_loaded


    def bind(self):
        self.exit_button.clicked.connect(self.close)#退出按钮
        self.left_ing.setPixmap(QPixmap(IMAGE_LEFT_INIT))
        self.right_ing.setPixmap(QPixmap(IMAGE_RIGHT_INIT))
        self.up_load_button.clicked.connect(self.upload_img)
        self.start_button.clicked.connect(self.detect_img)
        self.sp_img.setPixmap(QPixmap(IMAGE_VID_INIT))
        self.up_load_button_2.clicked.connect(self.open_mp4)
        self.start_button_3.clicked.connect(self.open_cam)
        self.stop_button.clicked.connect(self.close_vid)
        self.stop_button_2.clicked.connect(self.close_vid)

    def closeEvent(self, event):
        """用户退出事件"""
        reply = QMessageBox.question(self,
                                     'quit',
                                     "Are you sure?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                # 退出之后一定要尝试释放摄像头资源，防止资源一直在线
                if self.cap is not None:
                    self.cap.release()
                    print("摄像头已释放")
            except:
                pass
            self.close()
            event.accept()
        else:
            event.ignore()

    def upload_img(self):
        """上传图像，图像要尽可能保证是中文格式"""
        fileName, fileType = QFileDialog.getOpenFileName(self, 'Choose file', '', '*.jpg *.png *.tif *.jpeg')
        if fileName:
            # 判断用户是否选择了图像，如果用户选择了图像则执行下面的操作
            suffix = fileName.split(".")[-1]
            save_path = osp.join("images/tmp", "tmp_upload." + suffix)  # 将图像转移到images目录下并且修改为英文的形式
            shutil.copy(fileName, save_path)
            im0 = cv2.imread(save_path)
            resize_scale = self.output_size / im0.shape[0]
            im0 = cv2.resize(im0, (0, 0), fx=resize_scale, fy=resize_scale)
            cv2.imwrite("images/tmp/upload_show_result.jpg", im0)
            self.img2predict = save_path                               # 给变量进行赋值方便后面实际进行读取
            # 将图像显示在界面上并将预测的文字内容进行初始化
            self.left_ing.setPixmap(QPixmap("images/tmp/upload_show_result.jpg"))
            self.right_ing.setPixmap(QPixmap(IMAGE_RIGHT_INIT))

# 图片检测
    def detect_img(self):
        """检测单张的图像文件"""
        # txt_results = []
        output_size = self.output_size
        results = self.model(self.img2predict)  # 读取图像并执行检测的逻辑
        result = results[0]                     # 获取检测结果
        img_array = result.plot()               # 在图像上绘制检测结果
        im0 = img_array
        im_record = copy.deepcopy(im0)
        resize_scale = output_size / im0.shape[0]
        im0 = cv2.resize(im0, (0, 0), fx=resize_scale, fy=resize_scale)
        cv2.imwrite("images/tmp/single_result.jpg", im0)
        self.right_ing.setPixmap(QPixmap("images/tmp/single_result.jpg"))
        time_re = str(time.strftime('result_%Y-%m-%d_%H-%M-%S_%A'))
        cv2.imwrite("record/img/{}.jpg".format(time_re), im_record)
        # 保存txt记录文件
        # if len(txt_results) > 0:
        #     np.savetxt('record/img/{}.txt'.format(time_re), np.array(txt_results), fmt="%s %s %s %s %s %s",
        #                delimiter="\n")
        # 获取预测出来的每个类别的数量并在对应的图形化检测页面上进行显示
        result_names = result.names
        result_nums = [0 for i in range(0, len(result_names))]
        cls_ids = list(result.boxes.cls.cpu().numpy())
        for cls_id in cls_ids:
            result_nums[int(cls_id)] = result_nums[int(cls_id)] + 1
        result_info = ""
        for idx_cls, cls_num in enumerate(result_nums):
            # 添加对数据0的判断，如果当前数据的数目为0，则这个数据不需要加入到里面
            if cls_num > 0:
                result_info = result_info + "{}:{}\n".format(result_names[idx_cls], cls_num)

    def open_cam(self):
        """打开摄像头上传"""
        self.start_button_3.setEnabled(False)    # 将打开摄像头的按钮设置为false，防止用户误触
        self.up_load_button_2.setEnabled(False)       # 将打开mp4文件的按钮设置为false，防止用户误触
        self.stop_button.setEnabled(True)
        self.stop_button_2.setEnabled(True)# 将关闭按钮打开，用户可以随时点击关闭按钮关闭实时的检测任务
        self.vid_source = int(self.init_vid_id)        # 重新初始化摄像头
        self.webcam = True                             # 将实时摄像头设置为true
        self.a = 1
        self.cap = cv2.VideoCapture(self.vid_source)   # 初始化摄像头的对象
        th = threading.Thread(target=self.detect_vid)  # 初始化视频检测线程
        th.start()                                     # 启动线程进行检测

    def open_mp4(self):
        """打开mp4文件上传"""
        fileName, fileType = QFileDialog.getOpenFileName(self, 'Choose file', '', '*.mp4 *.avi')
        if fileName:
            # 和上面open_cam的方法类似，只是在open_cam的基础上将摄像头的源改为mp4的文件
            self.start_button_3.setEnabled(False)
            self.up_load_button_2.setEnabled(False)
            self.vid_source = fileName
            self.webcam = False
            self.cap = cv2.VideoCapture(self.vid_source)
            th = threading.Thread(target=self.detect_vid)
            th.start()

    # 视频检测主函数
    def detect_vid(self):
        """检测视频文件，这里的视频文件包含了mp4格式的视频文件和摄像头形式的视频文件"""
        # model = self.model
        vid_i = 0
        while self.cap.isOpened():
            # Read a frame from the video
            success, frame = self.cap.read()
            if success:
                # Run YOLOv8 inference on the frame
                results = self.model(frame)
                result = results[0]
                img_array = result.plot()
                # 检测 展示然后保存对应的图像结果
                im0 = img_array
                im_record = copy.deepcopy(im0)
                resize_scale = self.output_size / im0.shape[0]
                im0 = cv2.resize(im0, (0, 0), fx=resize_scale, fy=resize_scale)
                cv2.imwrite("images/tmp/single_result_vid.jpg", im0)
                if(self.a == 1):
                    self.Sx_img.setPixmap(QPixmap("images/tmp/single_result_vid.jpg"))
                else:
                    self.sp_img.setPixmap(QPixmap("images/tmp/single_result_vid.jpg"))
                time_re = str(time.strftime('result_%Y-%m-%d_%H-%M-%S_%A'))

                if vid_i % self.vid_gap == 0:
                    cv2.imwrite("record/vid/{}.jpg".format(time_re), im_record)
                # 保存txt记录文件
                # if len(txt_results) > 0:
                #     np.savetxt('record/img/{}.txt'.format(time_re), np.array(txt_results), fmt="%s %s %s %s %s %s",
                #                delimiter="\n")
                # 统计每个类别的数目，如果这个类别检测到的数量大于0，则将这个类别在界面上进行展示
                result_names = result.names
                result_nums = [0 for i in range(0, len(result_names))]
                cls_ids = list(result.boxes.cls.cpu().numpy())
                for cls_id in cls_ids:
                    result_nums[int(cls_id)] = result_nums[int(cls_id)] + 1
                result_info = ""
                for idx_cls, cls_num in enumerate(result_nums):
                    if cls_num > 0:
                        result_info = result_info + "{}:{}\n".format(result_names[idx_cls], cls_num)
                    # result_info = result_info + "{}:{}\n".format(result_names[idx_cls], cls_num)
                    # result_info = result_info + "{}:{}\n".format(result_names[idx_cls], cls_num)
                vid_i = vid_i + 1
            if cv2.waitKey(1) & self.stopEvent.is_set() == True:
                # 关闭并释放对应的视频资源
                self.stopEvent.clear()
                self.start_button_3.setEnabled(True)
                self.up_load_button_2.setEnabled(True)
                if self.cap is not None:
                    self.cap.release()
                    cv2.destroyAllWindows()
                self.reset_vid()
                break

    # 摄像头重置
    def reset_vid(self):
        """重置摄像头内容"""
        self.start_button_3.setEnabled(True)                      # 打开摄像头检测的按钮
        self.up_load_button_2.setEnabled(True)                         # 打开视频文件检测的按钮
        self.sp_img.setPixmap(QPixmap(IMAGE_VID_INIT))                # 重新设置视频检测页面的初始化图像
        self.Sx_img.setPixmap(QPixmap(IMAGE_VID_INIT))
        self.vid_source = int(self.init_vid_id)                         # 重新设置源视频源
        self.webcam = True                                              # 重新将摄像头设置为true
        self.a = 1

    def close_vid(self):
        """关闭摄像头"""
        self.a = 0
        self.stopEvent.set()
        self.reset_vid()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()