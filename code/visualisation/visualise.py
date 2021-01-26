# Armand Stiens, Willem Folkers, Dionne Ruigrok

import matplotlib.pyplot as plt
import numpy as np
import csv
 
def visualise(district, algorithm, district_id, total_cost, filename, advanced5):
    """
    Creates an images of the result
    """
    plt.clf()
    house_x_cor = []
    house_y_cor = []
    battery_x_cor = 0
    battery_y_cor = 0

    batteries = district.batteries
    x = list(range(0, 51))
    y = list(range(0, 51))
    plt.yticks(y, fontsize=6)
    plt.xticks(x, fontsize=6)
    plt.axis([-3, 53, -3, 53])
    plt.suptitle(f"algorithm: {algorithm}, district {district_id}, total costs: {total_cost}, {advanced5}")
    plt.grid(True)
    plt.tight_layout()
    colors = ['orange', 'forestgreen', 'm', 'dodgerblue', 'red']
    index = 0

    # loops trough all batteries and print them out
    for battery in batteries:
        battery_x_cor = batteries.get(battery).x_cor
        battery_y_cor = batteries.get(battery).y_cor
        cables = []
        house_x_cor = []
        house_y_cor = []

        # adds all houses and cables from one battery to a list
        for house in batteries.get(battery).houses:
            house_x_cor.append(house.x_cor)
            house_y_cor.append(house.y_cor)
            cables.append(house.cables)
            
        plt.scatter(battery_x_cor, battery_y_cor, marker='s', c=colors[index], s=100, edgecolor='black', zorder=3)
        plt.scatter(house_x_cor, house_y_cor, c=colors[index], zorder=3)

        # loop through all cables and prints them out
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
    
    plt.savefig(filename)
    plt.show()
