"""Import Libraries and Frameworks"""

import random
# import operator
import matplotlib.pyplot
import agentframework
import time
import csv
import sys

start = time.time() # start time counter

rowlist = [] # this creates an empty list
environment=[]
num_of_agents = 10 # this limits the number of agents
num_of_iterations = 100
agents = []

"""Environment CSV"""

f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    environment.append(rowlist)
    for value in row:
        rowlist.append(value)

"""Distance Between Agents"""

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
            ((agents_row_a.y - agents_row_b.y)**2))**0.5

"""Make the Agents"""

for i in range(num_of_agents): # this fills the list of agents
    # agents.append(agentframework.Agent()) 
    agents.append(agentframework.Agent(environment, random.randint(0,99), random.randint(0,99)))

"""Call the Agents"""

for j in range (num_of_iterations):
    for i in range (num_of_agents):
        agents[i].move()
        agents[i].eat()

"""Generate Scatter Graph"""

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

"""Distance Between Agents"""

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 
                
"""Verify that agentframework imported correctly"""

a = agentframework.Agent(environment, random.randint(0,99), random.randint(0,99))
print(a.y, a.x) # show original agents
a.move()
print(a.y, a.x) # show moved agents


"""Check Timing"""

end = time.time() # end time counter
print(end - start) # processing time in seconds