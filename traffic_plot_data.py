#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import argparse
import matplotlib.pyplot as plt

from matplotlib.dates import DateFormatter

def plot_traffic(file_path_list):
    print(file_path_list)

    df = pd.concat((pd.read_csv(file_path) for file_path in file_path_list), ignore_index=True)
    print(df)

    df.plot(x='datetime', y='duration')
    plt.show()

    #fig.autofmt_xdate()
    #formatter = DateFormatter('%H:%M')
    #ax.xaxis.set_major_formatter(formatter)
    #ax.plot(times, durations, 'ro')
    #ax.set_xlabel('Time (mn)')
    #ax.set_ylabel('Trip duration in current traffic')
    ## TODO: save figure in a png file ?

def main():
    parser = argparse.ArgumentParser(description='An argparse snippet.')

    parser.add_argument("fileargs", nargs="*", metavar="FILE",
            help="CSV files to plot.")

    args = parser.parse_args()

    plot_traffic(args.fileargs)

if __name__ == '__main__':
    main()

