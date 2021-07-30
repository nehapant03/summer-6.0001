def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    #without returns

    length = len(aStr)

    # take care of input string being 0 case
    if length == 0:
        return False
    else:
        middle = aStr[int(length / 2)]

    output = None

    if length == 1:
        if middle == char:
            output = True
        else:
            output = False

    else:

        if middle > char:
            aStr = aStr[0:int(length/2)]

        elif middle < char:
            aStr = aStr[int(length/2) + 1::]

        else:
            aStr = middle

        output = isIn(char, aStr)

    return output


print(isIn("b", "abcdef"))



