# Armand Stiens, Willem Folkers, Dionne Ruigrok

import csv, copy

from .house import House
from .battery import Battery

class District():
    def __init__(self, source_house, source_battery):
        """
        Initializes the district object
        """
        self.houses = self.load_houses(source_house)
        self.batteries = self.load_batteries(source_battery)
        self.cost_shared = 0


    def load_houses (self, source_house):
        """
        load all houses by opening the right csv file
        """
        houses = {}
        house_id = 1

        #
        with open(source_house, 'r') as houses_file:
            csv_reader = csv.reader(houses_file)
            next(csv_reader)

            #
            for row in csv_reader:
                houses[int(house_id)] = House(house_id, row[0], row[1], row[2])
                house_id += 1

        return houses


    def load_batteries(self, source_battery):
        """
        load all batteries
        """
        batteries = {}
        battery_id = 1
        with open(source_battery, 'r') as batteries_file:
            csv_reader = csv.reader(batteries_file)
            
            next(csv_reader)
            
            for row in csv_reader:
                
                batteries[battery_id] = Battery(battery_id, row[0], row[1], row[2])
                battery_id +=1
        
        return batteries

    
    def valid_solution(self):
        """
        Checks if solution is valid by looking at max capacity of batteries and length of cables. 
        Returns True if solution is valid, else False
        """
        houses = []
        for house in self.houses.values():
            houses.append(house)

        for battery in self.batteries.values():
            if battery.used_cap > battery.max_cap:
                return False
            
            for house in battery.houses:
                houses.remove(house)

                if len(house.cables) == 0:
                    return False
        
        if len(houses) > 0:
            return False

        return True


    def check_space_battery(self, old_battery, new_battery):
        """
        Checks if there is some power left in other battery. Takes old_battery and new_battery as object inputs
        """
        while True:
            difference = 0
            bestchange = None
            for houses in old_battery.houses:
                if new_battery.used_cap + houses.output < new_battery.max_cap and houses.output > difference:
                    difference = houses.output
                    bestchange = houses

            if difference == 0:
                break
            else:
                self.swap_battery(old_battery, new_battery, bestchange)


    def swap_battery(self, old_battery, new_battery, house):
        """
        Swaps the battery location of a house. Takes in the old and new battery and house as object inputs
        """
        # remove house from old battery and delete cables
        old_battery.houses.remove(house)
        for cable in house.cables:
            old_battery.remove_cable(cable)
        house.cables = []
        old_battery.used_cap = old_battery.used_cap - house.output

        # add house to new battery
        if self.closest_cable(new_battery, house) != True:
            self.cable_to_battery(house, new_battery)
        new_battery.add_house(house)


    def swap_house(self, old_battery, new_battery):
        """
        Swaps house between two batteries. Takes in the old and new battery object inputs
        """
        while True:
            difference = 0
            houseswap1 = None
            houseswap2 = None
            for houses in old_battery.houses:
                for houses2 in new_battery.houses:
                    if (new_battery.used_cap - houses2.output + houses.output < new_battery.max_cap
                    and	houses.output - houses2.output > difference):
                        difference = houses.output - houses2.output
                        houseswap1 = houses
                        houseswap2 = houses2
                        
            if difference == 0:
                break
            else:
                self.swap_battery(old_battery, new_battery, houseswap1)
                self.swap_battery(new_battery, old_battery, houseswap2)


    def house_swap_with_improvement(self, old_battery, new_battery):
        while True:
            improvement = 0
            houseswap1 = None
            houseswap2 = None

            for houses in old_battery:
                for houses2 in new_battery.houses:
                    old_distance = abs(old_battery.x_cor - houses.x_cor) + abs(old_battery.y_cor - houses.y_cor)
                    old_distance2 = abs(new_battery.x_cor - houses2.x_cor) + abs(new_battery.y_cor - houses2.y_cor)
                    new_distance = abs(new_battery.x_cor - houses.x_cor) + abs(new_battery.y_cor - houses.y_cor)
                    new_distance2 = abs(old_battery.x_cor - houses2.x_cor) + abs(old_battery.y_cor - houses2.y_cor)

                    if (new_distance - old_distance + new_distance2 - old_distance2) < improvement:
                        if (new_battery.used_cap - houses2.output + houses.output < new_battery.max_cap
                        and old_battery.used_cap - houses.output + houses2.output < old_battery.max_cap):
                            improvement = new_distance - old_distance + new_distance2 - old_distance2
                            houseswap1 = houses
                            houseswap2 = houses2

            if improvement == 0:
                break
            else:
                self.swap_battery(old_battery, new_battery, houseswap1)
                self.swap_battery(new_battery, old_battery, houseswap2)

    
    def cable_to_battery(self, house, battery):
        """
        From the house lays down a cable one step at the time until the cable reaches the battery. Makes the route from house to battery
        """
        if battery.x_cor < house.x_cor:
            x_direction = -1
        else:
            x_direction = 1
        
        x_cor = house.x_cor
        y_cor = house.y_cor
        while x_cor != battery.x_cor:
            house.add_cable(x_cor, y_cor)
            battery.add_cable(f"{x_cor},{y_cor}")
            x_cor += x_direction
            
        if battery.y_cor < house.y_cor:
            y_direction = -1
        else:
            y_direction = 1
        while y_cor != battery.y_cor:
            house.add_cable(x_cor, y_cor)
            battery.add_cable(f"{x_cor},{y_cor}")
            y_cor += y_direction

        house.add_cable(x_cor, y_cor)
        battery.add_cable(f"{x_cor},{y_cor}")
            


    def cable_to_cable(self, house, cable_x_cor, cable_y_cor, battery):
        """ 
        From the house lays down a cable one step at the time until the cable reaches the cable 
        """
        if cable_x_cor < house.x_cor:
            x_direction = -1
        else:
            x_direction = 1
            
        x_cor = house.x_cor
        y_cor = house.y_cor
        while x_cor != cable_x_cor:
            house.add_cable(x_cor, y_cor)
            battery.add_cable(f"{x_cor},{y_cor}")
            x_cor += x_direction
            
        if cable_y_cor < house.y_cor:
            y_direction = -1
        else:
            y_direction = 1
        while y_cor != cable_y_cor:
            house.add_cable(x_cor, y_cor)
            battery.add_cable(f"{x_cor},{y_cor}")
            y_cor += y_direction

        house.add_cable(x_cor, y_cor)
        battery.add_cable(f"{x_cor},{y_cor}")
            
    

    def double_cable_route(self, battery, cable_x, cable_y, new_house):
        cable_list = []
        index = 0
        for house in battery.houses:
            if f"{cable_x},{cable_y}" in house.cables:
                cable_list = copy.copy(house.cables)
                break

        while f"{cable_x},{cable_y}" != cable_list[index]:
            index +=1

        for index2 in range(index + 1,len(cable_list)): #Plus 1 om er voor te zorgen dat het eerste punt niet dubbel in de kabellijst staat
            new_house.cables.append(cable_list[index2])
            battery.add_cable(cable_list[index2])


    def closest_cable(self, battery, new_house):
        """
        Search for closest cable and attach house to that cable
        """
        battery_distance = abs(battery.x_cor - new_house.x_cor) + abs(battery.y_cor - new_house.y_cor)
        best_distance= battery_distance 
        best_x_cor = 0
        best_y_cor = 0
        for cable in battery.cables:
            temp_cable = cable.split(',')
            temp_cable = [int(temp_cable2) for temp_cable2 in temp_cable]
            
           
            distance = abs(temp_cable[0] - new_house.x_cor) + abs(temp_cable[1] - new_house.y_cor)
            if distance < best_distance:
                best_distance = distance
                best_x_cor = temp_cable[0]
                best_y_cor = temp_cable[1]

        if best_distance < battery_distance:
            # cable from house to cable
            self.cable_to_cable(new_house, best_x_cor, best_y_cor, battery)

            # cable from cable to battery
            self.double_cable_route(battery, best_x_cor, best_y_cor, new_house)


            return True
        else:
            return False




    def total_cost(self, battery_cost, cable_cost):
        batteries = self.batteries
        cableslength = 0
        total_cost = 0
        cables = []
        for battery in batteries:
            houses = batteries.get(battery).houses
            for house in houses:
                cables.extend(house.cables)
                #cableslength = cableslength + len(house.cables)
            
            #cableslength = cableslength - batteries.get(battery).double_cables_length)

        cables = list(set(cables))
        cableslength = len(cables)
        total_cost += cableslength * cable_cost
        total_cost += battery_cost * len(batteries)

        self.cost_shared = total_cost
        return total_cost