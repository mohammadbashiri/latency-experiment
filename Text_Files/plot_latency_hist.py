import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import click
import seaborn as sns


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
    sns.distplot(latency / 1000, ax=ax).set(xlabel='latency time (ms)', ylabel='frequency')
    return ax


@click.command()
@click.argument('csv_fname', type=click.File('r'))
@click.argument('fig_fname', type=click.File('wb'))
def run_latency_analysis(csv_fname, fig_fname):
    """
    Takes a csv file generated from the  arduino_serial_read.py experiment and outputs a figure image showing the trial latency.
    """
    data = pd.read_csv(csv_fname)
    fig, ax = plt.subplots()
    plot_latency_hist(df=data, win_size=9, threshold=5, ax=ax)
    fig.savefig(fig_fname)


if __name__ == '__main__':
    run_latency_analysis()
