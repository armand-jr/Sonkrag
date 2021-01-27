####################################################################################################################
#
# genetic.py from SONKRAG
# Armand Stiens, Willem Folkers, Dionne Ruigrok
# 
# Minor Programmeren UvA 2021
# 
# - Makes n random solution and tries to improve with the genetic_pop_hc algorithm and returns the best solution
# - Also improves the population with the hillclimber algorithm
####################################################################################################################

import copy, random, timeit
from code.algorithms import random as random_algo
from code.algorithms import hillclimber


class Genetic_Pop_HC():
    """
    Implements a genetic population hillclimber algorithm 
    """
    def __init__(self, district, cable_cost, battery_cost, population_size):
        """
        Initializes genetic object
        """
        self.district_population = []
        self.cost_populations = []
        self.population_size = population_size

        self.best_districts = []
        self.best_costs = []
        self.worst_districts = []

        self.parents = []
        self.parent1 = None
        self.parent2 = None
        self.child = None

        self.cable_cost = cable_cost
        self.battery_cost = battery_cost

        # generate n random different solutions
        while len(self.district_population) < self.population_size:
            while True:
                self.district = copy.deepcopy(district)
                firstsolution = random_algo.Random(self.district, cable_cost, battery_cost)
                firstsolution.house_loop()
                firstsolution.change_battery_or_house('change_battery')
                firstsolution.change_battery_or_house('change_house')

                if self.district not in self.district_population:
                    break

            # generate total cost and append to list
            self.district.total_cost(self.battery_cost, self.cable_cost)
            self.district_population.append(self.district)
            self.cost_populations.append(self.district.cost_shared)


    def improve_population(self):
        """
        Improves the population with a hillclimber algorithm
        """
        for index in range(len(self.district_population)):
            district = self.district_population[index]
            districtsolution = hillclimber.HillClimber(district, self.cable_cost, self.battery_cost)
            self.district_population[index] = districtsolution.run(1000, 80000)
            self.cost_populations[index] = district.total_cost(self.battery_cost, self.cable_cost)


    def sort_values(self):
        """
        Split districts into best and worst district based on total cost
        """
        for loopindex in range(0, self.population_size):
            index = self.cost_populations.index(min(self.cost_populations))
            
            if loopindex < int(self.population_size / 2):
                self.best_districts.append(self.district_population[index])
                self.best_costs.append(self.cost_populations[index])
            else:
                self.worst_districts.append(self.district_population[index])
            
            del self.cost_populations[index]
            del self.district_population[index]
    

    def make_parents(self):
        """
        Make parents of 60% of population, 2/3 from best and 1/3 from worst
        """
        self.parents = []
        
        for loopindex in range(0, int(self.population_size * 0.6)):
            while True:
                if loopindex < int(self.population_size * 6 / 15):
                    parent = random.choice(self.best_districts)
                else:
                    parent = random.choice(self.worst_districts)
                    
                if parent not in self.parents:
                    self.parents.append(parent)
                    break
    

    def parents_loop(self):
        """
        Make pairs of parents and create 2 children
        """
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

                childsolution = random_algo.Random(self.child, self.cable_cost, self.battery_cost)
                childsolution.change_battery_or_house('change_battery')
                childsolution.change_battery_or_house('change_house')

                if (self.child.valid_solution() and self.child not in self.district_population
                and self.child not in self.best_districts and self.child not in self.worst_districts):
                    self.district_population.append(self.child)
                    self.cost_populations.append(self.child.total_cost(self.battery_cost, self.cable_cost))
                    children += 1
    
    
    def battery_loop(self):
        """
        Compare batteries and assign battery to house if different
        """
        batteries1 = self.parent1.batteries
        batteries2 = self.parent2.batteries
        batterieschild = self.child.batteries

        for battery in batteries1:
            not_assigned = self.compare_battery(batteries1.get(battery), batteries2.get(battery), batterieschild.get(battery))
            not_assigned = list(set(not_assigned))
            self.assign_battery(batterieschild.get(battery), not_assigned)
    
    
    def compare_battery(self, battery1, battery2, batterieschild):
        """
        If the battery assigned to a house is different for each parent return not assigned
        """
        not_assigned = []
        
        for index in range(len(battery1.houses)):
            if battery1.houses[index] not in battery2.houses:
                not_assigned.append(batterieschild.houses[index])
        
        return not_assigned
 

    def assign_battery(self, old_battery, not_assigned):
        """
        If house in child district has no assigned battery, 80% keeps parent1 battery, else 50/50 chance for closest or random battery
        """
        for house in not_assigned:
            # new_battery = self.closest_battery(old_battery, house)
            random_or_closest = random.choice(["random", "closest"])
            if random_or_closest == "closest":
                new_battery = self.closest_battery(old_battery, house)
            else:
                new_battery = random.choice(list(self.child.batteries.values()))

            self.child.swap_battery(old_battery, new_battery, house)


    def closest_battery(self, old_battery, house):
        """
        Searches for the closest battery and return that battery
        """
        batteries = self.child.batteries
        nearest_battery = None
        shortest_distance = 0

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


    def run(self, no_improv_gen):
        """
        Runs the algorithm and the algorithm breaks after n times not finding a new best 
        """
        bestvalue = min(self.cost_populations)
        no_improvement_tries = 0
        starttime = timeit.default_timer()

        while no_improvement_tries < no_improv_gen:
            endtime = timeit.default_timer()
            print(f"Best value: {bestvalue}, no improvement tries: {no_improvement_tries}, time:{endtime - starttime}")

            self.improve_population()
            self.sort_values()
            self.make_parents()
            self.parents_loop()
            
            # add best of the old population to the population
            while len(self.district_population) < self.population_size:
                index = self.best_costs.index(min(self.best_costs))
                self.cost_populations.append(self.best_costs[index])
                self.district_population.append(self.best_districts[index])
                del self.best_costs[index]
                del self.best_districts[index]

            if min(self.cost_populations) < bestvalue:
                bestvalue = min(self.cost_populations)
                no_improvement_tries = 0
            else:
                no_improvement_tries += 1
            
            self.best_districts = []
            self.best_costs = []
            self.worst_districts = []
        
        bestdistrict = self.cost_populations.index(bestvalue)
        return self.district_population[bestdistrict]
