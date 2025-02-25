class Birds:
    
    def __init__ (self,name,fly_ability,size):
        self.fly_ability = fly_ability
        self.name = name
        self.size = size
    
    def info(self):
        print (f"fly_ability:{self.fly_ability},name:{self.name},size:{self.size}")
    
    def sounding(self):
        print(f"True")

    def eating(self):
        print(f"No")

    def slepping(self):
        print(f"No")

    def __del__ (self):
        print ("del done", self.name)


def bis():
        B = Birds("Guise" ,True, "Big")
        B.info()


def main():
        bis()

if __name__ == '__main__':
        main()
