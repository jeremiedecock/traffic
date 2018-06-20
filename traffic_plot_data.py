import matplotlib.pyplot as plt

from matplotlib.dates import DateFormatter

# TODO: parse data files to fill the next two variables...
# TODO: parse and plot data with Pandas...
times = []
durations = []

fig, ax = plt.subplots(1, 1, figsize=(15, 7.5))

fig.autofmt_xdate()
formatter = DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(formatter)

ax.plot(times, durations, 'ro')

ax.set_xlabel('Time (mn)')
ax.set_ylabel('Trip duration in current traffic')

plt.show()
# TODO: save figure in a png file ?
