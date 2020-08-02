def hamiltonian_cycle(adj, number_of_nodes, s):
    path = []

    def dfs():
        # base case
        if len(path) == number_of_nodes:
            if s in adj[path[-1]]:
                print_path()

        for node in adj[path[-1]]:
            if node not in path: # prune
                path.append(node)
                dfs()
                path.pop() # backtracking

    def print_path():
        print("path:", '->'.join(map(str, path)), end='')
        print(f'->{path[0]}')

    path=[s]
    dfs()
    
adj = {0:[1,2,3], 1:[0,2,4,5], 2:[0,1,3,5], 3:[0,2,5], 4:[1,5], 5:[1,2,3,4]}
hamiltonian_cycle(adj, 6, 0)

