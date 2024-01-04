import tkinter as tk
# from PyQt5 import QtCore, QtGui, QtWidgets
# import sys
from tkinter.constants import BOTTOM, LEFT, RIGHT, TOP

from get import getData
from process import Process


"""
Qt解决方案(暂未完成)
class Window:
    def __init__(self, settings):
        self.app = QtWidgets.QApplication(sys.argv)  # 创建app
        self.widget = QtWidgets.QWidget()  # 创建窗体，选择QtWidget类
        self.widget.resize(settings['size'][0], settings['size'][1])  # 设置窗体大小
        self.widget.setWindowTitle(settings['title'])  # 设置窗体名称

        self.label = QtWidgets.QLabel(self.widget)  # 创建标签，指定父容器
        self.label.setText('Hello,World')  # 设置标签内容
        self.font = QtGui.QFont()  # 创建字体font对象
        self.font.setBold(settings['fontBold'])  # 加粗
        self.font.setFamily(settings['fontFamily'])
        self.font.setPointSize(settings['fontSize'])  # 字号
        self.label.setFont(self.font)  # 设置标签字体
        self.size = self.label.sizeHint()  # 获取最佳位置
        self.label.setGeometry(70, 60, self.size.width(), self.size.height())  # 设置标签位置
"""


class Window:
    def __init__(self, settings):
        def change(label: tk.Label, data: tk.StringVar):
            label.configure(textvariable=data)

        self.window = tk.Tk()
        # 存储变量
        self.fontFamily = settings['fontFamily']
        self.fontSize = settings['fontSize']
        self.fontBold = settings['fontBold']
        self.result = tk.StringVar(master=self.window)
        # 窗体基本信息
        self.window.geometry(f"{settings['size'][0]}x{settings['size'][1]}")
        self.window.title(settings['title'])
        # 窗体额外信息(表现为特殊窗口)
        self.window.attributes('-alpha', settings['alpha'])
        self.window.attributes('-toolwindow', True)
        self.window.attributes("-topmost", settings['topMost'])
        # 窗体内容
        self.label = tk.Label(self.window, font=(self.fontFamily, self.fontSize))
        self.label.pack(side=TOP)
        self.refresh = tk.Button(self.window, text='刷新', command=lambda: [
            # getData(),
            self.result.set(Process()),
            change(self.label, self.result)
        ])
        self.refresh.pack(side=BOTTOM)
        # 保持窗口运行
        self.window.mainloop()
