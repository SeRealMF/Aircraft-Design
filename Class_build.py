



class Moment:
    def __init__(self, Weight, X_Dis_m, Dicr, Z_Dis_m = 0, Y_Dis_m = 0):


        self.dic = Dicr



        self.Weight = float(Weight)
        self.x = float(X_Dis_m)
        self.z = float(Z_Dis_m)
        self.y = float(Y_Dis_m)

        self.Mom_x = self.x * self.Weight

        if self.z != 0:
            self.Mom_z = self.z * self.Weight
        else: self.Mom_z = 0

        if self.y != 0:
            self.Mom_y = self.y * self.Weight
        else: self.Mom_y = 0

        """if "Weights" not in self.dic.keys():
            self.dic["Weights"] = 0"""

        self.dic["Weights"] += self.Weight
        self.dic["Mom_x"] += self.Mom_x
        self.dic["Mom_z"] += self.Mom_z
        self.dic["Mom_y"] += self.Mom_y


        


