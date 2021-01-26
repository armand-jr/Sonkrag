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
from code.algorithms import greedy, random, hillclimber, genetic, geneticgreedy
from code.visualisation import visualise as vis
from code.visualisation import output
from sys import argv


# Constants
CABLECOST = 9
BATTERYCOST = 5000
ITERATIONS = 250000
HILL_ITERATIONS = 2
genetic_populations_size = 100 #size * 6 % 15 == 0 and size * 3 % 5 == 0 and size % 2 == 0


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

    # Create a graph from our data
    data_houses = f"data/houses&batteries/district_{current_district}/district-{current_district}_houses.csv"
    data_batteries = f"data/houses&batteries/district_{current_district}/district-{current_district}_batteries.csv"
    
    district = district.District(data_houses, data_batteries)

    if argv[3] == "advanced5":
        batterychange = batteryplacement.batteryplacement(district, CABLECOST, BATTERYCOST)
        batterychange.run()


    # --------------------------- Algoritmhs ---------------------------
    elif argv[1] == "random":
        """
        Random algorithm
        """
        print("random algorithm chosen")
        answer = random.Random(district, CABLECOST, BATTERYCOST)
        answer.house_loop()
        answer.change_battery_or_house('change_battery')
        answer.change_battery_or_house('change_house')
        answer.district.total_cost(BATTERYCOST, CABLECOST)
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
        answer.improve_battery_distances()
        answer.district.total_cost(BATTERYCOST, CABLECOST)
        print(f"total cost: {answer}")


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
            temporarydistrict = districthillclimber.run(ITERATIONS)

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

        for hillclimberiteration in range(1, HILL_ITERATIONS + 1):
            print(f"Hillclimber run: {hillclimberiteration}/{HILL_ITERATIONS}, best value: {bestvalue}")
            districthillclimber = hillclimber.HillClimber(district, CABLECOST, BATTERYCOST)
            temporarydistrict = districthillclimber.run(ITERATIONS)

            if temporarydistrict.cost_shared < bestvalue:
                bestdistrict = temporarydistrict
                bestvalue = temporarydistrict.cost_shared

        district = bestdistrict
        print(f"bestvalue: {bestvalue}")


    elif argv[1] == "genetic":
        """
        Genetic algorithm with random and greedy
        """
        answer = genetic.Genetic(district, CABLECOST, BATTERYCOST, genetic_populations_size)
        district = answer.run()


    elif argv[1] == "geneticgreedy":
        """
        Genetic algorithm with greedy
        """
        answer = geneticgreedy.GeneticGreedy(district, CABLECOST, BATTERYCOST, genetic_populations_size)
        district = answer.run()


    elif argv[1] == "genetichillclimber":
        """
        Genetic hillclimber
        """
        answer = genetic.Genetic(district, CABLECOST, BATTERYCOST, genetic_populations_size)
        district = answer.run()

        bestvalue = district.total_cost(BATTERYCOST, CABLECOST)
        bestdistrict = district
        no_improvement = 0

        for hillclimberiteration in range(1, HILL_ITERATIONS + 1):
            print(f"Hillclimber run: {hillclimberiteration}/{HILL_ITERATIONS}, best value: {bestvalue}")
            districthillclimber = hillclimber.HillClimber(district, CABLECOST, BATTERYCOST)
            temporarydistrict = districthillclimber.run(ITERATIONS)

            if temporarydistrict.cost_shared < bestvalue:
                bestdistrict = temporarydistrict
                bestvalue = temporarydistrict.cost_shared

        district = bestdistrict

    else:
        print("this algorithm does not exist")
        exit()


    # --------------------------- Make filename ---------------------------
    if argv[3] == "advanced5":
            filename = f"results/result_{argv[1]}_district{current_district}{argv[3]}"
    else:
        filename = f"results/result_{argv[1]}_district{current_district}"
    total_cost = district.total_cost(BATTERYCOST, CABLECOST)


    # --------------------------- Visualisation ---------------------------
    vis.visualise(district, argv[1], argv[2], total_cost, f"{filename}.png", argv[3])


    # --------------------------- Output JSON -----------------------------
    output.make_json(district, f"{filename}.json", current_district)