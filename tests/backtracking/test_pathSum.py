from lib.utils import make_tree_node_from_array, print_tree_node
from backtracking.pathSum import Solution

def test_pathSum_1():
    arr = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    targetSum = 22
    tree_node = make_tree_node_from_array(arr)

    print_tree_node(tree_node)
    solution = Solution()
    expected = [[5,4,11,2],[5,8,4,5]]
    result = solution.pathSum(tree_node, targetSum)
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert len(r) == len(e)
        for r1, e1 in zip(r,e):
            assert r1 == e1