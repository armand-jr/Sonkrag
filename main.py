from code.classes import district, house, battery
from code.algorithms import greedy, greedy2, random, random2, hillclimber_random
from code.visualisation import visualise as vis
from code.visualisation import output
from sys import argv

# Constants
CABLECOST = 9
BATTERYCOST = 5000
hillclimberiterations = 10


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
        print(f"total cost: {answer}")



    elif argv[1] == "random2":
        """
        Random algorithm 2
        """
        print("random algorithm chosen")
        answer = random2.Random2(district, CABLECOST, BATTERYCOST)
        answer.house_loop()
        answer.change_battery_or_house('change_battery')
        answer.change_battery_or_house('change_house')
        answer.total_cost()
        print(f"total cost: {answer}")


    elif argv[1] == "greedy":
        """
        Greedy algorithm
        """
        print("greedy algorithm chosen")
        answer = greedy.Greedy(district, CABLECOST, BATTERYCOST)
        answer.house_loop()
        answer.change_battery_or_house('change_battery')
        answer.change_battery_or_house('change_house')
        answer.total_cost()
        print(f"total cost: {answer}")
        
    
    elif argv[1] == "greedy2":
        """
        Improved greedy algorithm
        """
        print("improved greedy algorithm chosen")
        answer = greedy2.Greedy2(district, CABLECOST, BATTERYCOST)
        answer.house_loop()
        # answer.change_battery()
        # answer.swap_houses()
        answer.change_battery_or_house('change_battery')
        answer.change_battery_or_house('change_house')
        
        # answer.improve_battery_distances()
        answer.total_cost()
        print(f"total cost: {answer}")


    elif argv[1] == "hillclimber":
        """
        Hillclimber algorithm with random
        """
        print("hillclimber algorithm with random for start answer")
        startanswer = random2.Random2(district, CABLECOST, BATTERYCOST)
        startanswer.house_loop()
        startanswer.change_battery_or_house('change_battery')
        startanswer.change_battery_or_house('change_house')

        bestvalue = district.total_cost(BATTERYCOST, CABLECOST)
        bestdistrict = district
        no_improvement = 0

        for hillclimberiteration in range(1, hillclimberiterations + 1):
            print(f"Hillclimber run: {hillclimberiteration}/{hillclimberiterations}, best value: {bestvalue}")
            districthillclimber = hillclimber_random.HillClimber(district, CABLECOST, BATTERYCOST)
            temporarydistrict = districthillclimber.run(50000)

            if temporarydistrict.cost_shared < bestvalue:
                bestdistrict = temporarydistrict
                bestvalue = temporarydistrict.cost_shared
                no_improvement = 0
            else:
                no_improvement += 1
                if no_improvement >= 30000:
                    break

        district = bestdistrict
        print(f"bestvalue: {bestvalue}")


    else:
        print("this algorithm does not exist")
        exit()




    # --------------------------- Visualisation --------------------------------
    filename = f"results/result_{argv[1]}_district{current_district}.png"
    vis.visualise(district, filename)



    # --------------------------- Output JSON ----------------------------------
    filename = f"results/result_{argv[1]}_district{current_district}.json"
    output.make_json(district, filename, current_district)