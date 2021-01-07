import csv

from .house import House
from .battery import Battery

class District ():

    # TODO initialize
    def __init__(self, source_battery, source_house):
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
        with open("data/houses&batteries/district_1/district-1_houses.csv", 'r') as houses_file:
            csv_reader = csv.reader(houses_file)
            
            next(csv_reader)

            #
            for row in csv_reader:
                

                houses[house_id] = House(house_id, row[0], row[1], row[2])
                house_id += 1

        return houses


    def load_batteries(self, source_battery):
        """
        load all batteries
        """
        batteries = []
        battery_id = 1

        #
        with open("data/houses&batteries/district_1/district-1_batteries.csv", 'r') as batteries_file:
            csv_reader = csv.reader(batteries_file)
            
            next(csv_reader)
            
            for row in csv_reader:
                print(row[1])
                batteries[battery_id] = Battery(battery_id, row[0], row[1], row[2], row[2], row[2])
                battery_id +=1
        
        return batteries
