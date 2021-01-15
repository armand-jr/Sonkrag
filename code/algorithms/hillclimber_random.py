import copy, random
from code.algorithms import random2

class HillClimber(random2.Random2):
    """
    Implements a Hill Climber algorithm which makes a random change to the solution. If there is a improvement, the new solution is kept.
    """

    def __init__(self, district, cable_cost, battery_cost):
        if not district.valid_solution():
            raise Exception("HillClimber needs a complete solution. Please run the random algorithm first")

        self.district = copy.deepcopy(district)
        self.cable_cost = cable_cost
        self.battery_cost = battery_cost
        self.no_improvement_tries = 0
        self.total_cost = district.total_cost(battery_cost, cable_cost)

    def change(self, new_district):
        """
        Picks two random batteries, picks one house per battery and swaps them if possible
        """

        random_battery1 = random.choice(list(new_district.batteries.values()))

        # if both random batteries are the same choose another one
        while True:
            random_battery2 = random.choice(list(new_district.batteries.values()))
            if random_battery1.id != random_battery2.id:
                break

        random_house1 = random.choice(random_battery1.houses)
        random_house2 = random.choice(random_battery2.houses)

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


    def run(self, iterations):
        """
        Loop x amount of time through the district making small changes trying to improve the total cost
        """

        # self.iterations = iterations
        self.no_improvement_tries = 0
        for iteration in range(1, iterations + 1):
            if iteration % 100 == 0:
                print(f"Iteration: {iteration}/{iterations}, current best cost: {self.total_cost}")

            new_district = copy.deepcopy(self.district)

            self.change(new_district)

            self.compare(new_district)

            if self.no_improvement_tries >= 10000:
                break
        
        return self.district

