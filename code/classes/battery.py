class Battery():
    def __init__(self, uid, x_cor, y_cor, max_cap):
        self.id = str(uid)
        self.x_cor = int(x_cor)
        self.y_cor = int(y_cor)
        self.max_cap = float(max_cap)
        self.used_cap = 0
        self.houses = []
        self.cables = {}
        self.double_cables_length = 0


    def add_house(self, house): 
        
        # adds a new house
        self.houses.append(house)
        self.used_cap += house.output


    def capacitycheck(self, output):

        # setting a cap on the battery
        new_used_cap = self.used_cap + output
        return new_used_cap < self.max_cap

    def add_cable(self, cable):

        #
        if cable in self.cables:
            self.cables[cable] = self.cables.get(cable) + 1
            self.double_cables_length += 1
        else:
            self.cables[cable] = 1
    
    
    def remove_cable(self, cable):

        #
        if cable in self.cables:
            if self.cables.get(cable) > 1:
                self.cables[cable] = self.cables.get(cable) - 1
                self.double_cables_length = self.double_cables_length - 1
            else:
                self.cables.pop(cable)


    def __repr__(self):
        return str(self.max_cap)