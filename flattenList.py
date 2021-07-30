def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    outputList = []
    for item in aList:
        if type(item) != list:
            outputList.append(item)
        else:
            outputList += flatten(item)
    return outputList

print(flatten(["a", ["b"], "c"]))


#print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))

