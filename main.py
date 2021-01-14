from code.classes import district, house, battery
from code.algorithms import greedy, greedy2, random
from code.visualisation import visualise as vis
from code.visualisation import output
from sys import argv

# Constants
CABLECOST = 9
BATTERYCOST = 5000


if __name__ == "__main__":

    # check command line arguments
    if len(argv) != 3:
        print("Usage: python main.py [algorithm] [district number]")
        exit(1)

    if argv[2] not in str([1, 2, 3]):
        print("please choose between district 1, 2 or 3")
        exit(1)

    current_district = str(argv[2])

    # Create a graph from our data
    data_houses = f"data/houses&batteries/district_{current_district}/district-{current_district}_houses.csv"
    data_batteries = f"data/houses&batteries/district_{current_district}/district-{current_district}_batteries.csv"
    
    district = district.District(data_houses, data_batteries)

    #print(district)


    # --------------------------- Algoritmhs -----------------------------------
    if argv[1] == "random":
        """
        Random algorithm
        """
        print("random algorithm chosen")
        answer = random.Random(district, CABLECOST, BATTERYCOST)
        answer.house_loop()
        answer.change_battery()
        answer.swap_houses()
        answer.total_cost()
        # print(answer)


    elif argv[1] == "greedy":
        """
        Greedy algorithm
        """
        print("greedy algorithm chosen")
        answer = greedy.Greedy(district, CABLECOST, BATTERYCOST)
        answer.house_loop()
        answer.change_battery()
        answer.swap_houses()
        answer.total_cost()
        
    
    elif argv[1] == "greedy2":
        """
        Improved greedy algorithm
        """
        print("improved greedy algorithm chosen")
        answer = greedy2.Greedy2(district, CABLECOST, BATTERYCOST)
        answer.house_loop()
        answer.change_battery()
        answer.swap_houses()
        answer.improve_battery_distances()
        answer.total_cost()
        

    else:
        print("this algorithm does not exist")
        exit()




    # --------------------------- Visualisation --------------------------------
    #vis.visualise(district)



    # --------------------------- Output JSON ----------------------------------
    filename = f"results/result_{argv[1]}_district{current_district}.json"
    output.make_json(district, filename, current_district)