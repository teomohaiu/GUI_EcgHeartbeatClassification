from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 280)
        qss_file = open('stylesheets/stylesheet.qss').read()
        Dialog.setStyleSheet(qss_file)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QRect(30, 200, 331, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.fileLabel = QtWidgets.QLabel(Dialog)
        self.fileLabel.setGeometry(QtCore.QRect(40, 70, 131, 31))
        self.fileLabel.setObjectName("fileLabel")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(210, 70, 161, 31))
        self.textEdit.setObjectName("textEdit")
        self.browseFileButton = QtWidgets.QPushButton(Dialog)
        self.browseFileButton.setGeometry(QtCore.QRect(380, 70, 121, 31))
        self.browseFileButton.setObjectName("browseFileButton")
        self.annotationLabel = QtWidgets.QLabel(Dialog)
        self.annotationLabel.setGeometry(QtCore.QRect(20, 120, 181, 31))
        self.annotationLabel.setObjectName("annotationLabel")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(210, 120, 161, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.browseAnnotationButton = QtWidgets.QPushButton(Dialog)
        self.browseAnnotationButton.setGeometry(QtCore.QRect(380, 120, 161, 31))
        self.browseAnnotationButton.setObjectName("browseAnnotationButton")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Upload file"))
        self.fileLabel.setText(_translate("Dialog", "Load ecg file:"))
        self.browseFileButton.setText(_translate("Dialog", "Browse file"))
        self.annotationLabel.setText(_translate("Dialog", "(Optional) Load annotation file:"))
        self.browseAnnotationButton.setText(_translate("Dialog", "Browse annotation file"))
