class Books:
    def __init__ (self,pages,ganr):
        self.pages = pages
        self.ganr = ganr
    def info(self):
        print (f"pages:{self.pages},ganr:{self.ganr}")
    def __del__ (self):
        print ("del done", self.pages)

B = Books(543, "advanture") 
B.info()   