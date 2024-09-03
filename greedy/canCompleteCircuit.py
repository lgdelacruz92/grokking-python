from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # to invert the question can you pass your initial index.
        # simplify say. start at i = 0
        # you must visit every gas station
        # i: current station. 
        # gas: [1,2,3,4,5] cost: [3,4,5,1,2]
        # because the solution is unique 
        # the gas[i] - cost[i] of all items must 
        # add to zero. Otherwise, we don't have a unique solution
        # or we have a no solution.
        # The goal to is to just find the starting point
        # that creates a zero

        # The last item that created a positive change.
        n = len(gas)
        diffs = [gas[i] - cost[i] for i in range(n)]

        if sum(diffs) < 0:
            return -1
        
        cur_total = 0
        potential_answer = -1
        for i in range(n):
            cur_total += diffs[i]
            if potential_answer == -1:
                potential_answer = i
            if cur_total < 0:
                potential_answer = -1
                cur_total = 0
        return potential_answer
