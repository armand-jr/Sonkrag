# Armand Stiens, Willem Folkers, Dionne Ruigrok

import copy, random
from code.algorithms import greedy

class batteryplacement:

    def __init__(self, district, battery_cost, cable_cost):
        self.district = district
        self.houses = list(self.district.houses.values())
        self.house_coordinates = []
        self.get_house_locations()

        self.bestdistrict = copy.deepcopy(district)
        self.battery_cost = battery_cost
        self.cable_cost = cable_cost

        answer = greedy.Greedy(self.bestdistrict, cable_cost, battery_cost)
        answer.house_loop()
        answer.change_battery_or_house('change_battery')
        answer.change_battery_or_house('change_house')

        self.best_score = self.bestdistrict.total_cost(self.battery_cost, self.cable_cost)

    def run(self):
        for index in range(1000):
            if index % 100 == 0:
                print(f"Battery coordinate change {index}/1000")
            
            new_district = copy.deepcopy(self.district)
            batteries = list(new_district.batteries.values())
            coordinates = self.battery_locations()

            for batteryindex in range(len(batteries)):
                coordinate = coordinates[batteryindex]
                coordinate = coordinate.split(',')
                batteries[batteryindex].x_cor = int(coordinate[0])
                batteries[batteryindex].y_cor = int(coordinate[1])
            
            answer = greedy.Greedy(new_district, self.cable_cost, self.battery_cost)
            answer.house_loop()
            answer.change_battery_or_house('change_battery')
            answer.change_battery_or_house('change_house')

            new_score = new_district.total_cost(self.battery_cost, self.cable_cost)

            if new_score < self.best_score:
                self.best_score = new_score
                bestcoordinates = copy.deepcopy(coordinates)

        if len(bestcoordinates) > 0:
            batteries = list(self.district.batteries.values())

            for batteryindex in range(len(batteries)):
                bestcoordinate = bestcoordinates[batteryindex]
                bestcoordinate = bestcoordinate.split(',')
                batteries[batteryindex].x_cor = int(bestcoordinate[0])
                batteries[batteryindex].y_cor = int(bestcoordinate[1])


    def battery_locations(self):
        coordinates_list = []
        
        while len(coordinates_list) < 5:
            randomx = random.randint(0,4)
            x_cor = int(5 + 10 * randomx)

            randomy = random.randint(0,4)
            y_cor = int(5 + 10 * randomy)

            coordinate = f"{x_cor},{y_cor}"

            if coordinate not in coordinates_list and coordinate not in self.house_coordinates:
                coordinates_list.append(coordinate)
        
        return coordinates_list

    def get_house_locations(self):
        for house in self.houses:
            self.house_coordinates.append(f"{house.x_cor},{house.y_cor}")
