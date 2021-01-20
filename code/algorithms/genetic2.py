########################################################################
#
# genetic.py from SONKRAG
# Armand Stiens, Willem Folkers, Dionne Ruigrok
# 
# Minor Programmeren UvA 2021
# 
# - ...
# - ...
########################################################################

import copy, random, timeit
from code.algorithms import random2

class Genetic(random2.Random2):

    def __init__(self, district, cable_cost, battery_cost, population_size):
        self.district_population = []
        self.cost_populations = []
        self.population_size = population_size

        self.parents = []
        self.parents_score = []
        self.parent1 = None
        self.parent2 = None
        self.child = None

        self.cable_cost = cable_cost
        self.battery_cost = battery_cost

        while len(self.district_population) < self.population_size:
            while True:
                self.district = copy.deepcopy(district)
                firstsolution = random2.Random2(self.district, cable_cost, battery_cost)
                firstsolution.house_loop()
                firstsolution.change_battery_or_house('change_battery')
                firstsolution.change_battery_or_house('change_house')

                if self.district not in self.district_population:
                    break

            self.district.total_cost(self.battery_cost, self.cable_cost)
            self.district_population.append(self.district)
            self.cost_populations.append(self.district.cost_shared)
    

    def make_parents(self):
        self.parents = copy.deepcopy(self.district_population)
        self.parents_score = copy.deepcopy(self.cost_populations)

        while len(self.parents) > int(self.population_size * 0.6):
            index = self.parents_score.index(max(self.parents_score))
            del self.parents[index]
            del self.parents_score[index]


    def parents_loop(self):
        while len(self.parents) > 0:
            children = 0
            self.parent1 = random.choice(self.parents)
            index = self.parents.index(self.parent1)
            del self.parents[index]
            self.parent2 = random.choice(self.parents)
            index = self.parents.index(self.parent2)
            del self.parents[index]

            while children < 2:
                self.child = copy.deepcopy(self.parent1)
                
                self.battery_loop()

                childsolution = random2.Random2(self.child, self.cable_cost, self.battery_cost)
                childsolution.change_battery_or_house('change_battery')
                childsolution.change_battery_or_house('change_house')

                if (self.child.valid_solution() and self.child not in self.district_population):
                    self.district_population.append(self.child)
                    self.cost_populations.append(self.child.total_cost(self.battery_cost, self.cable_cost))
                    children += 1
    
    
    def battery_loop(self):
        batteries1 = self.parent1.batteries
        batteries2 = self.parent2.batteries
        batterieschild = self.child.batteries

        for battery in batteries1:
            not_assigned = self.compare_battery(batteries1.get(battery), batteries2.get(battery), batterieschild.get(battery))
            not_assigned = list(set(not_assigned))
            self.assign_battery(batterieschild.get(battery), not_assigned)
    
    
    def compare_battery(self, battery1, battery2, batterieschild):
        not_assigned = []
        
        for index in range(len(battery1.houses)):
            if battery1.houses[index] not in battery2.houses:
                not_assigned.append(batterieschild.houses[index])
        
        return not_assigned


    def assign_battery(self, old_battery, not_assigned):
        for house in not_assigned:
            random_battery = random.choice(list(self.child.batteries.values()))
            self.child.swap_battery(old_battery, random_battery, house)


    def run(self):
        bestvalue = min(self.cost_populations)
        no_improvement_tries = 0
        starttime = timeit.default_timer()

        while no_improvement_tries < 10000:
            endtime = timeit.default_timer()
            print(f"Best value: {bestvalue}, no improvement tries: {no_improvement_tries}, time:{endtime - starttime}")

            self.make_parents()
            self.parents_loop()
            
            while len(self.district_population) > self.population_size:
                index = self.cost_populations.index(max(self.cost_populations))
                del self.district_population[index]
                del self.cost_populations[index]

            if min(self.cost_populations) < bestvalue:
                bestvalue = min(self.cost_populations)
                no_improvement_tries = 0
            else:
                no_improvement_tries += 1
        
        bestdistrict = self.cost_populations.index(bestvalue)
        return self.district_population[bestdistrict]
