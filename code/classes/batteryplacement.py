# Armand Stiens, Willem Folkers, Dionne Ruigrok

import copy, random
from code.algorithms import greedy2

class batteryplacement:

    def __init__(self, district, battery_cost, cable_cost):
        self.district = district
        self.houses = list(self.district.houses.values())
        self.house_coordinates = []
        self.get_house_locations()

        self.bestdistrict = copy.deepcopy(district)
        self.battery_cost = battery_cost
        self.cable_cost = cable_cost

        answer = greedy2.Greedy2(self.bestdistrict, cable_cost, battery_cost)
        answer.house_loop()
        answer.change_battery_or_house('change_battery')
        answer.change_battery_or_house('change_house')

        self.best_score = self.bestdistrict.total_score(self.battery_cost, self.cable_cost)

    def run(self):
        for index in range(500):
            new_district = copy.deepcopy(self.district)
            batteries = list(new_district.batteries.values())
            coordinates = self.battery_locations()

            for batteryindex in range(len(batteries)):
                coordinate = coordinates[batteryindex].split(',')
                batteries[batteryindex].x_cor = coordinate[0]
                batteries[batteryindex].y_cor = coordinate[1]
            
            answer = greedy2.Greedy2(new_district, self.cable_cost, self.battery_cost)
            answer.house_loop()
            answer.change_battery_or_house('change_battery')
            answer.change_battery_or_house('change_house')

            new_score = new_district.total_score(self.battery_cost, self.cable_cost)

            if new_score < self.best_score:
                self.best_score = new_score
                bestcoordinates = copy.deepcopy(coordinates)

        if len(bestcoordinates) > 0:
            batteries = list(self.district.batteries.values())

            for batteryindex in range(len(batteries)):
                bestcoordinate = bestcoordinates[batteryindex].split(',')
                batteries[batteryindex].x_cor = bestcoordinate[0]
                batteries[batteryindex].y_cor = bestcoordinate[1]


    def battery_locations(self):
        coordinates_list = []
        
        while len(coordinates_list) < 5:
            randomx = random.randint(0,4)
            x_cor = 5 + 10 * randomx

            randomy = random.randint(0,4)
            y_cor = 5 + 10 * randomy

            if f"{x_cor,y_cor}" not in coordinates_list and f"{x_cor,y_cor}" not in self.house_coordinates:
                coordinates_list.append(f"{x_cor,y_cor}")
        
        return coordinates_list

    def get_house_locations(self):
        for house in self.houses:
            self.house_coordinates.append(f"{house.x_cor},{house.y_cor}")
