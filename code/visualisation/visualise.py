import matplotlib.pyplot as plt
import numpy as np
import csv
 
def visualise(district):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    major_ticks = np.arange(0, 51, 10)
    minor_ticks = np.arange(0, 51, 1)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

    # batteries location
    bat_x = [38, 43, 42, 49, 3]
    bat_y = [12, 13, 3, 23, 45]

    house_x_cor = []
    house_y_cor = []

    house_x_cor.append(row[0])
    house_y_cor.append(row[1])

    x = list(range(0, 51))
    y = list(range(0, 51))
    plt.yticks(y)
    plt.xticks(x)

    plt.axis([0, 50, 0, 50])
    plt.scatter(bat_x, bat_y, marker='s', c='green')
    plt.scatter(house_x_cor, house_y_cor, c='red')
    plt.grid(True)
    plt.tight_layout()
    plt.show()






# data = [24, 24, 24, 16, 16, 2, 2, 2]
# x = list(range(0, 50))
# y = list(range(0, 50))


# plt.yticks(y)
# plt.xticks(x)



    