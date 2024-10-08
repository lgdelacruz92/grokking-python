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

def test_jumpGame2_3():
    nums = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
    solution = Solution()

    expected = 13
    result = solution.jump(nums)
    assert result == expected

def test_jumpGame2_4():
    nums = [1,2,3]
    solution = Solution()

    expected = 2
    result = solution.jump(nums)
    assert result == expected