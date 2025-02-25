class Birds:
    
    def __init__ (self,name,fly_ability,size,flying_range):
        self.fly_ability = fly_ability
        self.name = name
        self.size = size
        self.flying_range = flying_range

    def info(self):
        print (f"fly_ability:{self.fly_ability},name:{self.name},size:{self.size},flying_range:{self.flying_range}")
    
    def sounding(self):
        print(f"True")

    def eating(self):
        print(f"No")

    def slepping(self):
        print(f"No")

    def flying_range(self):
        if self.fly_ability == True:
            self.flying_range = self.size * 21
        else:
            self.fly_ability == False
        print (f"flying_range:{self.flying_range}")

    def __del__ (self):
        print ("del done", self.name)
     

def bis():
        B = Birds("Guise" ,True, "Big", True)
        B.info()
bis()

