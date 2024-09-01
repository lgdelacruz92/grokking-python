from typing import List
from collections import defaultdict
import heapq

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0:
            return False

        cur_last_pos = n - 1
        for i in range(n-1, -1, -1):
            if i+nums[i] >= cur_last_pos:
                cur_last_pos = i

        return cur_last_pos == 0