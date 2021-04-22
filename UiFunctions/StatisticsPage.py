from Canvas import MplCanvas
import seaborn as sns
import pandas as pd
import pickle


class Statistics:
    def __init__(self):
        self.sc = self.plot_statistics()

    def plot_statistics(self):
        sc = MplCanvas(self, 5, 5, 100)
        smote_5_categories = pickle.load(open('SerializedObjects/statistics/smote_5_categories.pkl', 'rb'))
        smote_5_categories = pd.DataFrame(smote_5_categories)
        sns.heatmap(smote_5_categories.iloc[:-1, :].T, annot=True, ax=sc.axes, vmin=0, vmax=1.0, fmt='0.2f', cbar=False,
                    annot_kws={"size": 14})
        sc.axes.tick_params(colors='white', which='both', labelsize=14)

        return sc
