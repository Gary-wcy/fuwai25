import copy
import os
import shutil
import numpy as np
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import threading
import cv2
import torch
import os.path as osp
import time
from ultralytics import YOLO
import matplotlib.pyplot as plt

IMAGE_RIGHT_INIT = "images/resources/人像.png"
IMAGE_LEFT_INIT = "images/resources/人像_1.png"
IMAGE_VID_INIT = "images/resources/人像.png"
ICON_IMAGE = "images/resources/logo-1.png"

# 导入 UI 文件
from Main import Ui_Form as Ui_Main
from tupian_1 import Ui_Form as Ui_Page2
from duotupian_1 import Ui_Form as Ui_Page3
from shipin_1 import Ui_Form as Ui_Page4
from shexiangtou_1 import Ui_Form as Ui_Page5

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("浓烟人体识别")
        self.resize(1420, 960)

        # 创建 QStackedWidget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # 创建页面实例
        self.page1 = Ui_Main()
        self.page2 = Ui_Page2()
        self.page3 = Ui_Page3()
        self.page4 = Ui_Page4()
        self.page5 = Ui_Page5()

        # 创建 QWidget 实例并应用界面
        self.widget_page1 = QWidget()
        self.widget_page2 = QWidget()
        self.widget_page3 = QWidget()
        self.widget_page4 = QWidget()
        self.widget_page5 = QWidget()

        self.page1.setupUi(self.widget_page1)
        self.page2.setupUi(self.widget_page2)
        self.page3.setupUi(self.widget_page3)
        self.page4.setupUi(self.widget_page4)
        self.page5.setupUi(self.widget_page5)

        # 将页面添加到 QStackedWidget
        self.stacked_widget.addWidget(self.widget_page1)
        self.stacked_widget.addWidget(self.widget_page2)
        self.stacked_widget.addWidget(self.widget_page3)
        self.stacked_widget.addWidget(self.widget_page4)
        self.stacked_widget.addWidget(self.widget_page5)

        # 连接按钮点击事件
        self.page1.picture.clicked.connect(self.go_to_page2)
        self.page2.backbutton.clicked.connect(self.go_to_page1)
        self.page1.pictures.clicked.connect(self.go_to_page3)
        self.page3.backbutton.clicked.connect(self.go_to_page1)
        self.page1.video.clicked.connect(self.go_to_page4)
        self.page4.backbutton.clicked.connect(self.go_to_page1)
        self.page1.canmera.clicked.connect(self.go_to_page5)
        self.page5.backbutton.clicked.connect(self.go_to_page1)

        # 初始化变量和设置
        self.stopEvent = threading.Event()
        self.webcam = True
        self.stopEvent.clear()
        self.init_vid_id = '0'
        self.vid_source = int(self.init_vid_id)
        self.IS_vid = 0
        self.model_path = "weights/fin.pt"#hongwaiout.pt,best.pt
        self.model = self.model_load(weights=self.model_path)
        self.output_size = 480
        self.conf_thres = 0.5
        self.iou_thres = 0.5
        self.vid_gap = 30
        # 计时器用于轮流播放图片
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_next_image)
        # 图片路径列表和当前索引
        self.image_files = []
        self.current_index = 0

        # 设置初始图片
        self.page2.left_img.setPixmap(QPixmap(IMAGE_LEFT_INIT))
        self.page2.right_img.setPixmap(QPixmap(IMAGE_RIGHT_INIT))

        # 绑定其他按钮事件
        self.bind()

    def go_to_page2(self):
        # 切换到第二个页面
        self.stacked_widget.setCurrentIndex(1)

    def go_to_page1(self):
        # 切换到第一个页面
        self.stacked_widget.setCurrentIndex(0)
        self.page2.left_img.setPixmap(QPixmap(IMAGE_LEFT_INIT))
        self.page2.right_img.setPixmap(QPixmap(IMAGE_RIGHT_INIT))
        self.page3.pictures_img.setPixmap(QPixmap(IMAGE_LEFT_INIT))
        self.page4.pictures_img.setPixmap(QPixmap(IMAGE_RIGHT_INIT))
        self.page5.canmera_img.setPixmap(QPixmap(IMAGE_LEFT_INIT))
        self.page2.img_label.setText("等待检测")

    def go_to_page3(self):
        self.stacked_widget.setCurrentIndex(2)

    def go_to_page4(self):
        self.stacked_widget.setCurrentIndex(3)

    def go_to_page5(self):
        self.stacked_widget.setCurrentIndex(4)

    # 模型初始化
    @torch.no_grad()
    def model_load(self, weights=""):
        model_loaded = YOLO(weights)
        return model_loaded

    def bind(self):
        # 退出按钮
        self.page2.closebutton.clicked.connect(self.close)
        # 单图片
        self.page2.up_load_button.clicked.connect(self.upload_img)
        self.page2.start_button.clicked.connect(self.detect_img)
        #多图片
        self.page3.pictures_img.setPixmap(QPixmap(IMAGE_VID_INIT))
        self.page3.up_load_button_2.clicked.connect(self.open_folder)
        self.page3.stop_button.clicked.connect(self.closeEvent1)
        self.page3.closebutton.clicked.connect(self.closeEvent)
        #视频
        self.page4.up_load_button_2.clicked.connect(self.open_mp4)
        self.page4.stop_button.clicked.connect(self.close_vid)
        self.page4.closebutton.clicked.connect(self.closeEvent)
        #摄像头
        self.page5.up_load_button_3.clicked.connect(self.open_cam)
        self.page5.stop_button_3.clicked.connect(self.close_vid)
        self.page5.closebutton.clicked.connect(self.closeEvent)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'quit', "Are you sure?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
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
        fileName, fileType = QFileDialog.getOpenFileName(self, 'Choose file', '', '*.jpg *.png *.tif *.jpeg')
        if fileName:
            suffix = fileName.split(".")[-1]
            save_path = osp.join("images/tmp", f"tmp_upload.{suffix}")
            shutil.copy(fileName, save_path)
            im0 = cv2.imread(save_path)
            resize_scale = self.output_size / im0.shape[0]
            im0 = cv2.resize(im0, (0, 0), fx=resize_scale, fy=resize_scale)
            cv2.imwrite("images/tmp/upload_show_result.jpg", im0)
            self.img2predict = save_path
            self.page2.left_img.setPixmap(QPixmap("images/tmp/upload_show_result.jpg"))
            self.page2.right_img.setPixmap(QPixmap(IMAGE_RIGHT_INIT))

    def detect_img(self):
        output_path = "images/tmp/enhanced_image.jpg"
        self.enhance_infrared_image(self.img2predict,output_path)
        output_size = self.output_size
        results = self.model(output_path, conf=self.conf_thres)
        result = results[0]
        img_array = result.plot()
        im0 = img_array
        im_record = copy.deepcopy(im0)
        resize_scale = output_size / im0.shape[0]
        im0 = cv2.resize(im0, (0, 0), fx=resize_scale, fy=resize_scale)
        cv2.imwrite("images/tmp/single_result.jpg", im0)
        self.page2.right_img.setPixmap(QPixmap("images/tmp/single_result.jpg"))
        time_re = time.strftime('result_%Y-%m-%d_%H-%M-%S_%A')
        cv2.imwrite(f"record/img/{time_re}.jpg", im_record)

        result_names = result.names
        result_nums = [0 for i in range(0, len(result_names))]
        cls_ids = list(result.boxes.cls.cpu().numpy())
        for cls_id in cls_ids:
            result_nums[int(cls_id)] = result_nums[int(cls_id)] + 1
        result_info = ""
        for idx_cls, cls_num in enumerate(result_nums):
            # 添加对数据0的判断，如果当前数据的数目为0，则这个数据不需要加入到里面
            if cls_num > 0:
                result_info = "检测人数 : {}\n".format(cls_num)
        self.page2.img_label.setText("{}".format(result_info))

    def open_cam(self):
        """打开摄像头上传"""
        self.page5.up_load_button_3.setEnabled(False)    # 将打开摄像头的按钮设置为false，防止用户误触
        self.page4.up_load_button_2.setEnabled(False)       # 将打开mp4文件的按钮设置为false，防止用户误触
        self.page4.stop_button.setEnabled(True)
        self.page5.stop_button_3.setEnabled(True)# 将关闭按钮打开，用户可以随时点击关闭按钮关闭实时的检测任务
        self.vid_source = int(self.init_vid_id)        # 重新初始化摄像头
        self.webcam = True                             # 将实时摄像头设置为true
        self.IS_vid = 1
        self.cap = cv2.VideoCapture(self.vid_source)   # 初始化摄像头的对象
        th = threading.Thread(target=self.detect_vid)  # 初始化视频检测线程
        th.start()                                     # 启动线程进行检测

    def open_mp4(self):
        """打开mp4文件上传"""
        fileName, fileType = QFileDialog.getOpenFileName(self, 'Choose file', '', '*.mp4 *.avi')
        if fileName:
            self.page4.up_load_button_2.setEnabled(False)
            self.page5.up_load_button_3.setEnabled(False)
            self.vid_source = fileName
            self.webcam = False
            self.IS_vid=0
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
                frame=self.enhance_frame(frame)
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
                if(self.IS_vid == 1):
                    self.page5.canmera_img.setPixmap(QPixmap("images/tmp/single_result_vid.jpg"))
                else:
                    self.page4.pictures_img.setPixmap(QPixmap("images/tmp/single_result_vid.jpg"))
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
                        result_info = result_info + "{} : {}\n".format(result_names[idx_cls], cls_num)
                    # result_info = result_info + "{}:{}\n".format(result_names[idx_cls], cls_num)
                    # result_info = result_info + "{}:{}\n".format(result_names[idx_cls], cls_num)
                self.page4.vid_label.setText("当前检测结果：\n {}".format(result_info))
                self.page5.vid_label.setText("当前检测结果：\n {}".format(result_info))
                vid_i = vid_i + 1
            if cv2.waitKey(1) & self.stopEvent.is_set() == True:
                # 关闭并释放对应的视频资源
                self.stopEvent.clear()
                self.page5.up_load_button_3.setEnabled(True)
                self.page4.up_load_button_2.setEnabled(True)
                if self.cap is not None:
                    self.cap.release()
                    cv2.destroyAllWindows()
                self.reset_vid()
                break

    def open_folder(self):
        """打开文件夹并读取其中的图片"""
        folder_path = QFileDialog.getExistingDirectory(self, "选择图片文件夹")
        if folder_path:
            self.load_images_from_folder(folder_path)

    def load_images_from_folder(self, folder_path):
        """从文件夹中加载图片"""
        # 获取文件夹中所有文件的列表
        file_list = os.listdir(folder_path)
        # 筛选图片文件
        self.image_files = []
        for file in file_list:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                self.image_files.append(os.path.join(folder_path, file))

        # 如果有图片文件，开始轮流播放
        if self.image_files:
            self.current_index = 0
            self.display_image(self.image_files[self.current_index])
            print(f"找到 {len(self.image_files)} 张图片")
            # 启动计时器，每3秒切换一次图片
            self.timer.start(25)
        else:
            print("未找到任何图片")

    def display_image(self, image_path):
        """在标签中显示图片"""
        # 对图片进行增强处理
        enhanced_image_path = self.enhance_image(image_path)

        # 加载增强后的图片
        pixmap = QPixmap(enhanced_image_path)
        pixmap = self.process_image(pixmap)

        if not pixmap.isNull():
            # 缩放图片以适应标签大小
            pixmap = pixmap.scaled(self.page2.label.width(), self.page2.label.height(), Qt.KeepAspectRatio)
            self.page3.pictures_img.setPixmap(pixmap)
            print(self.current_index)
        else:
            print(f"无法加载图片: {image_path}")

    def show_next_image(self):
        """显示下一张图片"""
        self.current_index = (self.current_index + 1) % len(self.image_files)
        self.display_image(self.image_files[self.current_index])

    def closeEvent1(self, event):
        """关闭窗口时停止计时器"""
        self.timer.stop()
        self.reset_vid()

    def process_image(self, pixmap):
        """处理图片的函数"""
        if not pixmap.isNull():
            # 将 QPixmap 转换为 QImage
            qimage = pixmap.toImage()

            # 将 QImage 转换为 OpenCV 格式的图像
            cv_image = self.qimage_to_cv(qimage)

            # 使用 YOLO 模型进行推理
            results = self.model(cv_image, conf=self.conf_thres)  # 读取图像并执行检测的逻辑
            result = results[0]  # 获取检测结果
            img_array = result.plot()  # 在图像上绘制检测结果

            result_names = result.names
            result_nums = [0 for i in range(0, len(result_names))]
            cls_ids = list(result.boxes.cls.cpu().numpy())
            for cls_id in cls_ids:
                result_nums[int(cls_id)] = result_nums[int(cls_id)] + 1
            result_info = ""
            for idx_cls, cls_num in enumerate(result_nums):
                # 添加对数据0的判断，如果当前数据的数目为0，则这个数据不需要加入到里面
                if cls_num > 0:
                    result_info = result_info + "{} : {}\n".format(result_names[idx_cls], cls_num)
            self.page3.imgs_label.setText("当前检测结果：\n {}".format(result_info))

            # 将检测结果转换回 QPixmap
            pixmap = QPixmap.fromImage(self.cv_to_qimage(img_array))

        return pixmap

    def qimage_to_cv(self, qimage):
        """将 QImage 转换为 OpenCV 格式的图像"""
        # 获取 QImage 的尺寸
        width = qimage.width()
        height = qimage.height()
        qimage = qimage.convertToFormat(QImage.Format_RGB888)
        byte_array = qimage.bits().tobytes()
        cv_image = np.frombuffer(byte_array, np.uint8).reshape(height, width, 3)
        return cv_image

    def cv_to_qimage(self, cv_image):
        """将 OpenCV 格式的图像转换为 QImage"""
        # 将 OpenCV 图像转换为 RGB 格式
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        height, width, channel = cv_image.shape
        bytes_per_line = 3 * width
        qimage = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return qimage

    # 摄像头重置
    def reset_vid(self):
        """重置摄像头内容"""
        self.page5.up_load_button_3.setEnabled(True)                      # 打开摄像头检测的按钮
        self.page4.up_load_button_2.setEnabled(True)                         # 打开视频文件检测的按钮
        self.page4.pictures_img.setPixmap(QPixmap(IMAGE_VID_INIT))                # 重新设置视频检测页面的初始化图像
        self.page5.canmera_img.setPixmap(QPixmap(IMAGE_VID_INIT))
        self.vid_source = int(self.init_vid_id)                         # 重新设置源视频源
        self.webcam = True                                              # 重新将摄像头设置为true
        self.IS_vid = 1

    def close_vid(self):
        """关闭摄像头"""
        self.model_path = "weights/fin.pt"  # hongwaiout.pt,best.pt
        self.model = self.model_load(weights=self.model_path)
        self.IS_vid = 0
        self.stopEvent.set()
        self.reset_vid()

    #图片处理
    @staticmethod
    def enhance_infrared_image(image_path, output_path, save_steps=False):
        smoke_n = 0.5  # 可以视情况调整

        # 只计算处理时间（不包括I/O）
        process_start = time.time()

        # 读取图像不计入处理时间
        ir_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        if ir_image is None:
            raise ValueError(f"无法读取图像: {image_path}")

        ir_image = cv2.resize(cv2.cvtColor(ir_image, cv2.COLOR_BGR2RGB),
                              (960, 540), interpolation=cv2.INTER_AREA)

        if save_steps:
            plt.imsave(f"{os.path.splitext(output_path)[0]}_1_original.png", ir_image)

        gray = cv2.cvtColor(ir_image, cv2.COLOR_RGB2GRAY)

        clahe = cv2.createCLAHE(clipLimit=1.2, tileGridSize=(8, 8))
        enhanced = clahe.apply(gray)

        denoised = cv2.fastNlMeansDenoising(
            enhanced, None, h=7,
            templateWindowSize=5,
            searchWindowSize=5
        )

        small_img = cv2.resize(denoised, (256, 256), interpolation=cv2.INTER_AREA)
        p_low, p_high = np.percentile(small_img, [2, 98])
        stretched = np.clip((denoised.astype(np.float32) - p_low) * 255.0 / (p_high - p_low), 0, 255)

        gamma = 0.7 - 0.05 * smoke_n
        gamma_corrected = np.power(stretched / 255.0, gamma) * 255.0

        lab = cv2.cvtColor(gamma_corrected.astype(np.uint8), cv2.COLOR_GRAY2RGB)
        lab = cv2.cvtColor(lab, cv2.COLOR_RGB2LAB)
        l, a, b = cv2.split(lab)
        l = cv2.createCLAHE(clipLimit=1.0).apply(l)
        enhanced_lab = cv2.cvtColor(cv2.merge((l, a, b)), cv2.COLOR_LAB2RGB)

        # 处理结束时间点（保存前）
        process_time = time.time() - process_start

        # 保存图像不计入处理时间
        plt.imsave(output_path, enhanced_lab)

        print(f'处理完成 {os.path.basename(image_path)}，处理耗时: {process_time:.2f}秒')

    def enhance_frame(self, frame):
        # 将帧保存为临时文件
        temp_path = "images/tmp/temp_frame.jpg"
        cv2.imwrite(temp_path, frame)

        # 调用 enhance_infrared_image 函数进行增强
        enhanced_path = "images/tmp/enhanced_frame.jpg"
        self.enhance_infrared_image(temp_path, enhanced_path, save_steps=False)

        # 读取增强后的图像
        enhanced_frame = cv2.imread(enhanced_path)

        # 删除临时文件
        os.remove(temp_path)

        return enhanced_frame

    def enhance_image(self, image_path):
        """对图片进行增强处理"""
        # 生成增强后的图片保存路径
        base_name = os.path.basename(image_path)
        enhanced_image_path = os.path.join("images/tmp", f"enhanced_{base_name}")

        # 调用 enhance_infrared_image 函数进行增强
        MainWindow.enhance_infrared_image(image_path, enhanced_image_path, save_steps=False)

        return enhanced_image_path

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()