from typing import List

class Solution:
    """
        This method uses sliding_window technique to solve this problem
    """
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
    
    """
    This method uses prefix sums technique
    """
    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        if sum(nums) < target:
            return 0

        prefix_sums = [0] * n
        prefix_sums[0] = nums[0]
        for i in range(1,n):
            prefix_sums[i] = prefix_sums[i-1] + nums[i]
        
        # prefix_sums is guaranteed prefix
        # e.g nums: [1,2,3] -> prefix_sums: [1,2+1,3+2+1] : [1,3,6]
        # target: 3
        # [1] not valid
        # 
        
        # at this point. I'm guaranteed to have an answer
        i = 0
        while i < n:
            if prefix_sums[i] >= target:
                break
            i += 1
        
        left = 0
        ans = i+1
        for right in range(i, n):
            # This has to be hold true to be an answer
            # prefix_sums[right] - prefix_sums[left] is always >= target is
            # a potential answer no matter what
            while prefix_sums[right] - prefix_sums[left] >= target:
                ans = min(ans, right - left)
                left += 1
        return ans
