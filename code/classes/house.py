class House():
    def __init__(self, x_cor, y_cor, output): #, cables
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.output = output
        self.cables = []

    def add_cable(self, x_cor, y_cor):
        
        #
        self.cables.append(f"{x_cor}, {y_cor}")
