from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        """
        This function initialize a FigureCanvas so it can be compatible with matplotlib figure.

        :param parent: specify the parent widget if it exists
        :param width: the width of the figure
        :param height: the height of the figure
        :param dpi: dots per inch - clarity of the figure
        """
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.tight_layout()
        fig.patch.set_facecolor("black")
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MultipleSubplotsCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        """
        This function initialize a FigureCanvas suitable for displaying a figure on a widget,
        and adds two subplots on a figure.

        :param parent: specify the parent widget if it exists
        :param width: the width of the figure
        :param height: the height of the figure
        :param dpi: dots per inch - clarity of the figure
        """
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.tight_layout()
        fig.patch.set_facecolor("black")
        self.ax1 = fig.add_subplot(121)
        self.ax2 = fig.add_subplot(122)
        super(MultipleSubplotsCanvas, self).__init__(fig)


class AllClassesCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        """
        This function initialize a figure with no subplots for displaying all classes
        on the dataset page.

        :param parent: specify the parent widget if it exists
        :param width: the width of the figure
        :param height: the height of the figure
        :param dpi: dots per inch - clarity of the figure
        """
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.tight_layout()
        fig.patch.set_facecolor("black")
        super(AllClassesCanvas, self).__init__(fig)


class GeneratedSamplesCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        """
        This function initialize a figure with 6 subplots for displaying the real
        and generated signals on the ui.

        :param parent: specify the parent widget if it exists
        :param width: the width of the figure
        :param height: the height of the figure
        :param dpi: dots per inch - clarity of the figure
        """
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
        """
        This functions initialize a figure and is used for displaying the seaborn
        figure on the statistics page.

        :param parent: specify the parent widget if it exists
        :param width: the width of the figure
        :param height: the height of the figure
        :param dpi: dots per inch - clarity of the figure
        """
        fig, self.ax = plt.subplots(figsize=(width, height))
        fig.tight_layout()
        fig.patch.set_facecolor("dimgray")
        super(SeabornCanvas, self).__init__(fig)
