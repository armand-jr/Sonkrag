# Armand Stiens, Willem Folkers, Dionne Ruigrok

import matplotlib.pyplot as plt
import numpy as np
import csv
 
def visualise(district):
    """
    TODO
    """
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    # major_ticks = np.arange(0, 51, 10)
    # minor_ticks = np.arange(0, 51, 1)

    # ax.set_xticks(major_ticks)
    # ax.set_xticks(minor_ticks, minor=True)
    # ax.set_yticks(major_ticks)
    # ax.set_yticks(minor_ticks, minor=True)

    house_x_cor = []
    house_y_cor = []
    battery_x_cor = []
    battery_y_cor = []
    cables = []

    houses = district.houses
    batteries = district.batteries

    # 
    for house in houses:
        cables.append(houses.get(house).cables)
        house_x_cor.append(houses.get(house).x_cor)
        house_y_cor.append(houses.get(house).y_cor)

    # 
    for cablelist in cables:
        for index in range(len(cablelist)-1):

            point1 = cablelist[index]
            point1  = point1.split(',')
            point2 = cablelist[index + 1]
            point2 = point2.split(',')
            xvalues = [int(point1[0]), int(point2[0])]
            yvalues = [int(point1[1]), int(point2[1])]
            plt.plot(xvalues, yvalues, 'C1')


    for battery in batteries:
        battery_x_cor.append(batteries.get(battery).x_cor)
        battery_y_cor.append(batteries.get(battery).y_cor)

    # 
    x = list(range(0, 51))
    y = list(range(0, 51))
    plt.yticks(y, fontsize=6)
    plt.xticks(x, fontsize=6)

    plt.axis([-3, 53, -3, 53])
    plt.scatter(battery_x_cor, battery_y_cor, marker='s', c='green', s=100, edgecolors='black')
    plt.scatter(house_x_cor, house_y_cor, c='red')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# data = [24, 24, 24, 16, 16, 2, 2, 2]
# x = list(range(0, 50))
# y = list(range(0, 50))


# plt.yticks(y)
# plt.xticks(x)
