import numpy as np
import pandas as pd
from Canvas import MultipleSubplotsCanvas, SeabornCanvas, AllClassesCanvas, GeneratedSamplesCanvas
import seaborn as sns


class Dataset:
    def __init__(self):
        self.sc = self.plot_imbalanced_classes()
        self.classes_plot = self.plot_class_examples()
        self.generated_plot = self.plot_generated_samples()
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

    def plot_class_examples(self):
        examples = np.load('SerializedObjects/class_samples/examples.npy')
        class_names = np.load('SerializedObjects/full_class_names.npy')
        colors = sns.color_palette("plasma", n_colors=15)
        num_rows = 3
        num_columns = 5
        sc = AllClassesCanvas(self, 7, 5)
        for i in range(num_rows * num_columns):
            ax = sc.figure.add_subplot(num_rows, num_columns, i + 1)
            ax.grid(False)
            ax.plot(examples[i], color=colors[i])
            ax.set_xlabel(class_names[i], color='white', fontsize=9)
            ax.xaxis.set_label_coords(0.5, -0.025)

            ax.set_xticks([])
            ax.set_yticks([])

        sc.figure.subplots_adjust(left=0.03, right=0.97)

        return sc

    def plot_generated_samples(self):
        X_example = np.load('SerializedObjects/generated_samples/generated_samples_example.npy')
        sc = GeneratedSamplesCanvas(self, 7, 5, dpi=120)
        for i, ax in enumerate(sc.figure.axes):
            x_label = 'Real'
            color = 'darkorange'
            if i in range(4, 6):
                color = 'red'
                x_label = 'Generated'
            ax.set(facecolor='black')
            ax.plot(X_example[i + 6], linewidth=0.8, color=color)
            ax.xaxis.set_label_coords(0.5, -0.025)
            ax.set_xlabel(x_label, color=color, fontsize=10)

        sc.figure.suptitle('Premature Ventricular Contraction Samples', fontsize=12, color='white')

        return sc

