import sys
import os
import numpy as np
import time

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPropertyAnimation, QThread, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QDialog, QFileDialog, QMessageBox
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from KerasModel import Model
from UiFunctions.PredictionPage import Prediction
from UiFunctions.DatasetPage import Dataset
from UiFunctions.StatisticsPage import Statistics
from ui_modified import Ui_MainWindow
from ui_dialog import Ui_Dialog
from ProgressBar import ProgressBarMain


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.animation = None
        self.uploadedRecord = None
        self.uploadedAnnotation = None
        self.firstOpenDialog = True

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Dialog = QDialog()
        self.ui_di = Ui_Dialog()
        self.ui_di.setupUi(self.Dialog)

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
        # self.ui.predictBtn.clicked.connect(self.progressBarAndPrediction)

        self.ui.uploadFileBtn.clicked.connect(self.uploadFileClick)

        #### Upload file dialog functions ####
        self.ui_di.browseFileButton.clicked.connect(self.browseFileClick)
        self.ui_di.browseAnnotationButton.clicked.connect(self.browseAnnotationClick)

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

        #### PAGE 3 FUNCTIONS ####
        statisticsPage = Statistics()
        layoutStatistics = QVBoxLayout()
        layoutStatistics.addWidget(statisticsPage.sc)
        self.ui.widgetStatistics.setLayout(layoutStatistics)

    def browseAnnotationClick(self):
        self.uploadedAnnotation, _ = QFileDialog.getOpenFileName(None, "Browse for annotations", "",
                                                                 " ATR Files (*.atr);;Text files (*.txt)")
        if self.uploadedAnnotation:
            print(self.uploadedAnnotation)
            self.ui_di.textEdit_2.setText(self.uploadedAnnotation)

    def browseFileClick(self):
        self.uploadedRecord, _ = QFileDialog.getOpenFileName(None, "Browse for ecg files", "", "Data files(*.dat);; "
                                                                                               "Text files (*.txt)")
        if self.uploadedRecord:
            print(self.uploadedRecord)
            self.ui_di.textEdit.setText(self.uploadedRecord)

    def uploadFileClick(self):
        if self.uploadedRecord is not None and self.uploadedAnnotation is not None:
            self.uploadedRecord = None
            self.uploadedAnnotation = None
            self.ui_di.textEdit.setText("")
            self.ui_di.textEdit_2.setText("")

        self.Dialog.show()
        dialog_response = self.Dialog.exec_()

        if dialog_response == QDialog.Accepted:
            print('OK WAS PRESSED')
            if self.uploadedRecord is None and self.uploadedAnnotation is None:
                ret = QMessageBox.question(self, 'Allert', "You didn't select a signal!",
                                           QMessageBox.Ok | QMessageBox.Cancel)

            else:
                if self.uploadedRecord.endswith('.dat') and self.uploadedAnnotation.endswith('.atr'):
                    record = os.path.splitext(self.uploadedRecord)[0]
                    annotation = os.path.splitext(self.uploadedAnnotation)[0]

                    try:
                        self.prediction_page.keras_model.read_signal(record, annotation)
                        self.prediction_page.keras_model.preprocess()
                        self.prediction_page.sc.axes.clear()
                        print('Signal from main:', self.prediction_page.keras_model.signal)
                        self.prediction_page.sc.axes.plot(self.prediction_page.keras_model.signal)
                        self.prediction_page.sc.draw()
                    except AttributeError as e:
                        print(e)

        else:
            print("Cancel was pressed")

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
