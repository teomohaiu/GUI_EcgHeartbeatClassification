import wfdb
import tensorflow as tf
import numpy as np
import statistics
from sklearn.preprocessing import StandardScaler
from Utils import (define_sequence,
                   assign_labels_for_categories,
                   assign_labels_for_all_classes,
                   denoise, f1_score_m,
                   segments, segments_signals_txt)
from scipy.signal import find_peaks


class Model:
    def __init__(self):
        self.X_test = list()
        self.y_class = list()
        self.y_category = list()
        self.signal = list()
        self.annotation_sample = list()
        self.annotation_symbols = list()
        self.beat_location = list()
        self.class_names = ['Normal beat', 'Left Bundle\nBranch Block', 'Right Bundle\nBranch Block', 'Atrial Escape',
                            'Nodal (junctional)\nEscape', 'Atrial premature\ncontraction',
                            'Abberated atrial\npremature',
                            'Blocked atrial\npremature', 'Nodal (junctional)\npremature',
                            'Premature\nventricular\ncontraction', 'Ventricular Escape', 'Ventricular flutter \nwave',
                            'Fusion of ventricular\nand normal', 'Fusion of\npaced and\nnormal', 'Unknown beats']
        self.sequence_start = list()
        self.sequence_end = list()
        # self.read_signal()
        # self.preprocess()

    def read_signal(self, record_file, annotation_file):
        if type(self.X_test) is np.ndarray:
            self.X_test = list()
            self.y_class = list()
            self.y_category = list()
            self.sequence_start = list()
            self.sequence_end = list()
            self.beat_location = list()

        record = wfdb.rdrecord(record_file, sampto=2200)
        annotation = wfdb.rdann(annotation_file, 'atr', sampto=2200)
        ecg_signal = record.p_signal
        self.signal = ecg_signal[:, 0]
        self.annotation_sample = annotation.sample
        self.annotation_symbols = annotation.symbol

        for i in range(self.annotation_sample.size):
            label_class = assign_labels_for_all_classes(self.annotation_symbols[i])
            label_category = assign_labels_for_categories(self.annotation_symbols[i])
            ecg_segment = define_sequence(self.signal, self.annotation_sample[i])
            start, end = segments(i, self.signal, self.annotation_sample, self.annotation_symbols)

            if ecg_segment.size > 0 and label_category is not None:
                self.y_class.append(label_class)
                self.y_category.append(label_category)
                self.X_test.append(ecg_segment)
                self.sequence_start.append(start)
                self.sequence_end.append(end - 6)
                self.beat_location.append(self.annotation_sample[i])

        print(len(self.annotation_sample))
        print(self.annotation_sample)
        print(self.annotation_symbols)
        for sample in self.X_test:
            print(sample.shape)
        for i in range(len(self.sequence_start)):
            print('start: {}, end:{}'.format(self.sequence_start[i], self.sequence_end[i]))
        print('Signal: ', self.signal)

    def read_signal_from_text_file(self, record_file, annotation_file):
        if type(self.X_test) is np.ndarray:
            self.X_test = list()
            self.y_class = list()
            self.y_category = list()
            self.sequence_start = list()
            self.sequence_end = list()
            self.beat_location = list()

        try:
            self.signal = np.loadtxt(record_file)
            if annotation_file is not None:
                self.annotation_sample = np.loadtxt(annotation_file, dtype=int)
            else:
                peaks = find_peaks(self.signal, height=0.4)
                self.annotation_sample = peaks[0]
        except Exception as e:
            print(e)

        for i in range(self.annotation_sample.size):
            ecg_segment = define_sequence(self.signal, self.annotation_sample[i])
            start, end = segments_signals_txt(i, self.signal, self.annotation_sample)

            if ecg_segment.size > 0:
                self.X_test.append(ecg_segment)
                self.sequence_start.append(start)
                self.sequence_end.append(end - 6)
                self.beat_location.append(self.annotation_sample[i])

    def preprocess(self):
        self.X_test = tf.keras.preprocessing.sequence.pad_sequences(
            self.X_test, maxlen=360, dtype='float32', padding='pre',
            truncating='pre', value=0.0
        )
        self.X_test = denoise(self.X_test)
        scaler = StandardScaler()
        self.X_test = scaler.fit_transform(self.X_test)

    def predict(self):
        model = tf.keras.models.load_model('model-end-to-end-fold-4', custom_objects={'f1_score_m': f1_score_m})
        predictions = model.predict(self.X_test)
        predicted_labels = np.argmax(predictions, axis=-1)
        print('Predicted labels:', predicted_labels)

        predicted_classes, probabilities = self.showPredictionsPercentages(predicted_labels, predictions)
        return predicted_classes, probabilities

    def showPredictionsPercentages(self, predicted_labels, predictions_array):
        accuracy_per_total = list()
        predicted_classes = list()
        probabilities = list()
        for i in range(len(predicted_labels)):
            accuracy_per_total.append(np.max(predictions_array[i]))
            print("{}:{:.2f}%".format(self.class_names[predicted_labels[i]], 100 * np.max(predictions_array[i])))
            predicted_classes.append(self.class_names[predicted_labels[i]])
            probabilities.append(np.round(100 * np.max(predictions_array[i]), 2))

        print('Accuracy per total:', statistics.mean(accuracy_per_total))
        return predicted_classes, probabilities
