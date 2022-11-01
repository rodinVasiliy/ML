import os.path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def convert_data(source, column_name):
    source[column_name] = source[column_name].str.replace(',', '')
    source[column_name] = pd.to_numeric(source[column_name])


def get_anomalies(source, column_name, threshold):
    arr = source.loc[:, column_name].rolling(window=9).median()
    size = len(arr)
    indexes = []
    vals = []
    for i in range(1, size):
        if (arr[i] / arr[i - 1]) > threshold or arr[i - 1] / arr[i] > threshold:
            indexes.append(i)
            vals.append(arr[i])

    tmp = source.loc[:, column_name].rolling(window=9).median().plot(figsize=[20, 5])
    plt.plot(indexes, [arr[i] for i in indexes], ls="", marker="o", label="points")
    print(indexes)

    plt.show()


if __name__ == '__main__':
    path = os.path.join('resources', 'bitcoin.csv')
    source_df = pd.read_csv(path, sep=',')
    get_anomalies(source_df, 'Open')
    get_anomalies(source_df, 'High')
    get_anomalies(source_df, 'Low')
    get_anomalies(source_df, 'Close')

    convert_data(source_df, 'Volume')
    # convert_data(source_df, 'Market Cap')
    source_df.loc[source_df['Market Cap'] == '-', :] = np.nan
    convert_data(source_df, 'Market Cap')
    source_df['Market Cap'].interpolate(limit=10, limit_direction='forward', method='pad')
    get_anomalies(source_df, 'Volume')
    get_anomalies(source_df, 'Market Cap')
