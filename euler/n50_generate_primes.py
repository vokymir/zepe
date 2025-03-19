
import math
import random
import sys

def one_test(n:int, a:int) -> bool:
    """
    One test in the miller-rabin primality test - test primality of 'n' for given number 'a'.
    More info in miller_rabin() method.
    """
    exp:int = n - 1

    while not exp & 1:
        exp >>= 1

    if pow(a, exp, n) == 1:
        return True

    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            return True

        exp <<= 1

    return False


def miller_rabin(n:int, k:int = 40) -> bool:
    """
    Miller-Rabin primality test - test if n is prime.
    The test is run k-times, granting (1 - 1/(2^k)) certainty - meaning it is 'probably' a prime.
    More about M-R test: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    Implemented with a help of a video: https://www.youtube.com/watch?v=-BWTS_1Nxao
    """
    if n < 2:
        return False
    if n in [2,3]:
        return True

    for i in range(k):
        r = random.randint(2, n - 1)
        if not one_test(n, r):
            return False

    return True


def sieve_of_eratosthenes(n:int) -> list[int]:
    """
    Generate array of primes from 2 up to n.
    Using sieve of Eratosthenes.
    Implemented based on Wikipedia article: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    array:bytearray = bytearray(b'\x01') * (n + 1)
    array[:2] = b'\x00\x00'
    index:int = 0
    res:list[int] = list()

    while index * index < n:

        if array[index]:
            array[index * index : n + 1 : index] = b'\x00' * ( (n - index*index) // index + 1 )

        index += 1

    for i in range(len(array)):
        if array[i]:
            res.append(i)

    return res


def estimate_required_primes(n:int) -> int:
    """
    Estimate how many primes are needed to exceed 'n' in sum.
    """
    m:int = 1024

    while (m * m * math.log(m)) / 2 < n:
        m *= 2

    return int(m * math.log(m) * 1.2)

def find_longest_prime_sum(n:int) -> tuple[int,int]:
    """
    Finds the largest prime that is a sum of the most consecutive primes, where the prime is smaller than n.
    """
    if n <= 3:
        return n, 1

    estimate:int = estimate_required_primes(n)

    primes = sieve_of_eratosthenes(estimate)

    # using dynamic programming prefix sum
    prefix = [0]
    for p in primes:
        prefix.append(prefix[-1] + p)

    # max chain length possible
    len_pos:int = 0
    for leng, summa in enumerate(prefix):
        if summa <= n:
            len_pos = leng
        else:
            break

    # longest prime sum search
    for length in range(len_pos, 0, -1):
        summa:int = prefix[length]

        if summa <= n and miller_rabin(summa):
            return summa, length

        for i in range(1, len(primes) - length + 1):
            summa = prefix[i + length] - prefix[i]

            if summa > n:
                break
            if miller_rabin(summa):
                return summa, length

    return 0, 0


def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        prime, length = find_longest_prime_sum(n)
        print(prime, length)

if __name__ == "__main__":
    main()





