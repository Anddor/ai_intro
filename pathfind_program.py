from sys import stdin
import astar
import pathfind_problem
import board_image_gen
import prique

__author__ = 'Andreas'
f = stdin.readlines()
# Instantiate variables
world = []
x = 0
start_x = 0
start_y = 0
goal_x = 0
goal_y = 0

ALGORITHM_TYPE = "b"



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


# Choose queue:
queue = prique.Frontier()
heuristic = True

if ALGORITHM_TYPE == "d":
    queue = prique.Frontier()
    heuristic = False
elif ALGORITHM_TYPE == "b":
    queue = prique.BfsQueue()
    heuristic = False

# Create problem file:
prob = pathfind_problem.Problem((goal_x, goal_y), (start_x, start_y), world, heuristic)
# Call A* algorithm
solution, frontier, visited = astar.cost_search(prob, queue)

# Draw world
board_gen = board_image_gen.Board_img_gen(len(world[0]), len(world), 50)
board_gen.draw_world(world)
board_gen.draw_open_closed(visited, "x")
board_gen.draw_open_closed([node.state for node in frontier.h], "o")

parent = solution.parent
path = []

while parent.parent:
    path.append(parent.state)
    parent = parent.parent

board_gen.draw_open_closed(path, " >")


board_gen.show_img()



