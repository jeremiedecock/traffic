#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import matplotlib.pyplot as plt
import os
import pandas as pd

from matplotlib.dates import DateFormatter

def plot_traffic(file_path_list):
    print(file_path_list)

    ts = pd.concat((pd.read_csv(file_path, index_col=0, parse_dates=[0], squeeze=True) for file_path in file_path_list))

    ts = ts.resample('1min', kind='period').mean()

    ax = ts.groupby(ts.index.start_time.time).mean().plot(y='duration', figsize=(18, 12), color="red")
    ts.groupby(ts.index.start_time.time).median().plot(ax=ax, color="green")
    ts.groupby(ts.index.start_time.time).quantile(0.25).plot(ax=ax, color="blue", alpha=0.75, style="--")
    ts.groupby(ts.index.start_time.time).quantile(0.75).plot(ax=ax, color="blue", alpha=0.75, style="--")
    ts.groupby(ts.index.start_time.time).quantile(0.95).plot(ax=ax, color="blue", alpha=0.5, style=":")
    ts.groupby(ts.index.start_time.time).quantile(0.05).plot(ax=ax, color="blue", alpha=0.5, style=":")

    #fig.autofmt_xdate()
    #formatter = DateFormatter('%H:%M')
    #ax.xaxis.set_major_formatter(formatter)
    #ax.plot(times, durations, 'ro')

    ax.set_xlabel('Time')
    ax.set_ylabel('Estimated trip duration (mn)')

    plt.show()

    ## TODO: save figure in a png file ?

def main():
    parser = argparse.ArgumentParser(description='An argparse snippet.')

    parser.add_argument("fileargs", nargs="*", metavar="FILE", help="CSV files to plot.")

    args = parser.parse_args()

    plot_traffic(args.fileargs)

if __name__ == '__main__':
    main()

