class Battery():
    def __init__(self, uid, x_cor, y_cor, max_cap):
        self.id = str(uid)
        self.x_cor = int(x_cor)
        self.y_cor = int(y_cor)
        self.max_cap = float(max_cap)
        self.used_cap = 0
        self.houses = []

    def add_house(self, house): #location, output, cables
        
        #
        self.houses.append(house)
        self.used_cap += house.output

    def capacitycheck(self, output):

        #
        new_used_cap = self.used_cap + output
        return new_used_cap < self.max_cap

    def __repr__(self):
        return str(self.max_cap)