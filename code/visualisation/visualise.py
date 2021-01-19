# Armand Stiens, Willem Folkers, Dionne Ruigrok

import matplotlib.pyplot as plt
import numpy as np
import csv
 
def visualise(district, algorithm, district_id, totalcost, filename):
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
    battery_x_cor = 0
    battery_y_cor = 0

    batteries = district.batteries
    
    # axes = plt.axis([[-3, 53, -3, 53]])

    x = list(range(0, 51))
    y = list(range(0, 51))
    # plt.set_title('filename')
    plt.yticks(y, fontsize=6)
    plt.xticks(x, fontsize=6)
    plt.axis([-3, 53, -3, 53])
    # plt.set_axisbelow(True)
    plt.suptitle(f"algorithm: {algorithm}, district {district_id}, total cost: {totalcost}")
    plt.grid(True)
    plt.tight_layout()


    colors = ['blue', 'green', 'darkviolet', 'dodgerblue', 'orange']
    index = 0

    for battery in batteries:
        battery_x_cor = batteries.get(battery).x_cor
        battery_y_cor = batteries.get(battery).y_cor
        cables = []

        for house in batteries.get(battery).houses:
            house_x_cor.append(house.x_cor)
            house_y_cor.append(house.y_cor)
            cables.append(house.cables)

        plt.scatter(battery_x_cor, battery_y_cor, marker='s', c=colors[index], s=100, edgecolor='black')

        for cablelist in cables:
            for cable in range(len(cablelist)-1):
                point1 = cablelist[cable]
                point1  = point1.split(',')
                point2 = cablelist[cable + 1]
                point2 = point2.split(',')
                xvalues = [int(point1[0]), int(point2[0])]
                yvalues = [int(point1[1]), int(point2[1])]
                plt.plot(xvalues, yvalues, colors[index])
        index += 1

    
    plt.scatter(house_x_cor, house_y_cor, c='red')
    plt.savefig(filename)
    plt.show()




# plt.yticks(y)
# plt.xticks(x)
