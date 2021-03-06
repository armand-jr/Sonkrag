########################################################################
#
# hillclimber.py from SONKRAG
# Armand Stiens, Willem Folkers, Dionne Ruigrok
# 
# Minor Programmeren UvA 2021
# 
# - Tries to improve a given solution with the hillclimber algorithm
########################################################################
import copy, random, timeit


class HillClimber():
    """
    Implements a hill climber algorithm which makes a random change to the solution. If there is a improvement, the new solution is kept.
    """
    def __init__(self, district, cable_cost, battery_cost):
        """
        Initializes hill climber object
        """
        self.district = copy.deepcopy(district)
        self.cable_cost = cable_cost
        self.battery_cost = battery_cost
        self.no_improvement_tries = 0
        self.total_cost = district.total_cost(battery_cost, cable_cost)


    def change(self, new_district):
        """
        Picks two random batteries, picks one house per battery and swaps them if possible
        """
        while True:
            random_battery1 = random.choice(list(new_district.batteries.values()))

            # if both random batteries are the same choose another one
            while True:
                random_battery2 = random.choice(list(new_district.batteries.values()))
                if random_battery1.id != random_battery2.id:
                    break

            random_house1 = random.choice(random_battery1.houses)
            random_house2 = random.choice(random_battery2.houses)

            if (random_battery1.used_cap - random_house1.output + random_house2.output < random_battery1.max_cap
            and random_battery2.used_cap - random_house2.output + random_house1.output < random_battery2.max_cap):
                break

        # removes house from old battery and adds it to the new battery, deleting old path and making a new one
        new_district.swap_battery(random_battery1, random_battery2, random_house1)
        new_district.swap_battery(random_battery2, random_battery1, random_house2)


    def compare(self, new_district):
        """
        Compares the new district to the old district, if the total cost went down the new district is stored as current best district
        """
        old_total_cost = self.total_cost
        new_total_cost = new_district.total_cost(self.battery_cost, self.cable_cost)

        if new_total_cost < old_total_cost:
            self.no_improvement_tries = 0
            self.district = new_district
            self.total_cost = new_total_cost
        else:
            self.no_improvement_tries += 1
            if new_total_cost == old_total_cost:
                self.district = new_district
                self.total_cost = new_total_cost


    def run(self, iterations, no_improv_hill):
        """
        Loop x amount of time through the district making small changes trying to improve the total cost
        """
        self.no_improvement_tries = 0
        starttime = timeit.default_timer()
        
        for iteration in range(1, iterations + 1):
            if iteration % 5000 == 0:
                endtime = timeit.default_timer()
                print(f"Iteration: {iteration}/{iterations}, current best cost: {self.total_cost}, time:{endtime - starttime}")

            new_district = copy.deepcopy(self.district)
            self.change(new_district)
            self.compare(new_district)

            if self.no_improvement_tries >= no_improv_hill:
                break
        
        return self.district
