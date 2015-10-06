import search_node


def cost_search(problem, queue):
    node = search_node.SearchNode(problem.initial_state, 0, problem.heuristic_eval(problem.initial_state), 0)
    frontier = queue
    frontier.insert(node)
    visited = []

    while frontier:
        active = frontier.pop()
        if problem.goal_test(active.state):
            # We have found a solution
            return active, frontier, visited

        visited.append(active.state)
        children = problem.generate_children(active)

        for child in children:
            # first, check if visited
            if child.state in visited:
                # If node already visited, no
                continue
            # check if in frontier
            elif child in frontier:

                old = frontier.get(child)
                if child.g < old.g:
                    old.replace_with(child)
            # append if in neither
            else:
                frontier.insert(child)

                # Sort list by ascending f

    return False
