def bubbleSort(L):

    cleanPass = False
    while not cleanPass:
        cleanPass = True
        for i in range(1, len(L)):
            if L[i-1] > L[i]:
                L[i-1], L[i] = L[i], L[i-1]
    return L

print(bubbleSort([2, 7, 3, 4]))