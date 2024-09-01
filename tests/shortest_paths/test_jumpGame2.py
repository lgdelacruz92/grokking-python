from shortest_paths.jumpGame2 import Solution

def test_jumpGame2_1():
    nums = [2,3,1,1,4]
    solution = Solution()

    expected = 2
    result = solution.jump(nums)
    assert result == expected

def test_jumpGame2_2():
    nums = [2,3,0,1,4]
    solution = Solution()

    expected = 2
    result = solution.jump(nums)
    assert result == expected