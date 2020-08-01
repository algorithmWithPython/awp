from collections import defaultdict
# This is the TreeNode we will use at the end when we 
# build up the tree
class TreeNode:
    def __init__(self, val, parent, children=[]):
        self.val = val
        # parent of root is None
        self.parent= parent
        self.children = children

    def setChildren(self, children):
        self.children = children

# this class is used to save a tree structure we can
# use, which represend the original undirected graph.
# self.node_values represent node values for each node. 
# the index of the node is used in self.node_edge. 
# self.node_edge is the adjacent list for each node.
class Tree:
    def __init__(self, node_values, edges):
        self.node_values = node_values
        self.node_edge = defaultdict(list)
        for edge in edges:
            self.node_edge[edge[0]].append(edge[1])
            self.node_edge[edge[1]].append(edge[0])

# the function to find the tree root. It will
# return index(es) of either one or two elements.
# (because there could be one or two root candidates)
def tree_root(node_values, edges):
    tree = Tree(node_values, edges)
    number_of_nodes = len(node_values)
    edges_from_node = [0]*number_of_nodes # each node has how many edges out from it. 
    leaves = [] # leave nodes, has only one edge out from it.
    for i in range(number_of_nodes):
        edges_from_node[i] = len(tree.node_edge[i])
        if edges_from_node[i] <= 1:
            leaves.append(i)
            edges_from_node[i] = 0 # set to 0 so this leave node will not be used any more.
    count = len(leaves)
    while count < number_of_nodes:
        new_leaves = []
        for leaf_node in leaves:
            for node in tree.node_edge[leaf_node]:
                edges_from_node[node] -= 1
                if edges_from_node[node] == 1:
                    new_leaves.append(node)
                    edges_from_node[node] = 0
        count += len(new_leaves)
        leaves = new_leaves
    return leaves

print(tree_root([0,1,2,3,4,5,6], [[3,2], [2,0], [0,1], [0,5], [5,4], [5,6]])) #graph on page 12th
print(tree_root([0,1,2,3,4,5,6,7,8,9], [[0,1], [1,2], [2,3], [2,9], [2,6], [3,4], [3,5], [6,7], [6,8]])) #graph on page 17th
print(tree_root([0,1,2,3,4,5,6,7,8,9], [[0,1], [1,4], [1,3], [2,3], [3,6], [3,7], [6,9], [4,8], [4,5]])) #graph on page 20th

# convert the graph to tree, the root node has value of root_node_value
def convert_to_tree(node_values, edges, root_node_value):
    tree = Tree(node_values, edges)
    # TODO move easy if use node/parent index instead of value
    def buildTree(node_value, parent):
        node = TreeNode(node_value, parent)
        children = []
        node_index = node_values.index(node_value)
        parent_index = node_values.index(parent.val) if parent else -1 
        for child_idx in tree.node_edge[node_index]:
            if child_idx != parent_index: # parent is also in tree.node_edge[node_index]
                children.append(buildTree(node_values[child_idx], node))
        node.setChildren(children)
        return node
    return buildTree(root_node_value, None)

# root is the root TreeNode of the tree, TreeNode is defined
# at the begining of this file
def tree_serialization(root):
    def serialize(node):
        node_serilization = []
        for node in node.children:
            node_serilization.append(serialize(node))
        if node_serilization:
            node_serilization.sort() # sort is important, make sure same order of the children 
        return '(' + ''.join(node_serilization) + ')'
    return serialize(root)

#g1 and g2 are 2 graphs can be converted to tree
#this method compare if g1 and g2 are the same graph
def same_graph(g1_node_values, g1_edges, g2_node_values, g2_edges):
    roots1 = tree_root(g1_node_values, g1_edges)
    roots2 = tree_root(g2_node_values, g2_edges)

    root1_value = g1_node_values.index(roots1[0])
    root1_node = convert_to_tree(g1_node_values, g1_edges, root1_value)

    for root2 in roots2:
        root2_value = g2_node_values.index(root2)
        root2_node = convert_to_tree(g2_node_values, g2_edges, root2_value)
        if tree_serialization(root1_node) == tree_serialization(root2_node):
            return True
    return False

print(same_graph([0,1,2,3,4,5],
                 [(0,1), (1,2), (2,3), (2,4), (2,5)],
                 [0,1,2,3,4,5],
                 [(1,0), (1,2), (1,4), (4,3), (4,5)])) # page 22

print(same_graph([0,1,2,3,4,5,6],
                 [(0,1), (0,2), (2,5), (2,3), (2,6), (3,4)],
                 [0,1,2,3,4,5,6],
                 [(1,2), (3,2), (3,0), (4,3), (3,5), (5,6)])) # page 22



