from sliding_window.numberOfSpecialSubstrings import Solution

def test_lengthOfLongestSubstringTwoDistinct_1():
    solution = Solution()
    s = 'ooo'

    expected = 3

    result= solution.numberOfSpecialSubstrings(s)
    assert result == expected