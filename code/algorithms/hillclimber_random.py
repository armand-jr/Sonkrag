import copy, random


class HillClimber:
    """
    Implements a Hill Climber algorithm which makes a random change to the solution. If there is a improvement, the new solution is kept.
    """

    def __init__(self, district, cable_cost, battery_cost):
        if not district.valid_solution():
            raise Exception("HillClimber needs a complete solution. Please run the random algorithm first")

        self.district = copy.deepcopy(district)

        # waar komt dit vandaan TODO
        self.total_cost = district.total_cost()
    

    def change(self, new_district):
        """
        Picks two random batteries, picks one house per battery and swaps them if possible
        """
        

        random_battery1 = random.choice(list(new_districts.batteries.values()))

        # if both random batteries are the same choose another one
        while True:
            random_battery2 = random.choice(list(new_districts.batteries.values()))
            if random_battery1 != random_battery2:
                break

        random_house1 = random.choice(random_battery1.houses)
        random_house2 = random.choice(random_battery2.houses)


        houseswap1 = random
        houseswap2 = None


        


    def compare(self, new_district):
        old_total_cost = self.total_cost
        new_total_cost = new_district.total_cost()

        if new_total_cost <= old_total_cost:
            self.district = new_district
            self.total_cost = new_total_cost


    def run(self, iterations=1000):
        # self.iterations = iterations

        for iteration in range(iterations):
            new_district = copy.deepcopy(self.district)

            self.change(new_district)

            self.compare(new_district)

