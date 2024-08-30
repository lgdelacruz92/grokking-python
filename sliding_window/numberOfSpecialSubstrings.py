from collections import defaultdict
class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        right_ptr = 0
        left_ptr = 0
        record = defaultdict(int)
        for right_ptr in range(n):
            record[s[right_ptr]] += 1
            if record[s[right_ptr]] > 1:
                while left_ptr != right_ptr:
                    record[s[left_ptr]] -= 1
                    left_ptr += 1
                    ans += right_ptr + 1 - left_ptr
            else:
                ans += right_ptr + 1 - left_ptr
        return ans