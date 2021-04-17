import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import numpy as np

from Canvas import MplCanvas
from KerasModel import Model
from ui_modified import Ui_MainWindow


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.isPredicted = False

        self.ui.Btn_Toggle.clicked.connect(lambda: self.toggleMenu(250, True))
        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        self.keras_model = Model()

        self.sc = self.plot_ecg(self.keras_model.signal)

        toolbar = NavigationToolbar(self.sc, self)
        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)

        self.ui.showEcg.setLayout(layout)
        self.ui.predictBtn.clicked.connect(self.predictClick)

    def plot_ecg(self, signal):
        sc = MplCanvas(self, width=4, height=4, dpi=100)
        sc.axes.plot(signal, color='teal')
        sc.axes.set(facecolor="black")
        sc.figure.subplots_adjust(top=0.875, bottom=0.101, left=0.064, right=0.985, hspace=0.2, wspace=0.2)

        for ax in sc.axes.spines.values():
            ax.set_color("white")
        sc.axes.spines['top'].set_visible(False)
        sc.axes.spines['right'].set_visible(False)
        sc.axes.tick_params(colors='white', which='both')

        return sc

    def predictClick(self):
        self.isPredicted = True
        predicted_classes, probabilities = self.keras_model.predict()

        colors = cm.rainbow(np.linspace(0, 1, len(self.keras_model.sequence_start)))
        for i, c in zip(range(len(self.keras_model.sequence_start)), colors):
            self.sc.axes.axvline(color=c, x=self.keras_model.sequence_start[i])
            self.sc.axes.axvline(color=c, x=self.keras_model.sequence_end[i])
            self.sc.axes.axvspan(self.keras_model.sequence_start[i], self.keras_model.sequence_end[i], color=c,
                                 alpha=0.2)

            self.sc.axes.text(self.keras_model.beat_location[i], 1.1,
                              "{} \n ({}%)".format(predicted_classes[i], probabilities[i]),
                              horizontalalignment='center',
                              color= 'white',
                              verticalalignment='center', bbox=dict(facecolor=c, alpha=0.5))

        self.sc.draw()

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 150

            # SET MAX WIDTH
            if width == 150:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icons/ecg-icon.png'))

    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
