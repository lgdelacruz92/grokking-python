from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.children = None
    
    def add_child(self, node):
        if self.children:
            self.children.append(node)
        else:
            self.children = [node]
    
    def print_trie(self):

        q = deque()
        q.append([self])
        while q:
            next_batch = q.popleft()
            
            print([item.val for item in next_batch])
            for item in next_batch:
                if item.children:
                    next_children = []
                    for child in item.children:
                        next_children.append(child)
                    q.append(next_children)

class Trie:
    def __init__(self):
        self.root = None
    
    def add_word(self, w):
        if len(w) == 0:
            return
        if not self.root:
            self.root = Node(w[0])
        
        next_node = self.root
        for c in w[1:]:
            new_node = Node(c)
            next_node.add_child(new_node)
            next_node = new_node
    
    def print_trie(self):
        if self.root:
            self.root.print_trie()

def test_1():
    root = Node('w')
    o = Node('o')
    r = Node('r')
    d = Node('d')
    e = Node('e')
    r.add_child(e)
    r.add_child(d)
    o.add_child(r)
    root.add_child(o)

def test_2():
    root = Trie()
    root.add_word('word')
    root.print_trie()
    root.add_word('wore')

test_2()
