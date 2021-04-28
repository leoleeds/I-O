import random

"""Creat Agent Class and Definitions"""

class Agent():
    def __init__(self, environment, y, x):
        self.environment=environment
        self.store=0
        # self.x=random.randint(0,99)
        # self.y=random.randint(0,99)
        self.x=x
        self.y=y
                
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100    
            
    def eat(self): 
            if self.environment[self.y][self.x] > 10:
                  self.environment[self.y][self.x] -= 10
                  self.store += 10