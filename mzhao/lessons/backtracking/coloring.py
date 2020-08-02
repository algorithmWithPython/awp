def coloring(adj, number_of_nodes, colors):
    node_color = [-1]*number_of_nodes
    number_of_color = len(colors)

    def dfs(node):
        # base case
        if node == number_of_nodes:
            print_color()
            return

        for i in range(number_of_color):
            isValid = True
            for n in adj[node]:
                if node_color[n] == i:
                    isValid = False
                    break
            if isValid:
                node_color[node] = i
                dfs(node+1)
                node_color[node] = -1 # backtracking
            
    def print_color():
        print("the solution is:")
        for i in range(len(node_color)):
            print( f'node {i} has color {colors[node_color[i]]}' )
        print()
    dfs(0)

coloring({0: [1,3], 1: [0, 2, 3], 2: [1,3], 3: [0,1,2,4], 4: [3]}, 5, ['Y', 'B', "G"])

        

