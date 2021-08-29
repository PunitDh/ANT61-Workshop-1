from Queue import Queue

def range_in_sum(nlist, esum):
    
    l = 0
    r = 0
    current_sum = 0
    list_length = len(nlist)
    queue = Queue(list=[])
    
    while current_sum < esum and l < list_length and r < list_length:
        queue.push(nlist[r])
        current_sum = queue.calc_sum()        
        while current_sum > esum:
            queue.pop()
            l += 1
            current_sum = queue.calc_sum()            
            if current_sum == esum:
                return (l,r)
            # end if
        # end while
        r += 1
    # end while
    
    return None
# end range_in_sum


def max_possible_sum_old(nlist):
    sum_matrix = []
    indices = []
    sums = []
    current_sum = 0
    list_length = len(nlist)
    l = 0
    r = 0

    for i in range(0,list_length):
        for j in range(i,list_length):
            indices.append((i,j))
            sums.append(sum(nlist[i:j+1]))
    sum_matrix.append(indices)
    sum_matrix.append(sums)
    
    max_sum_range = sum_matrix[0][sum_matrix[1].index(max(sums))]
        
    return max_sum_range
# end max_possible_sum



def max_possible_sum(nlist):
    l = 0
    r = len(nlist)-1
    length = len(nlist)
    sums = [[],[]]
    current_max_sum = 0
    

    while r-l > 0:
        sums[0].append(sum(nlist[l:r+1]))
        sums[1].append((l,r))
        if nlist[l] < nlist[r]:
            l += 1
        elif nlist[l] > nlist[r]:
            r -= 1
        else:
            l += 1
            r -= 1
    if l == 0 or nlist[l-1] < nlist[l]:
        while r < length:
            sums[0].append(sum(nlist[l:r+1]))
            sums[1].append((l,r))
            r += 1
    elif r == length-1 or nlist[r+1] < nlist[r]:
        while l >= 0:
            sums[0].append(sum(nlist[l:r+1]))
            sums[1].append((l,r))
            l -= 1
    else:
        return sums[1][sums[0].index(max(sums[0]))]
    
    return sums[1][sums[0].index(max(sums[0]))]
    
    
# end max_possible_sum


def max_possible_sum_o_n(nlist):
    l = 0
    r = 0
    s = 0
    current_max_sum = -99999999999999999999999999999999999999999999999
    max_end = 0
    length = len(nlist)
    
    for i in range(0,length):
        max_end += nlist[i]
        
        if current_max_sum < max_end:
            current_max_sum = max_end
            l = s
            r = i
        
        if max_end < 0:
            max_end = 0
            s = i + 1
    return (l,r)
# end max_possible_sum