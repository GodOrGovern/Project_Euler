''' The most naive way of computing n15 requires fourteen multiplications: We
shall define m(k) to be the minimum number of multiplications to compute n^k.
For 1 ≤ k ≤ 200, find ∑m(k) '''

class Node(object):
    ''' Represents a node on a tree '''
    def __init__(self, val, parent=None):
        self.value = val
        self.parent = parent
    def __repr__(self):
        return str(self.value)
    def get_ancestry(self):
        ''' Return a list of the node's ancestors, including the node itself '''
        ancestors = []
        cur = self
        while cur:
            ancestors.append(cur)
            cur = cur.parent
        return ancestors

def main():
    ''' Driver function '''
    print(sum_of_m_to(200))

def sum_of_m_to(end):
    ''' Build a tree where each layer contains all values with additions
    chains of that length. Returns ∑m(k) for k = 1 to 'end'. Fairly
    inefficient as the tree is not pruned '''
    total = 1
    root = Node(1)
    old_row = [Node(2, root)]
    index = 1
    vals = {1, 2}
    while len(vals) != end:
        new_row = []
        for node in old_row:
            for v in (n.value for n in node.get_ancestry()):
                val = node.value + v
                if val <= end:
                    new = Node(val, node)
                    new_row.append(new)
                    if val not in vals:
                        total += index + 1
                        vals.add(val)
        old_row = new_row
        index += 1
    return total

if __name__ == "__main__":
    main()
