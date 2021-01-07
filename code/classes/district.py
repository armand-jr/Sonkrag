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
        houses = []

        with open(source_house, 'r') as houses_file:
            reader = csv.DictReader(houses_file)

            for row in reader:
                values = row.split[',']
                houses.append(House(values[0], values[0], values[2]))
        
        return houses


    def load_batteries(self, source_battery):
        """
        load all batteries
        """
        batteries = []

        with open(source_battery, 'r') as batteries_file:
            reader = csv.DictReader(batteries_file)

            for row in reader:
                values = row.split[',']
                coordinaten = values[0].split[',']
                batteries.append(Battery(coordinaten[0], coordinaten[1], values[1]))
        
        return batteries
