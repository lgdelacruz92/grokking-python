from sliding_window.find_max_sliding_window import find_max_sliding_window

def test_find_max_sliding_window():
    nums = [-4,2,-5,3,6]
    k = 3
    expected = [2,3,6]
    result = find_max_sliding_window(nums, k)
    assert expected == result

def test_find_max_sliding_window_2():
    nums = [10,6,9,-3,23,-1,34,56,67,-1,-4,-8,-2,9,10,34,67]
    k = 3
    expected = [10,9,23,23,34,56,67,67,67,-1,-2,9,10,34,67]
    result = find_max_sliding_window(nums, k)
    assert expected == result