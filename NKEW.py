from Bio import Phylo
from io import StringIO

def calculate_distance(tree, node1, node2):
    common_ancestor = tree.common_ancestor(node1, node2)
    distance = tree.distance(common_ancestor, node1) + tree.distance(common_ancestor, node2)
    return distance

def extract_nodes(tree_string):
    lines = tree_string.strip().split('\n')
    nodes_line = lines[-1] #gets last line containing nodes
    nodes = nodes_line.strip().split()
    return tuple(nodes)

input_string = """#paste input here"""

tree_strings = input_string.strip().split('\n\n')

for i, tree_string in enumerate(tree_strings):
    tree_obj = StringIO(tree_string)
    trees = Phylo.parse(tree_obj, "newick")
    nodes = extract_nodes(tree_string)
    tree = next(trees) #assume only 1 tree in each str
    distance = calculate_distance(tree, *nodes)
        
    print(int(distance), end=" ")