from code.classes import district, house, battery
import random

class Random:
    """
    The Random class randomizes the optimal solution.
    """
    def __init__(self, district, cable_cost):
        self.district = district
        self.cable_cost = cable_cost
    
    def house_loop(self):
        """
        Loops through all houses, assigning to random battery and finding shortest cable to it
        """
        houses = self.district.houses
        batteries = self.district.batteries
        houses_list = []
        for house in houses: 
            houses_list.append(houses.get(house))

        for battery in batteries:
            print(f" battery nr {battery}")
            while True:
                if len(houses_list) == 0: 
                    break
                random_house = random.choice(houses_list)
                print(random_house) 
                if not batteries.get(battery).capacitycheck(random_house.output):
                    break 
                batteries.get(battery).add_house(random_house)
                # self.cable_to_battery(random_house, batteries.get(battery))
                houses_list.remove(random_house)
            
        # for house in houses:
        #     while True:
        #         battery = random.choice(list(batteries.values()))
        #         battery.add_house(houses.get(house))
        #         if battery.capacitycheck():
        #             break
        #     do battery =.......
        #     while !battery.capacitycheck()
            
    # def cap_check(self)

    def cable_to_battery(self, house, battery):
        """
        From the house lays down a cable one step at the time until the cable reaches the battery
        """
        if battery.x_cor < house.x_cor:
            x_direction = -1
        else:
            x_direction = 1
        
        x_cor = house.x_cor
        y_cor = house.y_cor
        while x_cor != battery.x_cor:
            house.add_cable(x_cor, y_cor)
            x_cor += x_direction
            
        if battery.y_cor < house.y_cor:
            y_direction = -1
        else:
            y_direction = 1
        while y_cor != battery.y_cor:
            house.add_cable(x_cor, y_cor)
            y_cor += y_direction

        house.add_cable(x_cor, y_cor)
    
    def total_cost(self):
        """
        Calculates the total cost of the cables by calculating the shortest distance between the battery and the assigned houses
        """
        batteries = self.district.batteries
        total_cost = 0
        for battery in batteries:
            houses = batteries.get(battery).houses
            for house in houses:
                distance = abs(batteries.get(battery).x_cor - house.x_cor) + abs(batteries.get(battery).y_cor - house.y_cor)
                total_cost += distance * self.cable_cost

        self.district.cost_shared = total_cost

    def __repr__(self):
        return str(self.district.cost_shared)