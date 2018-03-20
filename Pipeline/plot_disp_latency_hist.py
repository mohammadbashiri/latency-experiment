import pandas as pd
import numpy as np
import seaborn as sns
import click
import matplotlib.pyplot as plt


def plot_disp_latency_hist(df, ax=None, return_data=False):
    """
    Makes a latency plot from a dataframe made from the display_latency.py experiment.

    Arguments:
        - retrun_data: if you want the function return the data set this to True (default is False)

    Returns:
        - Matplotlib axis
    """

    data = df.copy()

    # Seperate the time points for each interval
    data['TrialTime'] = data.groupby('Trial').Time.apply(lambda x: x - x.min())

    # Onset Detection
    resp_on = data[(data['Chan1'] != 0) & (data['Trial'] != 0)]  # ignore trial 0

    # get the latency values
    latency = resp_on.groupby('Trial').TrialTime.min()
    
    # retrun the data
    if return_data:
        return latency / 1000
    
    # plot the histogram of latency values
    else:
        if not ax:
            fig, ax = plt.subplots()
        sns.distplot(latency / 1000).set(xlabel='latency time (ms)', ylabel='frequency', xlim=[0, 60])
        return ax
    
    
@click.command()
@click.argument('csv_fname', type=click.File('r'))
@click.argument('fig_fname', type=click.File('wb'))
def run_disp_latency_analysis(csv_fname, fig_fname):
    """
    Takes a csv file generated from the  arduino_serial_read_rw.py experiment and outputs a figure image showing the trial latency.
    """
    
    data = pd.read_csv(csv_fname)
    fig, ax = plt.subplots()
    plot_disp_latency_hist(df=data, ax=ax)
    fig.savefig(fig_fname)
    
    
if __name__ == '__main__':
    run_disp_latency_analysis()