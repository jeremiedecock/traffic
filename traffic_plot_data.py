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

    ts_mean = ts.groupby(ts.index.start_time.time).mean()
    ts_median = ts.groupby(ts.index.start_time.time).median()
    ts_quartile_1 = ts.groupby(ts.index.start_time.time).quantile(0.25)
    ts_quartile_3 = ts.groupby(ts.index.start_time.time).quantile(0.75)
    ts_percentile_5 = ts.groupby(ts.index.start_time.time).quantile(0.05)
    ts_percentile_95 = ts.groupby(ts.index.start_time.time).quantile(0.95)
    ts_min = ts.groupby(ts.index.start_time.time).min()
    ts_max = ts.groupby(ts.index.start_time.time).max()

    ax = ts_mean.plot(y='duration', figsize=(18, 12), color="red", label="mean", alpha=0.75)
    ts_median.plot(ax=ax, color="blue", label="median", alpha=0.75)
    ts_quartile_1.plot(ax=ax, color="blue", alpha=0.5, style="--", label="1st quartile")
    ts_quartile_3.plot(ax=ax, color="blue", alpha=0.5, style="--", label="3rd quartile")
    ts_percentile_5.plot(ax=ax, color="blue", alpha=0.25, style=":", label="5th percentile")
    ts_percentile_95.plot(ax=ax, color="blue", alpha=0.25, style=":", label="95th percentile")
    ts_min.plot(ax=ax, color="black", alpha=0.2, style=":", label="min")
    ts_max.plot(ax=ax, color="black", alpha=0.2, style=":", label="max")

    plt.fill_between(ts_percentile_5.index, ts_percentile_5.values, ts_percentile_95.values, facecolor='blue', alpha=0.1)
    plt.fill_between(ts_quartile_1.index, ts_quartile_1.values, ts_quartile_3.values, facecolor='blue', alpha=0.1)

    ax.legend()

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

