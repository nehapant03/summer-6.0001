def selectionSort(L):
    for j in range (0, len(L)):
        for i in range(j, len(L)):
            if L[i] < L[j]:
                L[j], L[i] = L[i], L[j]
    return L

print(selectionSort([14, -6, 5, -9, 0]))
