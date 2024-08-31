from prefix_sums.minSubArrayLen import Solution

def test_minSubArrayLen_1():
    target = 7
    nums = [2,3,1,2,4,3]
    solution = Solution()
    result = solution.minSubArrayLen(target, nums)
    result = solution.minSubArrayLen2(target, nums)

    expected = 2
    assert result == expected

def test_minSubArrayLen_2():
    target = 4
    nums = [1,4,4]
    solution = Solution()
    result = solution.minSubArrayLen(target, nums)
    result = solution.minSubArrayLen2(target, nums)

    expected = 1
    assert result == expected

def test_minSubArrayLen_3():
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    solution = Solution()
    result = solution.minSubArrayLen(target, nums)
    result = solution.minSubArrayLen2(target, nums)

    expected = 0
    assert result == expected