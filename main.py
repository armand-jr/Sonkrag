########################################################################
#
# main.py from SONKRAG
# Armand Stiens, Willem Folkers, Dionne Ruigrok
# 
# Minor Programmeren UvA 2021
# 
# - Choose district and algorithm and run the program
# - Creates file name
# - Creates visualisation
# - Creates JSON output file
########################################################################


from code.classes import district, house, battery, batteryplacement
from code.algorithms import greedy, random, hillclimber, genetic, genetic_pop_hc
from code.visualisation import visualise as vis
from code.visualisation import output
from sys import argv
import timeit, copy


# Constants
CABLECOST = 9
BATTERYCOST = 5000
ITERATIONS = 250000
HILL_ITERATIONS = 5
GENETIC_POPULATION_SIZE = 100
NO_IMPROV_HILL = 80000
NO_IMPROV_GEN = 100



if __name__ == "__main__":

    # check command line arguments
    if len(argv) != 4:
        print("Usage: python main.py [algorithm] [district number] [basis/advanced5]")
        exit(1)

    if argv[2] not in str([1, 2, 3]):
        print("please choose between district 1, 2 or 3")
        exit(1)

    if argv[3] not in ["basis", "advanced5"]:
        print("please choose between basis or advanced5")
        exit(1)

    current_district = str(argv[2])

    # make variable of the data
    data_houses = f"data/houses&batteries/district_{current_district}/district-{current_district}_houses.csv"
    data_batteries = f"data/houses&batteries/district_{current_district}/district-{current_district}_batteries.csv"
    
    district = district.District(data_houses, data_batteries)


    # check if user wants different battery placement or not
    if argv[3] == "advanced5":
        batterychange = batteryplacement.batteryplacement(district, CABLECOST, BATTERYCOST)
        batterychange.run()


    # --------------------------- Algoritmhs ---------------------------
    elif argv[1] == "random":
        """
        Random algorithm
        """
        print("random algorithm chosen")

        starttime = timeit.default_timer()
        bestdistrict = district
        best_value = 0
        for index in range(790000):
            temporarydistrict = copy.deepcopy(district)

            answer = random.Random(temporarydistrict, CABLECOST, BATTERYCOST)
            answer.house_loop()
            answer.change_battery_or_house('change_battery')
            answer.change_battery_or_house('change_house')
            answer.district.total_cost(BATTERYCOST, CABLECOST)
            endtime = timeit.default_timer()
            uid += 1
            
            if best_value == 0 or temporarydistrict.cost_shared < best_value:
                best_value = temporarydistrict.cost_shared
                bestdistrict = temporarydistrict
            print(f"id: {index}, total cost: {answer}, best value: {best_value}, time:{endtime - starttime}")
        district = bestdistrict


    elif argv[1] == "greedy":
        """
        Greedy algorithm
        """
        print("greedy algorithm chosen")
        starttime = timeit.default_timer()
        bestdistrict = district
        best_costs = 0
        
        for i in range(1, 180001):
            temporarydistrict = copy.deepcopy(district)
            answer = greedy.Greedy(temporarydistrict, CABLECOST, BATTERYCOST)
            answer.house_loop()
            answer.change_battery_or_house('change_battery')
            answer.change_battery_or_house('change_house')
            answer.improve_battery_distances()
            answer.district.total_cost(BATTERYCOST, CABLECOST)

            if best_costs == 0 or temporarydistrict.cost_shared < best_costs:
                best_costs = temporarydistrict.cost_shared
                bestdistrict = temporarydistrict

            endtime = timeit.default_timer()
            print(f"total cost: {answer}, run:{i}/180000, endtime: {endtime - starttime}")
        
        district = bestdistrict

        print(f"total cost: {district.cost_shared}")


    elif argv[1] == "hillclimber":
        """
        Hillclimber algorithm with random
        """
        print("hillclimber algorithm with random for start answer")
        startanswer = random.Random(district, CABLECOST, BATTERYCOST)
        startanswer.house_loop()
        startanswer.change_battery_or_house('change_battery')
        startanswer.change_battery_or_house('change_house')
        bestvalue = district.total_cost(BATTERYCOST, CABLECOST)
        bestdistrict = district
        no_improvement = 0

        for hillclimberiteration in range(1, HILL_ITERATIONS + 1):
            print(f"Hillclimber run: {hillclimberiteration}/{HILL_ITERATIONS}, best value: {bestvalue}")
            districthillclimber = hillclimber.HillClimber(district, CABLECOST, BATTERYCOST)
            temporarydistrict = districthillclimber.run(ITERATIONS, NO_IMPROV_HILL)

            if temporarydistrict.cost_shared < bestvalue:
                bestdistrict = temporarydistrict
                bestvalue = temporarydistrict.cost_shared

        district = bestdistrict
        print(f"bestvalue: {bestvalue}")


    elif argv[1] == "hillclimbergreedy":
        """
        Hillclimber algorithm with greedy
        """
        print("hillclimber algorithm with greedy for start answer")
        startanswer = greedy.Greedy(district, CABLECOST, BATTERYCOST)
        startanswer.house_loop()
        startanswer.change_battery_or_house('change_battery')
        startanswer.change_battery_or_house('change_house')
        startanswer.improve_battery_distances()

        bestvalue = district.total_cost(BATTERYCOST, CABLECOST)
        bestdistrict = district
        no_improvement = 0

        # run hill climber with n iterations
        for hillclimberiteration in range(1, HILL_ITERATIONS + 1):
            print(f"Hillclimber run: {hillclimberiteration}/{HILL_ITERATIONS}, best value: {bestvalue}")
            districthillclimber = hillclimber.HillClimber(district, CABLECOST, BATTERYCOST)
            temporarydistrict = districthillclimber.run(ITERATIONS, NO_IMPROV_HILL)

            # save best answer
            if temporarydistrict.cost_shared < bestvalue:
                bestdistrict = temporarydistrict
                bestvalue = temporarydistrict.cost_shared

        district = bestdistrict
        print(f"bestvalue: {bestvalue}")


    elif argv[1] == "genetic":
        """
        Genetic algorithm with random and greedy
        """
        answer = genetic.Genetic(district, CABLECOST, BATTERYCOST, GENETIC_POPULATION_SIZE)
        district = answer.run(NO_IMPROV_GEN)


    elif argv[1] == "genetic_pop_hc":
        """
        Genetic algorithm with greedy
        """
        answer = genetic_pop_hc.Genetic_Pop_HC(district, CABLECOST, BATTERYCOST, GENETIC_POPULATION_SIZE)
        district = answer.run(NO_IMPROV_GEN)


    elif argv[1] == "genetichillclimber":
        """
        Genetic hillclimber
        """
        answer = genetic.Genetic(district, CABLECOST, BATTERYCOST, GENETIC_POPULATION_SIZE)
        district = answer.run(NO_IMPROV_GEN)

        bestvalue = district.total_cost(BATTERYCOST, CABLECOST)
        bestdistrict = district
        no_improvement = 0

        # run hill climber with n iterations
        for hillclimberiteration in range(1, HILL_ITERATIONS + 1):
            print(f"Hillclimber run: {hillclimberiteration}/{HILL_ITERATIONS}, best value: {bestvalue}")
            districthillclimber = hillclimber.HillClimber(district, CABLECOST, BATTERYCOST)
            temporarydistrict = districthillclimber.run(ITERATIONS, NO_IMPROV_HILL)
            
            # save best answer
            if temporarydistrict.cost_shared < bestvalue:
                bestdistrict = temporarydistrict
                bestvalue = temporarydistrict.cost_shared

        district = bestdistrict

    else:
        print("this algorithm does not exist")
        exit()


    # --------------------------- Make filename ---------------------------
    if argv[3] == "advanced5":
            filename = f"result_{argv[1]}_district{current_district}{argv[3]}"
    else:
        filename = f"result_{argv[1]}_district{current_district}"
    total_cost = district.total_cost(BATTERYCOST, CABLECOST)


    # --------------------------- Visualisation ---------------------------
    vis.visualise(district, argv[1], argv[2], total_cost, f"results/images/{filename}.png", argv[3])


    # --------------------------- Output JSON -----------------------------
    output.make_json(district, f"results/{filename}.json", current_district)
