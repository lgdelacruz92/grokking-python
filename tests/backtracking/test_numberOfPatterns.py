from backtracking.numberOfPatterns import Solution

def test_numberOfPatterns_1():
    m = 1
    n = 3

    expected = 385
    solution = Solution()
    result = solution.numberOfPatterns(m, n)
    assert result == expected