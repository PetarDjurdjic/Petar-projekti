def de_bruijn_graph(k, text):
    graph = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k - 1]
        suffix = text[i + 1:i + k]

        if kmer in graph:
            graph[kmer].append(suffix)
        else:
            graph[kmer] = [suffix]

    return graph

def print_de_bruijn_graph(graph):
    for node, neighbors in sorted(graph.items()):
        if neighbors:
            print(f"{node}:", ' '.join(neighbors))

# Example usage:
k = 4
text = "AAGATTCTCTAAGA"
result_graph = de_bruijn_graph(k, text)
print_de_bruijn_graph(result_graph)



