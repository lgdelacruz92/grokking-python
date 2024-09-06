from typing import Optional, List
from lib.tree_node import TreeNode

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        def backtrack(node, cur_sum, ans):
            if not node:
                return

            cur_sum.append(node.val)
            if sum(cur_sum) == targetSum:
                ans.append(cur_sum[:])

            if node.left:
                backtrack(node.left, cur_sum, ans)
            
            if node.right:
                backtrack(node.right, cur_sum, ans)
            cur_sum.pop()

        ans = []
        backtrack(root, [], ans)
        return ans