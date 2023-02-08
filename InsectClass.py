import random

class Insect: 
    def __init__(self):
        self.wing= 2 
        self.legs = 4
        self.flight= 0 

    def length(self): 
        if random.randint(1,10) == 0:
            self.flight() 
            


