def eulerian_cycle(edge_dict):
    current_node = list(edge_dict.keys())[0]
    path = [current_node]
    while True:
        path.append(edge_dict[current_node][0])

        if len(edge_dict[current_node]) == 1:
            del edge_dict[current_node]
        else:
            edge_dict[current_node] = edge_dict[current_node][1:]

        if path[-1] in edge_dict:
            current_node = path[-1]
        else:
            break
    while len(edge_dict) > 0:
        for i in range(len(path)):
            if path[i] in edge_dict:
                current_node = path[i]
                cycle = [current_node]
                while True:
                    cycle.append(edge_dict[current_node][0])

                    if len(edge_dict[current_node]) == 1:
                        del edge_dict[current_node]
                    else:
                        edge_dict[current_node] = edge_dict[current_node][1:]

                    if cycle[-1] in edge_dict:
                        current_node = cycle[-1]
                    else:
                        break

                path = path[:i] + cycle + path[i+1:]
                break
    return path


def eulerian_path(edge_dict):
    # Determine the unbalanced edges.
    out_values = [neighbor for neighbors in edge_dict.values() for neighbor in neighbors]
    for node in set(out_values + list(edge_dict.keys())):
        out_value = out_values.count(node)
        if node in edge_dict:
            in_value = len(edge_dict[node])
        else:
            in_value = 0

        if in_value < out_value:
            unbalanced_from = node
        elif out_value < in_value:
            unbalanced_to = node

    # Add an edge connecting the unbalanced edges.
    if unbalanced_from in edge_dict:
        edge_dict[unbalanced_from].append(unbalanced_to)
    else:
        edge_dict[unbalanced_from] = [unbalanced_to]

    # Get the Eulerian Cycle from the edges, including the unbalanced edge.
    cycle = eulerian_cycle(edge_dict)

    # Find the location of the unbalanced edge in the eulerian cycle.
    divide_point = next(i for i, x in enumerate(cycle[:-1]) if (x == unbalanced_from and cycle[i+1] == unbalanced_to))

    # Remove the unbalanced edge and shift appropriately, overlapping the head and tail.
    return cycle[divide_point+1:] + cycle[1:divide_point+1]


if __name__ == '__main__':
    # Your input data
    input_data = """0: 2
1: 3
2: 1
3: 0 4
6: 3 7
7: 8
8: 9
9: 6

    """
    edges = {}
    for edge in [line.strip().split(':') for line in input_data.split('\n') if line]:
        if edge[0]:
            node = int(edge[0])
            neighbors = list(map(int, edge[1].split()))
            edges[node] = neighbors

    path = eulerian_path(edges)
    print(' '.join(map(str, path)))
