import csv, copy

from .house import House
from .battery import Battery

class District():

    # TODO initialize
    def __init__(self, source_house, source_battery):
        self.houses = self.load_houses(source_house)
        self.batteries = self.load_batteries(source_battery)
        self.cost_shared = 0

    # open csv file
    def load_houses (self, source_house):
        """
        load all houses
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


    def total_cost(self, battery_cost, cable_cost):
        batteries = self.batteries
        cableslength = 0
        total_cost = 0
        for battery in batteries:
            houses = batteries.get(battery).houses
            for house in houses:
                cableslength = cableslength + (len(house.cables) - 1)

        print(f"Cables: {cableslength}")
        cableslength = cableslength - batteries.get(battery).double_cables_length
        total_cost += cableslength * cable_cost
        total_cost += battery_cost * len(batteries)
        print(f"Total: {total_cost}")
        
        self.cost_shared = total_cost
        return total_cost