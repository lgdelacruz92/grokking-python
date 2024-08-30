from collections import defaultdict
class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        record = defaultdict(int)

        n = len(s)
        if n == 0:
            return 0
        window_left = 0
        window_right = 0
        record[s[window_right]] += 1
        window_right += 1
        ans = 0
        while window_right < n:
            ans = max(ans, window_right - window_left)
            if s[window_right] not in record:
                if len(record) < 2:
                    record[s[window_right]] += 1
                else:
                    record[s[window_right]] += 1
                    while len(record) > 2:
                        key = s[window_left]
                        record[s[window_left]] -= 1
                        window_left += 1
                        if record[key] == 0:
                            del record[key]
            else:
                record[s[window_right]] += 1
            window_right += 1
        
        ans = max(ans, window_right - window_left)
        return ans