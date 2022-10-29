import os.path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



if __name__ == '__main__':
    path = os.path.join('resources', 'bitcoin.csv')
    source_df = pd.read_csv(path, sep=',')
    arr_1 = source_df.loc[:, 'Open'].rolling(window=9).median()
    arr_2 = source_df.loc[:, 'Open'].rolling(window=9).mean()
    dif = arr_2 - arr_1
    size = len(dif)
    indexes = []
    vals = []
    for i in range(0, size):
        if dif[i] > 200 or dif[i] < -200:
            indexes.append(i)
            vals.append(arr_1[i])

    tmp = source_df.loc[:, 'Open'].rolling(window=9).median().plot(figsize = [20,5])
    plt.plot(indexes, [arr_1[i] for i in indexes], ls="", marker="o", label="points")
    print(indexes)

    plt.show()