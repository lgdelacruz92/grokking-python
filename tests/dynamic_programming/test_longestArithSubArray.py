from dynamic_programming.longestArithSubArray import Solution

def test_longestArithSubArray_1():
    nums = [3,6,9,12]
    solution = Solution()

    expected = 4
    result = solution.longestArithSeqLength(nums)
    assert expected == result

def test_longestArithSubArray_2():
    nums = [9,4,7,2,10]
    solution = Solution()

    expected = 3
    result = solution.longestArithSeqLength(nums)
    assert expected == result

def test_longestArithSubArray_3():
    nums = [20,1,15,3,10,5,8]
    solution = Solution()

    expected = 4
    result = solution.longestArithSeqLength(nums)
    assert expected == result