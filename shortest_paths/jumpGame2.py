from typing import List
from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return 0
        
        cur_index = 0
        count = 0
        while cur_index != n-1:
            if cur_index + nums[cur_index] >= n-1:
                return count + 1
            max_next_index = 0
            cur_max = 0
            count += 1
            for next_index in range(cur_index+1, cur_index + nums[cur_index] + 1):
                if next_index + nums[next_index] > cur_max:
                    cur_max = next_index + nums[next_index]
                    max_next_index = next_index
            cur_index = max_next_index
        return count