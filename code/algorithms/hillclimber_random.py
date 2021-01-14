import copy 


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
        pass


    def compare(self, new_district):
        old_total_cost = self.total_cost
        new_total_cost = new_district.total_cost()

        if new_total_cost <= old_total_cost:
            self.district = new_district
            self.total_cost = new_total_cost

    def run(self, iterations=1000):
        self.iterations = iterations
        for iteration in range(iterations):
            new_district = copy.deepcopy(self.district)

            self.change(new_district)

            self.compare(new_district)