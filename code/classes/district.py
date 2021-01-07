import csv

from .house import House
from .battery import Battery

class District ():

    # TODO initialize
    def __init__(self, source_battery, source_house):
        self.houses = self.load_houses(source_house)
        self.batteries = self.load_batteries(source_battery)
        

    # open csv file
    def load_houses(self, source_house):
        """
        load all houses
        """
        with open(source_house, 'r'):
            


    def load_batteries(self, source_battery):
        """
        load all batteries
        """
        with open(source_battery, 'r'):
