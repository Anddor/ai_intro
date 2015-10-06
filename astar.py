import search_node


def cost_search(problem, queue):
    # Generates the root node, from the initial state in the problem set
    node = search_node.SearchNode(problem.initial_state, 0, problem.heuristic_eval(problem.initial_state), 0)
    # Initiates the empty frontier. The type of queue is specified by parameter.
    frontier = queue
    # Root node is put in frontier
    frontier.insert(node)
    visited = []

    # The agenda loop runs as long as there are one or more items in the frontier
    while frontier:
        # A new node is popped from the queue.
        active = frontier.pop()

        if problem.goal_test(active.state):
            # We have found a solution
            return active, frontier, visited

        # The opened node is put in the list of visited nodes
        visited.append(active.state)
        # The active node is expanded, it's children/successors generated
        children = problem.generate_children(active)

        for child in children:
            # first, check if visited
            if child.state in visited:
                # If node already visited, no further action
                continue
            # check if in frontier
            elif child in frontier:
                # We fetch the old node with the same state
                old = frontier.get(child)
                if child.g < old.g:
                    # if the new node has a shorter path, the old node is replaced
                    old.replace_with(child)
            else:
                # node is put in frontier if in neither visited nor
                frontier.insert(child)

                # Sort list by ascending f

    return False
