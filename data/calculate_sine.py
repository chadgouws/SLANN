import numpy as np
import csv
import datetime
import time


def calculate_series(t):
    x = np.array(range(t))
    s = 0.029 * np.sin(x) + 1.1
    c = 0.031 * np.cos(x) + 1.1
    return s, c


def series_to_file(z):
    out = []
    for i in range(len(z)):
        out.append([z[i], z[i+1], z[i+2]])
        if i+3 == len(z):
            break
        else:
            pass

    with open('out-' + datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S') + '.csv', "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(out)


if __name__ == '__main__':

    a, b = calculate_series(100)
    series_to_file(a)
    time.sleep(2)
    series_to_file(b)
