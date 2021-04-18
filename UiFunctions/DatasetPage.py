import numpy as np
import pandas as pd
from Canvas import MultipleSubplotsCanvas, SeabornCanvas
import seaborn as sns


class Dataset:
    def __init__(self):
        self.sc = self.plot_imbalanced_classes()
        # self.sc = self.example_seaborn()

    def plot_imbalanced_classes(self):
        sc = MultipleSubplotsCanvas(self, width=5, height=4)
        available_categories = np.load('SerializedObjects/class_symbols.npy')
        imbalanced_classes = np.load('SerializedObjects/imbalanced_classes.npy')
        augmented_classes = np.load('SerializedObjects/augmented_classes.npy')
        legend_labels = np.load('SerializedObjects/legend_labels.npy')

        colors = sns.color_palette("plasma", n_colors=15)
        for j in range(len(available_categories)):
            sc.ax1.bar(available_categories[j], imbalanced_classes[j], label=available_categories[j], color=colors[j])
            sc.ax2.bar(available_categories[j], augmented_classes[j], label=available_categories[j], color=colors[j])

        for a, b in zip(sc.ax1.spines.values(), sc.ax2.spines.values()):
            a.set_color('white')
            b.set_color('white')

        sc.ax1.set_title('Train distribution before augmentation', color='white', fontsize=13)
        sc.ax1.set(facecolor='black')
        sc.ax1.tick_params(colors='white', which='both')
        sc.ax1.set_xlabel('Classes', color='white', fontsize=13)
        sc.ax1.set_ylabel('Nr. of samples', color='white', fontsize=13)

        sc.ax2.set(facecolor='black')
        sc.ax2.set_title('Train distribution after augmentation', color='white', fontsize=13)
        sc.ax2.tick_params(colors='white', which='both')
        sc.ax2.set_xlabel('Classes', color='white', fontsize=13)

        lines, _ = sc.figure.axes[-1].get_legend_handles_labels()
        sc.figure.legend(lines, legend_labels, loc='upper right', bbox_to_anchor=(1, 0.8), prop={'size': 8})
        sc.figure.subplots_adjust(top=0.88, bottom=0.145, left=0.11, right=0.76, hspace=0.2, wspace=0.2)

        return sc

    def example_seaborn(self):
        sc = SeabornCanvas(self, width=5, height=5)
        Mydict = {'Province': ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Newfoundland & Labrador',
                               'Northwest Territories', 'Nova Scotia', 'Nunavut', 'Ontario', 'Prince Edward Island',
                               'Quebec', 'Saskatchewan', 'Yukon'],
                  'Province_Code': ['AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT'],
                  'Minimum_Wage': ['15.00', '14.60', '11.65', '11.70', '11.65', '13.46', '12.55', '13.00', '14.00',
                                   '12.85', '13.10', '11.32', '13.71']}
        df = pd.DataFrame(Mydict)
        # change the datatype of minimum wage from object to float
        df['Minimum_Wage'] = df['Minimum_Wage'].astype(str).astype(float)
        print(df.dtypes)
        sns.barplot(x='Province_Code', y='Minimum_Wage', data=df, ci=95, ax=sc.ax, palette='plasma')
        sc.ax.set_title('Minimum Wage Comparison across Canada')

        return sc
