n = 4 #input n

def count_internal_nodes(n):
    return n-2 #each end node has 2 leaves, child has to have degree 3, hence if it is linked to parent and has child -> already has degree 2 and can only aquire 1 edge
