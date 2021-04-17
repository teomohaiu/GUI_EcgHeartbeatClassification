from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backend_bases import NavigationToolbar2
import matplotlib.pyplot as plt
import seaborn as sns


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.tight_layout()
        fig.patch.set_facecolor("black")
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MultipleSubplotsCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.tight_layout()
        fig.patch.set_facecolor("black")
        self.ax1 = fig.add_subplot(121)
        self.ax2 = fig.add_subplot(122)
        super(MultipleSubplotsCanvas, self).__init__(fig)


class SeabornCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig, self.ax = plt.subplots(figsize=(width, height))
        super(SeabornCanvas, self).__init__(fig)

