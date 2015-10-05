import astar
import pathfind_problem

__author__ = 'Andreas'

f = open('boards/board-1-1.txt', 'r')
world = []
x = 0
start_x = 0
start_y = 0
goal_x = 0
goal_y = 0

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

prob = pathfind_problem.Problem(goal_state=[goal_x, goal_y], initial_state=[start_x, start_y], world=world)
solution = astar.cost_search(prob)

print(solution)
parent = solution
new_world = world.copy()

while parent:
    print(parent.state)
    world[parent.state[0]][parent.state[1]] = "x"
    parent = parent.parent

for line in new_world:
    string = ""
    for char in line:
        string += char
    print(string)
