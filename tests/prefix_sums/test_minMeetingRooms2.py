from prefix_sums.minMeetingRooms2 import Solution

def test_minMeetingRooms2_1():
    intervals = [[0,30],[5,10],[15,20]]

    solution = Solution()
    expected = 2

    result = solution.minMeetingRooms(intervals)
    assert result == expected

def test_minMeetingRooms2_2():
    intervals = [[7,10],[2,4]]


    solution = Solution()
    expected = 1

    result = solution.minMeetingRooms(intervals)
    assert result == expected

def test_minMeetingRooms2_3():
    intervals = [[13,15],[1,13],[6,9]]


    solution = Solution()
    expected = 2

    result = solution.minMeetingRooms(intervals)
    assert result == expected