def prime_factors(n):
    prime_factors1arr = []

    # If n is a negative number, we add -1 as a prime factor
    # And make n positive
    if n < 0:
        prime_factors1arr.append(-1)
        n = -n

    for i in range(2, int((n / 2) + 1)):
        while n % i == 0:
            prime_factors1arr.append(i)
            n = int(n / i)
            if n == 1:
                return prime_factors1arr
    # If there are no prime factors, just return the number as an array
    prime_factors1arr.append(n)
    return prime_factors1arr

def lowest_common_multiple2(arr1, arr2):
    i = 0
    j = 0
    lcm = 1

    while i < len(arr1) and j < len(arr2):
        v1 = arr1[i]
        v2 = arr2[j]
        if v1 == v2:
            lcm = lcm * v1
            i = i + 1
            j = j + 1
        elif v1 < v2:
            lcm = lcm * v1
            i = i + 1
        elif v1 > v2:
            lcm = lcm * v2
            j = j + 1

    while i < len(arr1):
        v1 = arr1[i]
        lcm = lcm * v1
        i = i + 1

    while j < len(arr2):
        v2 = arr2[j]
        j = j + 1
        lcm = lcm * v2

    return lcm

