from greedy.canJump import Solution

def test_canJump_1():
    nums = [2,3,1,1,4]
    expected = True

    solution = Solution()
    result = solution.canJump(nums)
    assert result == expected

def test_canJump_2():
    nums = [3,2,1,0,4]
    expected = False

    solution = Solution()
    result = solution.canJump(nums)
    assert result == expected