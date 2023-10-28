def a_star(start, goal, heuristic):
      """Implements the A* algorithm.

  Args:
    start: The starting state.
    goal: The goal state.
    heuristic: The heuristic function.

  Returns:
    A list of actions that lead from the start state to the goal state.
  """

  # Initialize the open and closed sets.
  open = set([start])
  closed = set()

  # Initialize the parent map.
  parent = {start: None}

  # Initialize the g-values.
  g = {start: 0}

  # Initialize the f-values.
  f = {start: heuristic(start)}

  # While the open set is not empty:
  while open:

    # Get the node with the lowest f-value.
    node = min(open, key=lambda x: f[x])

    # If the node is the goal node, return the path to it.
    if node == goal:
      path = []
      while node is not None:
        path.append(node)
        node = parent[node]
      return path[::-1]

    # Remove the node from the open set and add it to the closed set.
    open.remove(node)
    closed.add(node)

    # For each neighbor of the node:
    for neighbor in neighbors(node):

      # If the neighbor is not in the closed set:
      if neighbor not in closed:

        # Calculate the g-value and f-value for the neighbor.
        g_neighbor = g[node] + cost(node, neighbor)
        f_neighbor = g_neighbor + heuristic(neighbor)

        # If the neighbor is not in the open set:
        if neighbor not in open:

          # Add the neighbor to the open set and update the parent map.
          open.add(neighbor)
          parent[neighbor] = node

          # Initialize the g-value and f-value for the neighbor.
          g[neighbor] = g_neighbor
          f[neighbor] = f_neighbor

        # Otherwise, if the f-value for the neighbor is higher than the f-value for the node:
        else:

          # Update the g-value and f-value for the neighbor.
          g[neighbor] = g_neighbor
          f[neighbor] = f_neighbor

  # No path to the goal node was found.
  return None