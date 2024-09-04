from lib.utils import make_tree_node_from_array, print_tree_node
from lib.tree_node import TreeNode

def make_test1_expected():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    return root

def assert_root(root1, root2):
    if root1 is None or root2 is None:
        return
    assert type(root1) == type(root2)
    assert root1.val == root2.val

    assert_root(root1.left, root2.left)
    assert_root(root1.right, root2.right)

def test_utils_1():
    arr = [5,4,8,11,None,13,4]

    expected = make_test1_expected()
    result = make_tree_node_from_array(arr)
    # print_tree_node(result)
    assert_root(expected, result)
    