from greedy.canCompleteCircuit import Solution

def test_canCompleteCircuit_1():
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    solution = Solution()
    expected = 3
    result = solution.canCompleteCircuit(gas, cost)
    assert result == expected

def test_canCompleteCircuit_2():
    gas = [2,3,4]
    cost = [3,4,3]

    solution = Solution()
    expected = -1
    result = solution.canCompleteCircuit(gas, cost)
    assert result == expected

def test_canCompleteCircuit_3():
    gas = [5,8,2,8]
    # if i = 1
    # tank - 6 + 8
    # 1: tank[i] = tank[i-1] - cost[i-1] + gas[i] = tank[i-1] - 6 + 8 
    # 0: tank[i-1] = tank[i-2] - cost[i-2] + gas[i-1] = tank[i-2] - 6 + 5
    # 3: tank[i-2] = tank[i-3] - cost[i-3] + gas[i-2] = tank[i-3] - 6 + 8
    # 2: tank[i-3] = tank[i-4] - cost[i-4] + gas[i-3] = tank[i-4] - 5 + 2
    cost = [6,5,6,6]

    solution = Solution()
    expected = 3
    result = solution.canCompleteCircuit(gas, cost)
    assert result == expected

def test_canCompleteCircuit_4():
    gas = [1,2,3,4,5,5,70]
    cost = [2,3,4,3,9,6,2]

    solution = Solution()
    expected = 6
    result = solution.canCompleteCircuit(gas, cost)
    assert result == expected