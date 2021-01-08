import csv

from .house import House
from .battery import Battery

class District ():

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

            #print("HOUSES \n")
            #print(houses)
            #print("\n\n\n")

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
            #print("BATTERIES \n")
            #print(batteries)    
        
        return batteries
