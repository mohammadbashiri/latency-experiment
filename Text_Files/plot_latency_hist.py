import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# get the file name
path = input("Enter the file name:")

# Import data
data = pd.read_csv(path)

# Smoothing
win_size = 9
data[['Chan1_Smooth', 'Chan2_Smooth']] = data[['Chan1', 'Chan2']].rolling(win_size).max()

# Thresholding
threshold = 5
data[['Frame1On', 'Frame2On']] = data[['Chan1_Smooth', 'Chan2_Smooth']] > threshold

# Trial time detection
data['TrialTime'] = data.groupby('Trial').Time.apply(lambda x: x - x.min())

# Onset Detection for Each Trial
resp_on = data[(data['Frame1On'] & (data['LED_State'] == 1)) | (data['Frame2On'] & (data['LED_State'] == 0))]
latency = resp_on.groupby('Trial').TrialTime.min()

fig, ax = plt.subplots()
(latency / 1000).hist(ax=ax).set(xlabel='latency time (ms)', ylabel='frequency')
fig.savefig('s02_230218_white_randFreq_ObjectMode.png')
