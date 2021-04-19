from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


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


class AllClassesCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.tight_layout()
        fig.patch.set_facecolor("black")
        super(AllClassesCanvas, self).__init__(fig)


class GeneratedSamplesCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.tight_layout()
        fig.patch.set_facecolor("black")
        spec2 = gridspec.GridSpec(ncols=2, nrows=3, figure=fig)
        self.ax1 = fig.add_subplot(spec2[0, 0])
        self.ax2 = fig.add_subplot(spec2[0, 1])
        self.ax3 = fig.add_subplot(spec2[1, 0])
        self.ax4 = fig.add_subplot(spec2[1, 1])
        self.ax5 = fig.add_subplot(spec2[2, 0])
        self.ax6 = fig.add_subplot(spec2[2, 1])
        super(GeneratedSamplesCanvas, self).__init__(fig)



class SeabornCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig, self.ax = plt.subplots(figsize=(width, height))
        super(SeabornCanvas, self).__init__(fig)
