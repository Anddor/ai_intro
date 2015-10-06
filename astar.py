import search_node
import prique


def cost_search(problem):
    node = search_node.SearchNode(problem.initial_state, 0, problem.heuristic(problem.initial_state), 0)
    frontier = prique.Frontier()
    frontier.insert(node)
    visited = []

    while frontier:
        active = frontier.pop()
        problem.print_state(active.state)

        if problem.goal_test(active.state):
            # We have found a solution
            return active

        visited.append(active.state)
        children = problem.generate_children(active)

        for child in children:
            # check if visited
            if child.state in visited:
                # No further actions
                continue
            # check if in frontier
            elif frontier.contains(child):
                old = frontier.get(child.state)
                if child.get_f() < old.get_f():
                    old.replace_with(child)
            # append if in neither
            else:
                frontier.insert(child)

        # Sort list by ascending f

    return False

