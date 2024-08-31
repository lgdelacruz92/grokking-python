from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left_ptr = 0

        n = len(nums)
        cur_sum = 0
        ans = float('inf')
        for right_ptr in range(n):
            cur_sum += nums[right_ptr]
            while cur_sum >= target:
                ans = min(ans, right_ptr - left_ptr+1)
                cur_sum -= nums[left_ptr]
                left_ptr += 1
        return int(ans) if ans != float('inf') else 0
    
    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        return 0
