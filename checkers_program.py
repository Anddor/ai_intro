__author__ = 'Andreas'
import astar
import checkers_problem

f = open('checkers.txt', 'r')
world = []
for line in f:
    line = line.strip().split(',')
    world.append(line)

print(world)

g_file = open('checkers_goal.txt', 'r')
goal = []
for line in g_file:
    line = line.strip().split(',')
    goal.append(line)

print(goal)
prob = checkers_problem.Problem(goal_state=goal, initial_state=world)
solution = astar.cost_search(prob)
print(solution)
