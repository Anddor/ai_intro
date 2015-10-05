import search_node


def cost_search(problem):
    node = search_node.SearchNode(problem.initial_state, 0, problem.heuristic(problem.initial_state), 0)
    frontier = [node]
    visited = []

    while frontier:
        active = frontier.pop()

        print(active.state)
        if problem.goal_test(active.state):
            # We have found a solution
            print("solution")
            print("active", active)
            return active

        visited.append(active)
        children = problem.generate_children(active)  # how to make sure generated children will be the same?

        for child in children:
            for node in visited:
                if child.state == node.state:
                    break
            for node in frontier:
                if child.state == node.state and child.get_f() < node.get_f():
                    node.replace_with(child)
                break
            if problem.goal_test(child.state):
                return child
            frontier.append(child)

        # Sort list by ascending f
        frontier.sort(key=search_node.SearchNode.get_f, reverse=True)
    return False
