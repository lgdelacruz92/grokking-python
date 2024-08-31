from sliding_window.numberOfSpecialSubstrings import Solution

def test_numberOfSpecialSubstrings_1():
    solution = Solution()
    s = 'ooo'

    expected = 3

    result= solution.numberOfSpecialSubstrings(s)
    assert result == expected

def test_numberOfSpecialSubstrings_2():
    solution = Solution()
    s = 'abcd'

    expected = 10

    result= solution.numberOfSpecialSubstrings(s)
    assert result == expected

def test_numberOfSpecialSubstrings_3():
    solution = Solution()
    s = 'abab'

    expected = 7

    result= solution.numberOfSpecialSubstrings(s)
    assert result == expected