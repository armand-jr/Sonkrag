from code.classes import district, house, battery
from code.algorithms import greedy, random
from code.visualisation import visualise as vis

# Constants
CABLECOST = 9

if __name__ == "__main__":

    current_district = str(3)

    # Create a graph from our data
    data_houses = f"data/houses&batteries/district_{current_district}/district-{current_district}_houses.csv"
    data_batteries = f"data/houses&batteries/district_{current_district}/district-{current_district}_batteries.csv"
    
    district = district.District(data_houses, data_batteries)

    #print(district)


    # --------------------------- Algoritmes -----------------------------------
    # greedy algorithm
    # answer = greedy.Greedy(district, CABLECOST)
    # random algorithm
    answer = random.Random(district, CABLECOST)
    answer.house_loop()
    answer.total_cost()
    # print(answer)

    # --------------------------- Visualisation --------------------------------
    vis.visualise(district)
