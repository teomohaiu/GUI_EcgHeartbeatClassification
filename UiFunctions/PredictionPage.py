import numpy as np
from matplotlib.pyplot import cm

from Canvas import MplCanvas
from KerasModel import Model


class Prediction:
    def __init__(self):
        self.isPredicted = False
        self.keras_model = Model()
        self.sc = self.plot_ecg(self.keras_model.signal)

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
                              color='white',
                              verticalalignment='center', bbox=dict(facecolor=c, alpha=0.5))

        self.sc.draw()
