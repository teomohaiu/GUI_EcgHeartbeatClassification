import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from UiFunctions.PredictionPage import Prediction
from UiFunctions.DatasetPage import Dataset
from ui_modified import Ui_MainWindow


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.animation = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Btn_Toggle.clicked.connect(lambda: self.toggleMenu(250, True))
        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        ##### PAGE 1 FUNCTIONS #####
        self.prediction_page = Prediction()
        toolbar = NavigationToolbar(self.prediction_page.sc, self)
        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.prediction_page.sc)
        self.ui.showEcg.setLayout(layout)
        self.ui.predictBtn.clicked.connect(self.prediction_page.predictClick)

        ##### PAGE 2 FUNCTIONS #####
        self.dataset_page = Dataset()

        layoutDataDistribution = QVBoxLayout()

        layoutDataDistribution.addWidget(self.dataset_page.sc)
        self.ui.widgetClass.setLayout(layoutDataDistribution)

        layoutClassExamples = QVBoxLayout()
        layoutClassExamples.addWidget(self.dataset_page.classes_plot)
        self.ui.widgetViewClasses.setLayout(layoutClassExamples)

        layoutGeneratedSamples = QVBoxLayout()
        layoutGeneratedSamples.addWidget(self.dataset_page.generated_plot)
        self.ui.widgetSMOTE.setLayout(layoutGeneratedSamples)


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
