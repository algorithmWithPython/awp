def coloring(adj, number_of_nodes, colors):
    node_color = [-1]*number_of_nodes
    number_of_color = len(colors)

    def dfs(node):
        if node == number_of_nodes:
            print_result()
            return
        
        for i in range(number_of_color):
            valid = True
            for j in adj[node]:
                if node_color[j] == i:
                    valid = False
                    break
            if valid:
                node_color[node] = i
                dfs(node+1)
                node_color[node] = -1

    def print_result():
        print("solution:")
        for i, c in enumerate(node_color):
            print(f'node {i}: {colors[c]}')
        print()

    dfs(0)

coloring({0: [1,3], 1: [0, 2, 3], 2: [1,3], 3: [0,1,2,4], 4: [3]}, 5, ['Y', 'B', "G"])

        

