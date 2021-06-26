from scipy.signal import butter, filtfilt
from tensorflow.keras import backend as K


def assign_labels_for_categories(label):
    """
    This function takes the signal of the category and encodes it into an integer value.

    :param label: symbol of the class
    :return:
    """
    categories_and_classes = {'N': ['N', 'L', 'R', 'e', 'j'], 'S': ['A', 'a', 'x', 'J'], 'V': ['V', 'E', '!'],
                              'F': ['F'], 'Q': ['f', 'Q']}
    keys = list(categories_and_classes.keys())
    for category, classes in categories_and_classes.items():
        if label in classes:
            return keys.index(category)


def assign_labels_for_all_classes(label):
    """
    This function takes the signal of the class and encodes it into an integer value.
    :param label: symbol of the class
    :return:
    """
    categories_and_classes = {'N': ['N', 'L', 'R', 'e', 'j'], 'S': ['A', 'a', 'x', 'J'], 'V': ['V', 'E', '!'],
                              'F': ['F'], 'Q': ['f', 'Q']}
    available_classes = [category for categories in categories_and_classes.values() for category in categories]
    if label in available_classes:
        return available_classes.index(label)


def segments(i, signal, ann_sample, ann_symbol):
    """
    This function returns the start and the end of every heartbeat so it can
    be beautiful displayed on the UI.

    :param i: the index indicating the number of the heartbeat
    :param signal: the array containing the signal
    :param ann_sample: the array containing the beats locations
    :param ann_symbol: the array containing the beats symbols
    :return: start location and the end location of the heartbeat
    """
    if i == 0:
        next_beat = ann_sample[i + 1]
        ecg_window = (next_beat - ann_sample[i]) // 2
        start = 0
        end = ann_sample[i] + ecg_window

    elif i == ann_sample.size - 1:
        previous_beat = ann_sample[i - 1]
        ecg_window = (ann_sample[i] - previous_beat) // 2
        start = ann_sample[i] - ecg_window
        end = signal.shape[0]

    else:
        previous_label = assign_labels_for_categories(ann_symbol[i - 1])
        ecg_window_before = (ann_sample[i] - ann_sample[i - 1]) // 2
        ecg_window_after = (ann_sample[i + 1] - ann_sample[i]) // 2
        end = ann_sample[i] + ecg_window_after
        if previous_label is None:
            start = 0
        else:
            start = ann_sample[i] - ecg_window_before

    return start, end


def segments_signals_txt(i, signal, ann_sample):
    if i == 0:
        next_beat = ann_sample[i + 1]
        ecg_window = (next_beat - ann_sample[i]) // 2
        start = 0
        end = ann_sample[i] + ecg_window

    elif i == ann_sample.size - 1:
        previous_beat = ann_sample[i - 1]
        ecg_window = (ann_sample[i] - previous_beat) // 2
        start = ann_sample[i] - ecg_window
        end = signal.shape[0]

    else:
        ecg_window_before = (ann_sample[i] - ann_sample[i - 1]) // 2
        ecg_window_after = (ann_sample[i + 1] - ann_sample[i]) // 2
        end = ann_sample[i] + ecg_window_after

        start = ann_sample[i] - ecg_window_before

    return start, end


def define_sequence(signal, beat_location):
    """
    This function defines the sequences of the heartbeats, segmented
    with a fixed size. This heartbeats are used for prediction.

    :param signal: the array of the signal
    :param beat_location: the beat location value
    :return:
    """
    ecg_segment_before = 179
    ecg_segment_after = 180
    sequence_start = beat_location - ecg_segment_before
    sequence_end = beat_location + ecg_segment_after + 1

    if sequence_start < 0:
        sequence_start = 0
        sequence = signal[sequence_start: sequence_end]
    elif sequence_end > signal.shape[0]:
        sequence_end = signal.shape[0]
        sequence = signal[sequence_start:sequence_end]
    else:
        sequence = signal[sequence_start:sequence_end]

    return sequence


def butterworth_filter(signal, low_fs, high_fs, fs, order=2):
    """
    This function takes the signal and performs the denoising step with
    applying a Butterworth filter over the signal.

    :param signal: the array with the signal
    :param low_fs: low frequency
    :param high_fs: high frequency
    :param fs: frequency
    :param order:
    :return:
    """
    nyq = 0.5 * fs
    low = low_fs / nyq
    high = high_fs / nyq
    b, a = butter(order, [low, high], btype='band')
    y = filtfilt(b, a, signal)
    return y


def denoise(dataset):
    """
    Applies the denosing step to the entire dataset.

    :param dataset: the array of arrays containg the signals.
    :return: the processed dataset
    """
    processed_dataset = []
    for signal in dataset:
        signal = butterworth_filter(signal, 0.5, 40, 360)
        processed_dataset.append(signal)
    return processed_dataset


def recall_m(y_true, y_pred):
    """
    This function computes the recall metric for training/ predicting.

    :param y_true: The true labels
    :param y_pred: The predicted labels
    :return:
    """
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall


def precision_m(y_true, y_pred):
    """
      This function computes the precision metric for training/ predicting.

      :param y_true: The true labels
      :param y_pred: The predicted labels
      :return:
      """
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision


def f1_score_m(y_true, y_pred):
    """
      This function computes the f1-score metric for training/ predicting.

      :param y_true: The true labels
      :param y_pred: The predicted labels
      :return:
      """
    precision = precision_m(y_true, y_pred)
    recall = recall_m(y_true, y_pred)
    return 2 * ((precision * recall) / (precision + recall + K.epsilon()))
