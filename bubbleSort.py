def bubbleSort(L):
    swap = False
    while not swap:
        swap = True
        for i in range(1, len(L)):
            if L[i-1] > L[i]:
                swap = False
                L[i-1], L[i] = L[i], L[i-1]
    return L


print(bubbleSort([4, 3, 2, 1]))
print(bubbleSort([2, 3, 4, 1]))

