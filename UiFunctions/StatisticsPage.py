import pickle

import pandas as pd
import seaborn as sns

from Canvas import MultipleSubplotsCanvas, SeabornCanvas


class Statistics:
    def __init__(self):
        self.sc = self.plot()

    def plot(self):
        sc = SeabornCanvas(self, 3, 4, 100)
        smote_15_classes = pickle.load(open('SerializedObjects/statistics/smote_15_classes.pkl', 'rb'))
        sns.heatmap(pd.DataFrame(smote_15_classes).iloc[:-1, :].T, annot=True, ax=sc.ax)

        return sc

    def plot_statistics(self):
        sc = MultipleSubplotsCanvas(self, 4, 3, 100)
        smote_5_categories = pickle.load(open('SerializedObjects/statistics/smote_5_categories.pkl', 'rb'))
        smote_15_classes = pickle.load(open('SerializedObjects/statistics/smote_15_classes.pkl', 'rb'))
        smote_5_categories = pd.DataFrame(smote_5_categories)
        smote_15_classes = pd.DataFrame(smote_15_classes)
        # sns.heatmap(smote_15_classes.iloc[:-1,:].T, annot=True, ax=sc.ax1)
        sns.heatmap(smote_15_classes.iloc[:-1, :].T, annot=True, ax=sc.ax1, vmin=0, vmax=1.0, fmt='0.2f', cbar=False,
                    annot_kws={"size": 14})
        sc.ax1.tick_params(colors='white', which='both', labelsize=9)
        sc.ax1.set_title('Classification report 15 classes', color='white')
        sc.ax2.tick_params(colors='white', which='both', labelsize=8)
        sc.ax2.set_title('Classification report 5 category', color='white')
        sns.heatmap(smote_5_categories.iloc[:-1, :].T, annot=True, ax=sc.ax2, vmin=0, vmax=1.0, fmt='0.2f', cbar=False,
                    annot_kws={"size": 14})

        return sc
