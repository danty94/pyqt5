import sys

from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    #创建QApplication类的实例
    app = QApplication(sys.argv)
    #创建一个窗口
    w = QWidget()
    #设置窗口的尺寸
    w.resize(400, 200)
    #移动窗口
    w.move(300, 300)
    w.setWindowTitle('first pyqt5 desktop application')
    w.show()

    #进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())