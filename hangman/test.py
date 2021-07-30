import math
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here

    # exp = math.floor(math.log(num, base))
    #
    # if abs(num - (base ** exp)) < abs(num - (base ** (exp - 1))):
    #    exp += 1
    # else:
    #     exp += 0
    #
    # delta = num - (base ** exp)
    #
    # if abs(delta) > abs(num - 1):
    #     exp = 0
    #
    # return exp

    prev = num
    delta = num

    for exp in range(0, int(num)):
        delta = abs(num - base ** exp)
        print(exp, delta)
        if delta >= prev:
            break
        prev = delta
    if exp == 0:
        return 0
    else:
        return exp - 1




print(closest_power(4, 12))