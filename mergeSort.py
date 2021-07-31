def merge(left, right):
    output = []
    i, j = 0, 0
    while i < len(left) and j < len(right): # get through every element in left & right
        if left[i] < right[j]:
            output.append(left[i]) # add the smaller value to the output list
            i += 1 # took care of 1 element in i
        else:
            output.append(right[j])
            j += 1
    # at this point, either i or j is already reached max value
    while i < len(left): # if i is the one w values left
        output.append(left[i]) # dump everything left into output (it's already sorted)
        i += 1
    while j < len(right): # if j is the one w values left
        output.append(right[j])
        j += 1
    return output

print(merge([1, 3, 5, 7], [2, 4, 6, 8]))
