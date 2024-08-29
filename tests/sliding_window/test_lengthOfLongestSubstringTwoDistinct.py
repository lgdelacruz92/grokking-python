from sliding_window.lengthOfLongestSubstringTwoDistinct import Solution
def test_lengthOfLongestSubstringTwoDistinct_1():
    s = "eceba"

    expected = 3
    solution = Solution()
    result = solution.lengthOfLongestSubstringTwoDistinct(s)

    assert result == expected


def test_lengthOfLongestSubstringTwoDistinct_2():
    s = "ccaabbb"

    expected = 5
    solution = Solution()
    result = solution.lengthOfLongestSubstringTwoDistinct(s)

    assert result == expected


def test_lengthOfLongestSubstringTwoDistinct_3():
    s = "abaccc"

    expected = 4
    solution = Solution()
    result = solution.lengthOfLongestSubstringTwoDistinct(s)

    assert result == expected