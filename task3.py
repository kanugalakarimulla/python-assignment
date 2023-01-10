# Q3. Write a generator function that yields the next prime number on each iteration.

# Sample Input output

# Input: 5
# Output: [2, 3, 5, 7, 11]

# Input: 10
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def isprime(n):
    for i in range(2, int((n**0.5))+1):
        if n % i == 0:
            return False
    return True


def get_primes(n):
    yield 2
    i = 1
    count = 1
    while count < n:
        i += 2
        if isprime(i):
            count += 1
            yield i


print(list(get_primes(10)))
