from code.classes import district, house, battery
from code.algorithms import greedy, random
from code.visualisation import visualise as vis
from code.visualisation import output

# Constants
CABLECOST = 9
BATTERYCOST = 5000


if __name__ == "__main__":

    current_district = str(1)

    # Create a graph from our data
    data_houses = f"data/houses&batteries/district_{current_district}/district-{current_district}_houses.csv"
    data_batteries = f"data/houses&batteries/district_{current_district}/district-{current_district}_batteries.csv"
    
    district = district.District(data_houses, data_batteries)

    #print(district)

    # --------------------------- Algoritmes -----------------------------------
    # greedy algorithm
    """
    Greedy algorithm
    """
    # answer = greedy.Greedy(district, CABLECOST)
    # answer.house_loop()
    # answer.change_battery()
    # answer.swap_houses()
    # answer.total_cost()
    """
    Random algorithm
    """
    answer = random.Random(district, CABLECOST, CABLECOST)
    answer.house_loop()
    answer.change_battery()
    answer.swap_houses()
    answer.total_cost()
    
    print(answer)

    # --------------------------- Visualisation --------------------------------
    #vis.visualise(district)



    # --------------------------- Output JSON ----------------------------------
    filename = f"results/result_district{current_district}.json"
    output.make_json(district, filename, current_district)