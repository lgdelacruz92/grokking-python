from collections import defaultdict
import heapq
def find_max_sliding_window(nums, w):
    max_h = []
    for i in range(w):
        heapq.heappush(max_h, -nums[i])
    
    ans = []
    ans.append(-max_h[0])
    delayed_del = defaultdict(int)
    for i in range(1, len(nums) - w + 1):
        next_num = nums[i+w-1]
        prev_num = nums[i-1]

        delayed_del[prev_num] += 1
        while max_h and -max_h[0] in delayed_del and delayed_del[-max_h[0]] > 0:
            delayed_del[-max_h[0]] -= 1
            heapq.heappop(max_h)
        
        heapq.heappush(max_h, -next_num)
        ans.append(-max_h[0])
    return ans


        