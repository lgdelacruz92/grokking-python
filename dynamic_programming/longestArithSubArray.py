from typing import List
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        memo = {}
        def dfs(i,j, memo):
            
            if j > n-1:
                memo[(i,j)] = 0
                return 0
        
            if (i,j) in memo:
                return memo[(i,j)]
            
            x = nums[j] - nums[i]
            
            ans = 1
            for k in range(j+1, n):
                if nums[j] + x == nums[k]:
                    ans = 1 + dfs(j, k, memo)
            memo[(i,j)] = ans
            return ans
        
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, 1 + dfs(i,j, memo))
        return ans
            
            
if __name__ == '__main__':
    solution = Solution()
    # result = solution.longestArithSeqLength([9,4,7,2,10])
    result = solution.longestArithSeqLength([20,1,15,3,10,5,8])
    print(result)