from sys import stdin
import astar
import pathfind_problem
import board_image_gen

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
    for char in line.strip():
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
board_gen = board_image_gen.Board_img_gen(len(world[0]), len(world), 50)
board_gen.draw_world(world)
board_gen.show_img()
prob = pathfind_problem.Problem(goal_state=(goal_x, goal_y), initial_state=(start_x, start_y), world=world)

solution, frontier, visited = astar.cost_search(prob)
parent = solution.parent
board_gen.draw_open_closed(visited, "x")
board_gen.draw_open_closed([node.state for node in frontier.h], "o")

path = []

while parent.parent:
    path.append(parent.state)
    parent = parent.parent

board_gen.draw_open_closed(path, " >")


board_gen.show_img()



