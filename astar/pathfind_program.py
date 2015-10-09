from sys import stdin
import sys

import astar
import pathfind_problem
import board_image_gen
from astar import prique

__author__ = 'Andreas'
f = stdin.readlines()
# Instantiate variables
world = []
x = 0
start_x = 0
start_y = 0
goal_x = 0
goal_y = 0

# fetches the command line arguments
args = sys.argv
if len(args) > 1:
    # if there are any command line arguments:
    ALGORITHM_TYPE = args[1]
else:
    # Fallback on astar
    ALGORITHM_TYPE = "astar"

print(ALGORITHM_TYPE)

# Parse board file:
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


# Choose queue and heuristic:
# -- ASTAR -- Priority queue and heuristic
queue = prique.Frontier()
heuristic = True

if ALGORITHM_TYPE == "d":
    # -- Dijkstra -- Priority queue and no heuristic
    queue = prique.Frontier()
    heuristic = False
elif ALGORITHM_TYPE == "b":
    # -- BFS -- FIFO queue and no heuristic
    queue = prique.BfsQueue()
    heuristic = False

# Create problem file:
prob = pathfind_problem.Problem((goal_x, goal_y), (start_x, start_y), world, heuristic)
# Call search algorithm
solution, frontier, visited = astar.cost_search(prob, queue)

# Create image
board_gen = board_image_gen.Board_img_gen(len(world[0]), len(world), 50)
# Draw world
board_gen.draw_world(world)
# Draw visited nodes
board_gen.draw_open_closed(visited, "x")
# Draw open nodes
board_gen.draw_open_closed([node.state for node in frontier.h], "o")

# Reconstruct the path taken to goal, by going backwards from parent to parent
parent = solution.parent
path = []

while parent.parent:
    path.append(parent.state)
    parent = parent.parent

# Draw the reconstructed path
board_gen.draw_open_closed(path, " >")

# Show the drawn image
board_gen.show_img()



