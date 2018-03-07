from glob import glob
from os import path

def task_plot_latency_hist():
    for csv_fname in glob('.\\Measurements\\*.csv'):
        fig_fname = '.\\Figures\\' + path.splitext(path.basename(csv_fname))[0] + '.png'
        yield {
            'name': csv_fname,
            'actions': ['python .\\Text_Files\\plot_latency_hist.py {0} {1}' .format(csv_fname, fig_fname)],
            'file_dep': [csv_fname],
            'targets': [fig_fname],
        }
