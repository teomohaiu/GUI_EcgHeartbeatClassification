from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QSpacerItem, QSizePolicy, QWidget, QHBoxLayout, QPushButton, QScrollArea, QVBoxLayout, \
    QLabel, QFrame


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 700)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        qss_file = open('stylesheets/stylesheet.qss').read()
        MainWindow.setStyleSheet(qss_file)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 60))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(150, 60))
        self.frame_toggle.setStyleSheet("background-color: rgb(32,178,170);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "border: 0px solid;")
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_page_1 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_1.setMinimumSize(QtCore.QSize(0, 40))

        qss_file_menu_btns = open('stylesheets/pageBtnStylesheet.qss').read()

        self.btn_page_1.setStyleSheet(qss_file_menu_btns)
        self.btn_page_1.setObjectName("btn_page_1")
        self.verticalLayout_4.addWidget(self.btn_page_1)
        self.btn_page_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_2.setMinimumSize(QtCore.QSize(0, 40))

        self.btn_page_2.setStyleSheet(qss_file_menu_btns)
        self.btn_page_2.setObjectName("btn_page_2")
        self.verticalLayout_4.addWidget(self.btn_page_2)
        self.btn_page_3 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_3.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_page_3.setStyleSheet(qss_file_menu_btns)
        self.btn_page_3.setObjectName("btn_page_3")
        self.verticalLayout_4.addWidget(self.btn_page_3)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.uploadFileBtn = QPushButton(self.page_1)
        self.uploadFileBtn.setObjectName(u"uploadFileBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.uploadFileBtn.sizePolicy().hasHeightForWidth())
        self.uploadFileBtn.setSizePolicy(sizePolicy1)
        self.uploadFileBtn.setStyleSheet("QPushButton\n"
            "{\n"
            "    height: 20px; \n"
            "    width: 100px; \n"
            "    min-width: 40px;\n"
            "}\n")

        self.horizontalLayout_5.addWidget(self.uploadFileBtn)

        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.showEcg = QWidget(self.page_1)
        self.showEcg.setObjectName(u"showEcg")
        sizePolicy.setHeightForWidth(self.showEcg.sizePolicy().hasHeightForWidth())
        self.showEcg.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.showEcg)


        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_7.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_7.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.predictBtn = QtWidgets.QPushButton(self.page_1)
        self.predictBtn.setObjectName("predictBtn")

        self.predictBtn.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "    height: 40px; \n"
            "    width: 150px; \n"
            "    min-width: 40px;\n"
            "}\n"

        )
        self.horizontalLayout_3.addWidget(self.predictBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)


        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.scrollArea = QScrollArea(self.page_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1076, 1000))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy2)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 1700))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.textLabelClass = QLabel(self.scrollAreaWidgetContents)
        self.textLabelClass.setObjectName(u"textLabelClass")
        sizePolicy2.setHeightForWidth(self.textLabelClass.sizePolicy().hasHeightForWidth())
        self.textLabelClass.setSizePolicy(sizePolicy2)
        self.textLabelClass.setMinimumSize(QSize(0, 10))
        font = QFont()
        font.setFamily(u"Bahnschrift Light Condensed")
        font.setPointSize(16)
        self.textLabelClass.setFont(font)
        self.textLabelClass.setAutoFillBackground(False)

        self.verticalLayout_11.addWidget(self.textLabelClass)

        self.widgetClass = QWidget(self.scrollAreaWidgetContents)
        self.widgetClass.setObjectName(u"widgetClass")

        self.verticalLayout_11.addWidget(self.widgetClass)

        self.widgetViewClasses = QWidget(self.scrollAreaWidgetContents)
        self.widgetViewClasses.setObjectName(u"widgetViewClasses")

        self.verticalLayout_11.addWidget(self.widgetViewClasses)

        self.textLabelSMOTE = QLabel(self.scrollAreaWidgetContents)
        self.textLabelSMOTE.setObjectName(u"textLabelSMOTE")
        sizePolicy2.setHeightForWidth(self.textLabelSMOTE.sizePolicy().hasHeightForWidth())
        self.textLabelSMOTE.setSizePolicy(sizePolicy2)
        self.textLabelSMOTE.setMinimumSize(QSize(10, 0))
        self.textLabelSMOTE.setFont(font)
        self.textLabelSMOTE.setStyleSheet(u"QLabel: {\n"
                                          "	\n"
                                          "	color: rgb(255, 255, 255);\n"
                                          "}")

        self.verticalLayout_11.addWidget(self.textLabelSMOTE)

        self.widgetSMOTE = QWidget(self.scrollAreaWidgetContents)
        self.widgetSMOTE.setObjectName(u"widgetSMOTE")

        self.verticalLayout_11.addWidget(self.widgetSMOTE)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.page_2)


        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.scrollArea_2 = QScrollArea(self.page_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1069, 700))
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy2)
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(0, 700))

        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.clfReportLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.clfReportLabel.setObjectName(u"clfReportLabel")
        sizePolicy2.setHeightForWidth(self.clfReportLabel.sizePolicy().hasHeightForWidth())
        self.clfReportLabel.setSizePolicy(sizePolicy2)
        self.clfReportLabel.setMinimumSize(QSize(0, 10))
        self.clfReportLabel.setFont(font)
        self.clfReportLabel.setAutoFillBackground(False)

        self.verticalLayout_9.addWidget(self.clfReportLabel)

        self.widgetStatistics = QWidget(self.scrollAreaWidgetContents_2)
        self.widgetStatistics.setObjectName(u"widgetStatistics")
        #self.widgetStatistics.setGeometry(QRect(10, 60, 1200, 500))

        self.verticalLayout_9.addWidget(self.widgetStatistics)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)



        '''
      
        self.widgetStatistics = QWidget(self.scrollAreaWidgetContents_2)
        self.widgetStatistics.setObjectName(u"widgetStatistics")
        self.widgetStatistics.setGeometry(QRect(10, 60, 1200, 500))
        self.clfReportLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.clfReportLabel.setObjectName(u"clfReportLabel")
        self.clfReportLabel.setGeometry(QRect(10, 10, 1047, 36))
        sizePolicy2.setHeightForWidth(self.clfReportLabel.sizePolicy().hasHeightForWidth())
        self.clfReportLabel.setSizePolicy(sizePolicy2)
        self.clfReportLabel.setMinimumSize(QSize(0, 10))
        self.clfReportLabel.setFont(font)
        self.clfReportLabel.setAutoFillBackground(False)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

     '''
        self.verticalLayout_8.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ECG Heartbeat Classification"))
        self.Btn_Toggle.setText(_translate("MainWindow", "MENU"))
        self.btn_page_1.setText(_translate("MainWindow", "PREDICTION"))
        self.btn_page_2.setText(_translate("MainWindow", "DATASET "))
        self.btn_page_3.setText(_translate("MainWindow", "STATISTICS"))
        self.predictBtn.setText(_translate("MainWindow", "PREDICT"))
        self.uploadFileBtn.setText(_translate("MainWindow", "Upload file"))
        self.textLabelClass.setText(_translate("MainWindow", u"Class representation", None))
        self.textLabelSMOTE.setText(_translate("MainWindow", u"SMOTE generated examples", None))
        self.clfReportLabel.setText(_translate("MainWindow", u"Classification report", None))


