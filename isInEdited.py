def isIn(char, aStr):
    '''
    :param char:
    :param aStr:
    :return: true if char is in aStr, false if not
    '''

    length = len(aStr)
    output = None

    # take care of input string being 0 case
    if length == 0:
        return False
    else:
        middle = aStr[int(length / 2)]

    if middle == char:
        return True

    else:
        if middle > char:
            aStr = aStr[0:int(length/2)]

        # look at back half of string
        if middle < char:
            aStr = aStr[int(length/2) + 1::]

        return isIn(char, aStr)

print(isIn("a", "bcdefg"))


