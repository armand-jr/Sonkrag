from code.classes import district, house, battery
from code.algorithms import greedy
from code.visualisation import visualise as vis

if __name__ == "__main__":

    current_district = str(1)

    # Create a graph from our data
    data_houses = f"data/houses&batteries/district_{current_district}/district-{current_district}_houses.csv"
    data_batteries = f"data/houses&batteries/district_{current_district}/district-{current_district}_batteries.csv"
    
    district = district.District(data_houses, data_batteries)

    #print(district)


    # --------------------------- Algoritmes ---------------------------------------
    answer = greedy.Greedy(district, 9)
    answer.house_loop()
    answer.total_cost()
    print(answer)

    # --------------------------- Visualisation --------------------------------
    vis.visualise(district)
