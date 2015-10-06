from sys import stdin
import astar
import pathfind_problem

__author__ = 'Andreas'
f = stdin.readlines()
world = []
x = 0
start_x = 0
start_y = 0
goal_x = 0
goal_y = 0

# Parse file:
for line in f:
    l = []
    y = 0
    for char in line:
        if char == "A":
            start_x = x
            start_y = y
        elif char == "B":
            goal_y = y
            goal_x = x

        l.append(char)
        y += 1
    x += 1
    world.append(l)

# Create problem file:
prob = pathfind_problem.Problem(goal_state=(goal_x, goal_y), initial_state=(start_x, start_y), world=world)
# Do search:
solution = astar.cost_search(prob)

parent = solution.parent

while parent.parent:
    world[parent.state[0]][parent.state[1]] = "x"
    parent = parent.parent

for line in world:
    string = ""
    for char in line:
        string += char
    print(string)
