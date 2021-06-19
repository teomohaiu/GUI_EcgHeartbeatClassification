from PyQt5.QtGui import QColor

from ui_splash_screen import Ui_SplashScreen
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5 import QtCore
import sys

counter = 0


class ProgressBarMain(QMainWindow):
    def __init__(self):
        super(ProgressBarMain, self).__init__()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.progressBarValue(50)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(117, 255, 255, 110))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

    def progress(self):
        global counter

        self.progressBarValue(counter)

        htmlText = """
        <p><span style=" font-size:60pt;">{VALUE}</span><span style=" font-size:45pt; vertical-align:super;">%</span></p>
        """

        newHtml= htmlText.replace("{VALUE}", str(counter))
        self.ui.labelPercentage.setText(newHtml)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            self.timer.stop()
            self.close()

        counter += 1

    def progressBarValue(self, value):
        stylesheet = """QFrame{ border-radius: 150px; background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, 
        stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(117, 255, 255,255)); } 
        """

        progress = (100 - value) / 100.0
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        newStyleSheet = stylesheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
        self.ui.circularProgress.setStyleSheet(newStyleSheet)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = ProgressBarMain()
    window.show()
    sys.exit(app.exec_())
