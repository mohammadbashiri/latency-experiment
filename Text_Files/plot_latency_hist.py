import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_latency_hist(df, win_size=9, threshold=5, ax=None):
    """
    Makes a latency plot from a dataframe made from the arduino_serial_read.py experiment.

    Arguments:
        -win_size: the window size used for smoothing data.  Units are samples.
        -threshold: the channel threshold used for frame detection.

    Returns:
        Matplotlib axis.
    """

    data = df.copy()

    # Smooth Data and Detect Frames
    data[['Chan1_Smooth', 'Chan2_Smooth']] = data[['Chan1', 'Chan2']].rolling(win_size).max()  # Smoothing
    data[['Frame1On', 'Frame2On']] = data[['Chan1_Smooth', 'Chan2_Smooth']] > threshold  # Thresholding

    # Calculate Latency from LED Onset for each trial
    data['TrialTime'] = data.groupby('Trial').Time.apply(lambda x: x - x.min())  # Trial time detection
    resp_on = data[(data['Frame1On'] & (data['LED_State'] == 1)) | (data['Frame2On'] & (data['LED_State'] == 0))]
    latency = resp_on.groupby('Trial').TrialTime.min()

    # Plot the data
    if not ax:
        fig, ax = plt.subplots()
    (latency / 1000).hist(ax=ax).set(xlabel='latency time (ms)', ylabel='frequency')
    return ax


if __name__ == '__main__':

    # Import data
    data = pd.read_csv('../Measurements/s02_230218_white_randFreq_ObjectMode.csv')
    fig, ax = plt.subplots()
    plot_latency_hist(df=data, win_size=9, threshold=5, ax=ax)
    fig.savefig('s02_230218_white_randFreq_ObjectMode.png')
