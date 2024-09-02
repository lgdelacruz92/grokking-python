from collections import defaultdict
from typing import List
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 2
        # this problem is very hard
        # here is the intuition

        # every sequence must start with a fixed
        # i, j and x is the common difference
        # recall that arithmetic seq is a + x*d
        # where d is the number of items in the sequence
        # this means we can find k where k > j that is the next
        # item in the sequence. 
        # We can check if k is the next item of the sequence if 
        # it satifies this condition nums[k] - nums[j] == nums[j] - nums[i]

        # here we can build a record of differences
        # dp[x] where x is all the nums[j] - nums[i]. i.e the common difference x
        # dp[x][j] where j is the last index of this difference
        n = len(nums)
        dp = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            for j in range(i+1, n):
                x = nums[j]- nums[i]
                dp[x][j] = 2
        
        # answer will always be at least two else
        # there is no sequence
        ans = 2

        # here we find x2: nums[k] - nums[j] = x2
        # Then we check if we've already seen that common diff x2
        # then we check if we've already seen that last item j
        # if so then we have a new item in the dp ending in k and numberof items dp[x][j] + 1
        # hence dp[x][k] = dp[x][j] + 1
        for j in range(1, n):
            for k in range(j+1, n):
                x = nums[k] - nums[j]
                if x in dp and j in dp[x]:
                    dp[x][k] = dp[x][j] +1
                    ans = max(dp[x][k], ans)
        return ans
            