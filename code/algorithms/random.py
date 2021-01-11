from code.classes import district, house, battery
import random, copy

class Random:
    """
    The Random class randomizes the optimal solution.
    """
    def __init__(self, district, cable_cost):
        self.district = district
        self.cable_cost = cable_cost
    
        


    def house_loop(self):
        houses = self.district.houses
        batteries = self.district.batteries
        amount = 0
        for house in houses:
            amount += 1
            battery = random.choice(list(batteries.values()))
            battery.add_house(houses.get(house))
            self.cable_to_battery(houses.get(house), battery)
        print(f"amount: {amount}")

        for i in batteries:
            print(batteries.get(i).used_cap)

        # print(f"{houses}")
            

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