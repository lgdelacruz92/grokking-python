from prefix_sums.sumRegion import NumMatrix

def test_sumRegion_1():
    matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]

    matrix_obj = NumMatrix(matrix)
    range = [2,1,4,3]

    expected = 8
    result = matrix_obj.sumRegion(range[0], range[1], range[2], range[3])
    assert result == expected

def test_sumRegion_2():
    matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]

    matrix_obj = NumMatrix(matrix)
    range = [1,1,2,2]

    expected = 11
    result = matrix_obj.sumRegion(range[0], range[1], range[2], range[3])
    assert result == expected

def test_sumRegion_3():
    matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]

    matrix_obj = NumMatrix(matrix)
    range = [1,2,2,4]

    expected = 12
    result = matrix_obj.sumRegion(range[0], range[1], range[2], range[3])
    assert result == expected