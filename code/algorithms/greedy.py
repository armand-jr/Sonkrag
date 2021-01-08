from code.classes import district, house, battery

class Greedy:
    """
    The Greedy class that assigns the best possible value to each node one by one.
    """
    def __init__(self, district, cable_cost):
        self.district = district
        self.cable_cost = cable_cost
    
    def house_loop(self):
        """
        Loops through all houses, checking for the closest battery and lays the cables
        """
        houses = self.district.houses
        batteries = self.district.batteries
        for house in houses:
            battery = self.closest_battery(houses.get(house), batteries)
            battery.add_house(houses.get(house))
            self.cable_to_battery(houses.get(house), battery)

    def closest_battery(self, house, batteries):
        """
        Seeks for the battery with the closest distance to the house
        """
        shortest_distance = 0
        nearest_battery = None
        for battery in batteries:
            distance = abs(batteries.get(battery).x_cor - house.x_cor) + abs(batteries.get(battery).y_cor - house.y_cor)
            if shortest_distance == 0:
                shortest_distance = distance
                nearest_battery = batteries.get(battery)
            else:
                if distance < shortest_distance:
                    shortest_distance = distance
                    nearest_battery = batteries.get(battery)
        
        return nearest_battery

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
        while x_cor != battery.x_cor:
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