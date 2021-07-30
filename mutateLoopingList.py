def f(i):
    return i + 2
def g(i):
    return i > 5



def applyF_filterG(L, f, g):
    L_copy = L[:]
    for item in L_copy:
        num = f(item)
        if not g(num):
            L.remove(item)
    try:
        maximum = max(L)
    except:
        maximum = -1
    return maximum


L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)




