def generatePrimes():
    primes = []
    isPrime = True
    current = 2
    while True:
        isPrime = True
        for item in primes:
            if current % item == 0:
                isPrime = False
        if isPrime:
            primes.append(current)
            yield current
        current += 1

gen = generatePrimes()

print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())


def genFib():
    fib1 = 0
    fib2 = 1

    while True:
        next = fib1 + fib2
        yield next
        fib2 = fib1
        fib1 = next

# fib = genFib()
# print(fib.__next__())
# print(fib.__next__())
# print(fib.__next__())