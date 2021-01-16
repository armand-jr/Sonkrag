########################################################################
#
# greedy2.py from SONKRAG
# Armand Stiens, Willem Folkers, Dionne Ruigrok
# 
# Minor Programmeren UvA 2021
# 
# - ...
# - ...
########################################################################

from code.classes import district, house, battery
import random

class Greedy2:
    """
    The Greedy class that assigns the best possible value to each node one by one and takes the possibility of sharing the cables into account.
    """
    def __init__(self, district, cable_cost, battery_cost):
        """
        Initializes the Greedy2 object
        """
        self.district = district
        self.cable_cost = cable_cost
        self.battery_cost = battery_cost
    
    
    def house_loop(self):
        """
        Loops through all houses, checking for the closest battery and lays the cables
        """
        houses = self.district.houses
        batteries = self.district.batteries
        for house in houses:
            battery = self.closest_battery(houses.get(house), batteries)
            battery.add_house(houses.get(house))
            self.district.cable_to_battery(houses.get(house), battery)
        
        # for battery in batteries:
        #     print(f"amount: {batteries.get(battery).used_cap}")


    def change_battery_or_house(self, bat_or_house):
        """
        If the used capacity exceeds the max capacity, check if it is possible to move house to another battery or to swap houses from batteries
        """
        batteries = self.district.batteries
        for battery in batteries:
            if batteries.get(battery).used_cap > batteries.get(battery).max_cap:
                for newbattery in batteries:
                    if batteries.get(newbattery).used_cap < batteries.get(newbattery).max_cap and newbattery != battery:

                        if bat_or_house == 'change_battery':
                            self.district.check_space_battery(batteries.get(battery), batteries.get(newbattery))

                        else:
                            self.district.swap_house(batteries.get(battery), batteries.get(newbattery))


    #TODO wordt aan gewerkt om het te verkorten
    def improve_battery_distances(self):
        """
        Check if swapping houses makes a improvement in total length of cables.
        """
        batteries = self.district.batteries
        
        for battery in batteries:
            for newbattery in batteries:
                    if newbattery != battery:
                        while True:
                            improvement = 0
                            houseswap1 = None
                            houseswap2 = None

                            for houses in batteries.get(battery).houses:
                                for houses2 in batteries.get(newbattery).houses:
                                    old_distance = abs(batteries.get(battery).x_cor - houses.x_cor) + abs(batteries.get(battery).y_cor - houses.y_cor)
                                    old_distance2 = abs(batteries.get(newbattery).x_cor - houses2.x_cor) + abs(batteries.get(newbattery).y_cor - houses2.y_cor)
                                    new_distance = abs(batteries.get(newbattery).x_cor - houses.x_cor) + abs(batteries.get(newbattery).y_cor - houses.y_cor)
                                    new_distance2 = abs(batteries.get(battery).x_cor - houses2.x_cor) + abs(batteries.get(battery).y_cor - houses2.y_cor)

                                    if (new_distance - old_distance + new_distance2 - old_distance2) < improvement:
                                        if (batteries.get(newbattery).used_cap - houses2.output + houses.output < batteries.get(newbattery).max_cap
                                        and batteries.get(battery).used_cap - houses.output + houses2.output < batteries.get(battery).max_cap):
                                            improvement = new_distance - old_distance + new_distance2 - old_distance2
                                            houseswap1 = houses
                                            houseswap2 = houses2

                            if improvement == 0:
                                break
                            else:
                                batteries.get(battery).houses.remove(houseswap1)
                                for cable in houseswap1.cables:
                                    batteries.get(battery).remove_cable(cable)
                                houseswap1.cables = []
                                batteries.get(battery).used_cap = batteries.get(battery).used_cap - houseswap1.output
                                self.district.cable_to_battery(houseswap1, batteries.get(newbattery))
                                batteries.get(newbattery).add_house(houseswap1)

                                batteries.get(newbattery).houses.remove(houseswap2)
                                for cable in houseswap2.cables:
                                    batteries.get(battery).remove_cable(cable)
                                houseswap2.cables = []
                                batteries.get(newbattery).used_cap = batteries.get(newbattery).used_cap - houseswap2.output
                                self.district.cable_to_battery(houseswap2, batteries.get(battery))
                                batteries.get(battery).add_house(houseswap2)
           
        # for battery in batteries:
        #     print(f"amount3: {batteries.get(battery).used_cap}")

                                    
    def least_used_cap(self, batteries):
        """
        Loops through batteries and assigns house to least used battery
        """
        rest_value = 0
        battery_biggest_rest = None
        for battery in batteries:
            if batteries.get(battery).max_cap - batteries.get(battery).used_cap > rest_value:
                rest_value = batteries.get(battery).max_cap - batteries.get(battery).used_cap
                battery_biggest_rest = batteries.get(battery)
        return battery_biggest_rest


    def closest_battery(self, house, batteries):
        """
        Seeks for the battery with the closest distance to the house
        """
        shortest_distance = 0
        nearest_battery = None
        for battery in batteries:
            if batteries.get(battery).capacitycheck(house.output):
                distance = abs(batteries.get(battery).x_cor - house.x_cor) + abs(batteries.get(battery).y_cor - house.y_cor)

                if shortest_distance == 0:
                    shortest_distance = distance
                    nearest_battery = batteries.get(battery)
                else:
                    if distance < shortest_distance:
                        shortest_distance = distance
                        nearest_battery = batteries.get(battery)

        if nearest_battery == None:
            nearest_battery = self.least_used_cap(batteries)

        return nearest_battery


    def total_cost(self):
        """
        Calculates the total cost of the cables by calculating the shortest distance between the battery and the assigned houses
        """
        return self.district.total_cost(self.battery_cost, self.cable_cost)

        # batteries = self.district.batteries
        # total_cost = 0
        # for battery in batteries:
        #     houses = batteries.get(battery).houses
        #     for house in houses:
        #         distance = abs(batteries.get(battery).x_cor - house.x_cor) + abs(batteries.get(battery).y_cor - house.y_cor)
        #         total_cost += distance * self.cable_cost

        # total_cost += self.battery_cost * len(batteries)
        # self.district.cost_shared = total_cost


    def __repr__(self):
        return str(self.district.cost_shared)
        