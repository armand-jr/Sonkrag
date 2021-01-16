# Armand Stiens, Willem Folkers, Dionne Ruigrok

class Battery():
    def __init__(self, uid, x_cor, y_cor, max_cap):
        """
        Initializes the battery object
        """
        self.id = str(uid)
        self.x_cor = int(x_cor)
        self.y_cor = int(y_cor)
        self.max_cap = float(max_cap)
        self.used_cap = 0
        self.houses = []
        self.cables = {}
        self.double_cables_length = 0


    def add_house(self, house): 
        """
        Adds a new house to the battery and adjusts used capacity. Takes as input house as object
        """
        self.houses.append(house)
        self.used_cap += house.output


    def capacitycheck(self, output):
        """
        Setting the new used capacity of the battery. Takes as input output as integer.
        Gives True if some capacity of battery is left, else False
        """
        new_used_cap = self.used_cap + output
        return new_used_cap < self.max_cap

    def add_cable(self, cable):
        """
        Adds cable to double-count. Takes as input the cable as ???
        """
        if cable in self.cables:
            self.cables[cable] = self.cables.get(cable) + 1
            self.double_cables_length += 1
        else:
            self.cables[cable] = 1
    
    
    def remove_cable(self, cable):
        """
        Removes cable from double-count. Takes as input the cable as ???? TODO
        """
        if cable in self.cables:
            if self.cables.get(cable) > 1:
                self.cables[cable] = self.cables.get(cable) - 1
                self.double_cables_length = self.double_cables_length - 1
            else:
                self.cables.pop(cable)


    def __repr__(self):
        return str(self.max_cap)