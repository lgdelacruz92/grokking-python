def min_window(str1, str2):
    
    # Replace this placeholder return statement with your code
    n1 = len(str1)
    n2 = len(str2)

    if n2 > n1:
        return ''

    p2 = 0
    window_range = [0,0]
    cur_ans = str1
    no_answer = True
    while window_range[0] < n1 and str1[window_range[0]] != str2[p2]:
        window_range[0] += 1
    if window_range[0] > window_range[1]:
        window_range[1] = window_range[0]
    while window_range[1] < n1:
        if str1[window_range[1]] == str2[p2]:
            if p2 == n2-1:
                no_answer = False
                potential_ans = str1[window_range[0]:window_range[1]+1]
                cur_ans = potential_ans if  len(potential_ans) < len(cur_ans) else cur_ans
                p2 = 0
                window_range[0] += 1
                while window_range[0] < n1 and str1[window_range[0]] != str2[p2]:
                    window_range[0] += 1
                window_range[1] = window_range[0]
                window_range[1] -=1
            else:
                p2 += 1
        window_range[1] += 1
    ans = cur_ans
    return ans if not no_answer else ''
