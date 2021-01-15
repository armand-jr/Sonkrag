from code.classes import district, house, battery
import random, copy

class Random2:
    """
    The Random class randomizes the optimal solution and takes the possibility of sharing the cables into account.
    """
    def __init__(self, district, cable_cost, battery_cost):
        self.district = district
        self.cable_cost = cable_cost
        self.battery_cost = battery_cost
    
        

    def house_loop(self):
        """
        Loops trough all houses and assigns a random battery
        """
        houses = self.district.houses
        batteries = self.district.batteries
        amount = 0

        for house in houses:
            amount += 1
            battery = random.choice(list(batteries.values()))
            battery.add_house(houses.get(house))
            self.district.cable_to_battery(houses.get(house), battery)
        
        print(f"amount: {amount}")

        # for i in batteries:
        #     print(batteries.get(i).used_cap)

        # print(f"{houses}")
            

    def change_battery_or_house(self, bat_or_house):
        """
        If the used capacity exceeds the max capacity, check if it is possible to move house to another battery or to swap houses from batteries
        """
        batteries = self.district.batteries
        for battery in batteries:
            if batteries.get(battery).used_cap > batteries.get(battery).max_cap:
                for newbattery in batteries:
                    if batteries.get(newbattery).used_cap < batteries.get(newbattery).max_cap and newbattery != battery:

                        if bat_or_house == 'change_battery':
                            self.district.check_space_battery(batteries.get(battery), batteries.get(newbattery))

                        else:
                            self.district.swap_house(batteries.get(battery), batteries.get(newbattery))

                        
       
        # print(f"amount: {batteries.get(battery).used_cap}")


    def total_cost(self):
        """
        Calculates the total cost of the cables by calculating the shortest distance between the battery and the assigned houses
        """
        return self.district.total_cost(self.battery_cost, self.cable_cost)


    def __repr__(self):
        return str(self.district.cost_shared)
