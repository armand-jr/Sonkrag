# Armand Stiens, Willem Folkers, Dionne Ruigrok

class House():
    def __init__(self, uid, x_cor, y_cor, output): #, cables
        """
        Initializes the house object
        """
        self.id = str(uid)
        self.x_cor = int(x_cor)
        self.y_cor = int(y_cor)
        self.output = float(output)
        self.cables = []


    def add_cable(self, x_cor, y_cor):
        """
        Adds cable to house. Takes the x and y coordinate as integer inputs
        """
        self.cables.append(f"{x_cor},{y_cor}")


    def __repr__(self):
        return self.id
        